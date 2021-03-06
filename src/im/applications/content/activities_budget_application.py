# -*- coding: utf-8 -*-
from im.applications import _
# from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.dexterity.content import Item
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer
from zope.interface import Invalid
from zope.interface import invariant
from DateTime import DateTime
from Products.CMFCore.utils import getToolByName
from zope.i18n import translate


class IActivitiesBudgetApplication(model.Schema):
    """ Marker interface and Dexterity Python Schema for ActivitiesBudgetApplication
    """
    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('activities_budget_application.xml')

    # directives.widget(level=RadioFieldWidget)
    # level = schema.Choice(
    #     title=_(u'Sponsoring Level'),
    #     vocabulary=LevelVocabulary,
    #     required=True
    # )

    # text = RichText(
    #     title=_(u'Text'),
    #     required=False
    # )

    # url = schema.URI(
    #     title=_(u'Link'),
    #     required=False
    # )

    # fieldset('Images', fields=['logo', 'advertisement'])
    # logo = namedfile.NamedBlobImage(
    #     title=_(u'Logo'),
    #     required=False,
    # )

    # advertisement = namedfile.NamedBlobImage(
    #     title=_(u'Advertisement (Gold-sponsors and above)'),
    #     required=False,
    # )

    # directives.read_permission(notes='cmf.ManagePortal')
    # directives.write_permission(notes='cmf.ManagePortal')
    # notes = RichText(
    #     title=_(u'Secret Notes (only for site-admins)'),
    #     required=False
    # )


    title = schema.TextLine(
        title=_(u'label_applications_title', default=u'Activity Name'),
        required=True,
    )

    edition = schema.TextLine(
        title=_(u'label_applications_edition', default=u'Edition'),
        description=_(u'help_applications_edition', default=u'The edition of the activity, in case of academic activity. By example Thirty-third'),
        required=True,
    )

    minute = schema.TextLine(
        title=_(u'label_applications_minute', default=u'Minute Number'),
        description=_(u'help_applications_minute', default=u'Minute of Consejo Interno'),
        required=False,
    )

    internalc_date = schema.Date(
        title=_(u'label_applications_amount_internalc_date', default=u'Consejo Interno Date'),
        required=False,
    )

    # typeactivity = schema.TextLine(
    #     title=_(u'label_applications_typeactivity', u'Type activity Activity'),
    #     required=True,
    # )

    typeactivity = schema.Choice(
        title=_(u'label_applications_typeactivity', u'Type activity Activity'),
        required=True,
        vocabulary='im.applications.TypeActivityIM',
    )

    responsables = schema.Text(
        title=_(u'label_applications_responsables', u'Responsable(s) Name'),
        required=True,
    )

    requested_amount = schema.Float(
        title=_(u'label_applications_requested_amount', u'Requested Amount'),
        # description=_(u'help_applications_amount', u'Amount when the solicitud was created'),
        required=False,
        min=1.0,
        # max=25000.0,
    )

    amount = schema.Float(
        title=_(u'label_applications_amount', u'Approved Amount'),
        # description=_(u'help_applications_amount', u'Amount when the solicitud was created'),
        required=True,
        min=1.0,
        # max=25000.0,
    )

    start = schema.Date(
        title=_(u'label_applications_start_date', default=u'Start date of the activity'),
        required=True,
    )

    end = schema.Date(
        title=_(u'label_applications_end_date', default=u'End date of the activity'),
        required=True,
    )

    place_activity = schema.Text(
        title=_(u'label_applications_place_activity', u'Place Activity'),
        required=True,
    )

    description_activity = schema.Text(
        title=_(u'label_applications_description_activity', u'Description Activity'),
        required=False,
    )

    @invariant
    def validateDateFields(data):
        if data.end < data.start:
            message = 'Invalid Dates: the Star Date must be greater that End Date, please correct it.'
            raise Invalid(_('label_applications_error_datesbefore', default=message))


@implementer(IActivitiesBudgetApplication)
class ActivitiesBudgetApplication(Item):
    """
    """
    # TO DO: Methods that are necessary for uni admin view
    def getCantidadDeDias(self):

        return (self.end - self.start).days

    def getFechaDesde(self):
        datetzinfo = DateTime(self.start.__str__()).asdatetime().replace(tzinfo=None)
        return DateTime(datetzinfo)

    def actaci(self):
        return self.minute

    def getFechaHasta(self):
        datetzinfo = DateTime(self.end.__str__()).asdatetime().replace(tzinfo=None)
        return DateTime(datetzinfo)

    def getCiudadPais(self):
        return self.place_activity

    def getPais(self):
        return ''

    def getObjetoViaje(self):
        if self.description_activity:
            return self.title + '. Por considerar: ' + self.description_activity

        return self.title
        # return self.typeactivity + ': ' + self.title + '\n ' + self.description_activity
        # return self.description_activity

    def getCantidad_consejo_viaticos(self):
        return self.amount

    def getWFStateName(self):
        workflowTool = getToolByName(self, "portal_workflow")
        current_state = workflowTool.getInfoFor(self, 'review_state', None)
        statename = workflowTool.getTitleForStateOnType(current_state, self.portal_type)
        return translate(statename, domain='im.applications', target_language=self.REQUEST.LANGUAGE)

