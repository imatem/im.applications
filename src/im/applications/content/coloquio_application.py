# -*- coding: utf-8 -*-
from DateTime import DateTime
from datetime import timedelta
from im.applications import _
from im.applications.utilities import cleanPermissionsCommissions
from im.applications.utilities import createViaticalControl
from im.applications.utilities import createLandticketControl
from im.applications.utilities import createAirticketControl
from im.applications.utilities import getGroupsCommision
from plone import api
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.supermodel import model
from Products.CMFCore.utils import getToolByName
from zope import schema
from zope.interface import implementer
from zope.interface import Invalid
from zope.interface import invariant
from im.applications.content.moneysack import Moneysack


from z3c.form import validator
# from z3c.form.interfaces import IValidator
import zope.schema
from z3c.form import util


class IColoquioApplication(model.Schema):
    """ Marker interface and Dexterity Python Schema for ColoquioApplication
    """

    directives.read_permission(campus='cmf.ManagePortal')
    directives.write_permission(campus='cmf.ManagePortal')
    campus = schema.Choice(
        title=_(u'label_applications_campus', default=u'Campus Applications'),
        vocabulary='im.applications.IMCampus',
        required=False,
    )

    title = schema.TextLine(
        title=_(u'label_applications_coloquio_title', default=u'Speaker Name'),
        required=True,
    )

    institution = schema.TextLine(
        title=_(u'label_applications_coloquio_institution', default=u'Speaker Institution'),
        required=True,
    )

    exposition_date = schema.Date(
        title=_(u'label_applications_coloquio_exposition_date', default=u'Exposition Date'),
        required=True,
    )

    comments = schema.Text(
        title=_(u'label_applications_comments', u'Adtional Comments'),
        required=False,
    )

    directives.read_permission(specialc_date='im.applications.ViewComision')
    directives.write_permission(specialc_date='im.applications.EditComision')
    specialc_date = schema.Date(
        title=_(u'label_applications_amount_specialc_date', default=u'Special Comision Date'),
        required=True,
    )

    directives.read_permission(comments_recommended='im.applications.ViewComision')
    directives.write_permission(comments_recommended='im.applications.EditComision')
    comments_recommended = schema.Text(
        title=_(u'label_applications_comments_recommended', u'Special Comision Comments'),
        required=False,
    )

    directives.read_permission(minute='im.applications.ViewConsejo')
    directives.write_permission(minute='im.applications.EditConsejo')
    minute = schema.TextLine(
        title=_(u'label_applications_minute', default=u'Minute Number'),
        description=_(u'help_applications_minute', default=u'Minute of Consejo Interno'),
        required=False,
    )

    directives.read_permission(internalc_date='im.applications.ViewConsejo')
    directives.write_permission(internalc_date='im.applications.EditConsejo')
    internalc_date = schema.Date(
        title=_(u'label_applications_amount_internalc_date', default=u'Consejo Interno Date'),
        required=True,
    )

    directives.read_permission(comments_authorized='im.applications.ViewConsejo')
    directives.write_permission(comments_authorized='im.applications.EditConsejo')
    comments_authorized = schema.Text(
        title=_(u'label_applications_comments_authorized', u'Consejo Interno Comments'),
        required=False,
    )


class DateInRangeValidator(validator.SimpleFieldValidator):
    """z3c.form validator class for exposition date
    """
    # zope.interface.implements(IValidator)
    def validate(self, value):
        """Validate international phone number on input
        """
        super(DateInRangeValidator, self).validate(value)
        if value:
            if value < self.context.start:
                raise Invalid(_(u"The start date must be grather than '${name}'", mapping={'name': self.context.start}))


validator.WidgetValidatorDiscriminators(
    DateInRangeValidator, field=IColoquioApplication['exposition_date'])

zope.component.provideAdapter(DateInRangeValidator)


