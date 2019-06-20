# -*- coding: utf-8 -*-
from im.applications import _
# from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Item
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer
from plone import api
from Products.CMFCore.utils import getToolByName

# from plone.directives import dexterity


# from im.applications import _


class IColoquioApplication(model.Schema):
    """ Marker interface and Dexterity Python Schema for ColoquioApplication
    """

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


    # ########################################################################

    def pasarValorComisionado(self):
        with api.env.adopt_user(username='admin'):
            self.amount_travel_recommended = self.amount_travel
            self.amount_transportation_recommended = self.amount_transportation

        return True

    def pasarValorConsejero(self):
        with api.env.adopt_user(username='admin'):
            self.amount_travel_authorized = self.amount_travel_recommended
            self.amount_transportation_authorized = self.amount_transportation_recommended

        return True

    def pasarValorAutorizado(self):
        with api.env.adopt_user(username='admin'):
            self.amount_travel_used = self.amount_travel_authorized
            self.amount_transportation_used = self.amount_transportation_authorized
        return True

    def actualizarInvestigador(self):
        # folder = self.aq_parent

        # solicitante = self.getIdOwner()

        # folder.sumarACantidadAutorizada(None, self.getCantidadAutorizadaTotal(), 0, solicitante,
        #                                 self.getCargo_presupuesto())
        return True

    def desactualizarInvestigador(self):
        # folder = self.aq_parent

        # solicitante = self.getIdOwner()

        # folder.restarACantidadAutorizada(None, self.getCantidadAutorizadaTotal(), 0, solicitante)
        return True

    def getIdOwner(self):
        return self.getOwner().getId()

    def sendMail(self, state='aprobada'):
        mt = getToolByName(self, 'portal_membership')
        member = mt.getMemberById(self.getIdOwner())
        mail_to = member.getProperty('email', None)
        mail_from = 'solicitudes@matem.unam.mx'
        subject = '[matem] Su solicitud ha sido ' + state
        msg = """
        Su solicitud de expositor (%s) para el coloquio del %s ha sido %s.


        Para más información vaya a %s.

        ------------------------------------------------------------------
        Éste es un correo electrónico automático, por favor no lo responda
        """
        msg = msg.decode('utf-8') % (
            self.title,
            self.exposition_date.strftime('%d/%m/%Y'),
            state,
            self.absolute_url(),
        )
        getToolByName(self, 'MailHost').send(msg, mail_to, mail_from, subject)

        return True