class AmountMaxValidator(validator.InvariantsValidator):
    """
    This validator verify the max amount permitted
    """

    def validate(self, obj):
        errors = super(AmountMaxValidator, self).validateObject(obj)

        xrequest = self.request
        transportation = xrequest['form.widgets.ITransportationexpenses.amount_transportation'] or '0.0'
        viatical = xrequest['form.widgets.ITravelexpenses.amount_travel'] or '0.0'
        total = eval(transportation) + eval(viatical)

        if self.context:
            # ya está creado el objeto
            parent = self.context.aq_parent
        else:
            parent = [xparent for xparent in xrequest['PARENTS'] if isinstance(xparent, Moneysack)][0]

        if parent.amountmax:
            if total > parent.amountmax:
                errors += (Invalid(_(u"The amount must be smaller than '${amountmax}'", mapping={'amountmax': parent.amountmax})), )

        if parent.remaining_amount() < total:
            errors += (Invalid(_(u"The amount available is less than the amount requested, you dispose of '${remainingamount}'", mapping={'amountmax': parent.remaining_amount})), )

        return errors

validator.WidgetsValidatorDiscriminators(
    AmountMaxValidator, schema=util.getSpecification(IColoquioApplication, force=True))

zope.component.provideAdapter(AmountMaxValidator)


@implementer(IColoquioApplication)
class ColoquioApplication(Item):
    """
    """
    def hasSpecialDate(self):
        if self.specialc_date:
            return True

        return False

    def hasInternalDate(self):
        if self.internalc_date:
            return True

        return False

    def getIdOwner(self):
        return self.getOwner().getId()

    def nombre_owner(self):
        ownerid = self.getIdOwner()
        member = api.content.find(portal_type='FSDPerson', id=ownerid)[0].getObject()
        if member.apellidoMaterno:
            lastN = member.lastName + ' ' + member.apellidoMaterno
        else:
            lastN = member.lastName

        return lastN + ', ' + member.firstName

    def campus_owner(self):
        if self.campus:
            return self.campus
        ownerid = self.getIdOwner()
        member = api.content.find(portal_type='FSDPerson', id=ownerid)[0].getObject()
        return member.sede

    def prepareToCommission(self):

        # with api.env.adopt_user(username='admin'):
        self.amount_travel_recommended = self.amount_travel
        self.amount_transportation_recommended = self.amount_transportation
        if self.campus:
            cleanPermissionsCommissions(self)
            groups = getGroupsCommision(self.campus)

        else:
            ownerid = self.getIdOwner()
            member = api.content.find(portal_type='FSDPerson', id=ownerid)[0].getObject()
            self.campus = member.sede
            groups = getGroupsCommision(member.sede)

        api.group.grant_roles(groupname=groups['commissioners'], roles=['IMComisionado'], obj=self)
        api.group.grant_roles(groupname=groups['assistants'], roles=['IMComisionado', 'Editor'], obj=self)

        return True

    def prepareToConsejo(self):
        self.amount_travel_authorized = self.amount_travel_recommended
        self.amount_transportation_authorized = self.amount_transportation_recommended

        if self.campus:
            groups = getGroupsCommision(self.campus)

        else:
            ownerid = self.getIdOwner()
            member = api.content.find(portal_type='FSDPerson', id=ownerid)[0].getObject()
            self.campus = member.sede
            groups = getGroupsCommision(member.sede)

        cleanPermissionsCommissions(self)
        api.group.grant_roles(groupname=groups['commissioners'], roles=['IMComisionado'], obj=self)
        api.group.grant_roles(groupname=groups['assistants'], roles=['IMComisionado'], obj=self)
        api.group.grant_roles(groupname='imconsejeros', roles=['IMConsejero'], obj=self)
        api.group.grant_roles(groupname='assistants_imconsejeros', roles=['IMComisionado', 'Editor'], obj=self)

        return True

    def prepareToApprove(self):
        self.amount_travel_used = self.amount_travel_authorized
        self.amount_transportation_used = self.amount_transportation_authorized
        self.createControls()
        self.sendMail()

    def prepareToReject(self):
        self.amount_travel_used = 0
        self.amount_transportation_used = 0
        self.sendMail('rechazada')

    def returnToCommission(self):
        if self.campus:
                groups = getGroupsCommision(self.campus)

        else:
            ownerid = self.getIdOwner()
            member = api.content.find(portal_type='FSDPerson', id=ownerid)[0].getObject()
            self.campus = member.sede
            groups = getGroupsCommision(member.sede)

        cleanPermissionsCommissions(self)
        api.group.revoke_roles(groupname='imconsejeros', roles=['IMConsejero'], obj=self)
        api.group.revoke_roles(groupname='assistants_imconsejeros', roles=['Editor'], obj=self)

        api.group.grant_roles(groupname=groups['commissioners'], roles=['IMComisionado'], obj=self)
        api.group.grant_roles(groupname=groups['assistants'], roles=['IMComisionado', 'Editor'], obj=self)

    def returnToConsejo(self):
        if self.campus:
                groups = getGroupsCommision(self.campus)

        else:
            ownerid = self.getIdOwner()
            member = api.content.find(portal_type='FSDPerson', id=ownerid)[0].getObject()
            self.campus = member.sede
            groups = getGroupsCommision(member.sede)

        cleanPermissionsCommissions(self)
        api.group.grant_roles(groupname=groups['commissioners'], roles=['IMComisionado'], obj=self)
        api.group.grant_roles(groupname=groups['assistants'], roles=['IMComisionado'], obj=self)

    def sendMail(self, state='aprobada'):
        mt = getToolByName(self, 'portal_membership')
        member = mt.getMemberById(self.getIdOwner())
        mail_to = member.getProperty('email', None)
        mail_from = 'solicitudes@matem.unam.mx'
        subject = '[matem] Su solicitud ha sido ' + state
        msg = """
        Su solicitud de expositor (%s) para el coloquio del %s ha sido %s.


        Para más información ir a %s.\n

        ------------------------------------------------------------------
        Éste es un correo electrónico automático, por favor no lo responda
        """
        msg = msg.decode('utf-8') % (
            self.title,
            self.exposition_date.strftime('%d/%m/%Y'),
            state,
            self.absolute_url(),
        )

        getToolByName(self, 'MailHost').send(msg.encode('utf-8'), mail_to, mail_from, subject)

        return True

    def createControls(self):
        data = {}
        data['title'] = self.title
        data['relatedsolicitud'] = self.UID()
        data['classification'] = 'NA'
        data['campus'] = self.campus_owner()
        data['start'] = self.exposition_date
        data['end'] = self.end()

        if self.amount_travel_authorized > 0 and data['campus'] != 'Cuernavaca':
            data['amount'] = self.amount_travel_authorized
            with api.env.adopt_user(username='admin'):
                if not api.content.find(portal_type='viatical', relatedsolicitud=data['relatedsolicitud']):
                    createViaticalControl(data)
        if self.amount_transportation_authorized > 0 and data['campus'] != 'Cuernavaca':
            data['amount'] = self.amount_transportation_authorized
            typestransportations = self.transportation_type
            if 'groudtransportation' in typestransportations and 'airtransport' in typestransportations:
                with api.env.adopt_user(username='admin'):
                    if not api.content.find(portal_type='airticket', relatedsolicitud=data['relatedsolicitud']):
                        createAirticketControl(data)
                    if not api.content.find(portal_type='landticket', relatedsolicitud=data['relatedsolicitud']):
                        createLandticketControl(data, 'block')
            elif 'airtransport' in typestransportations:
                with api.env.adopt_user(username='admin'):
                    if not api.content.find(portal_type='airticket', relatedsolicitud=data['relatedsolicitud']):
                        createAirticketControl(data)
            elif 'groudtransportation' in typestransportations:
                with api.env.adopt_user(username='admin'):
                    if not api.content.find(portal_type='landticket', relatedsolicitud=data['relatedsolicitud']):
                        createLandticketControl(data)
        return True

    def end(self):
        return self.exposition_date + timedelta(days=1)

    def amount_used(self):
        return self.amount_travel_used + self.amount_transportation_used

    # TO DO: Methods that are necessary for uni admin view
    def getCantidadDeDias(self):
        return (self.end() - self.exposition_date).days

    def getFechaDesde(self):
        datetzinfo = DateTime(self.exposition_date.__str__()).asdatetime().replace(tzinfo=None)
        return DateTime(datetzinfo)

    def actaci(self):
        return self.minute

    def getFechaHasta(self):
        datetzinfo = DateTime(self.end().__str__()).asdatetime().replace(tzinfo=None)
        return DateTime(datetzinfo)

    def getCiudadPais(self):
        return 'N/A'

    def getPais(self):
        return 'COUNTRY'

    def getObjetoViaje(self):
        # return self.description_activity
        return 'DESCRIPTION'

    def getCantidad_consejo_viaticos(self):
        return self.amount_travel_authorized

    def getCantidad_consejo_pasaje(self):
        return self.amount_transportation_authorized
