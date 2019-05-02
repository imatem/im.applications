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

    minute = schema.TextLine(
        title=_(u'label_applications_minute', default=u'Minute Number'),
        description=_(u'help_applications_minute', default=u'Minute of Consejo Interno'),
        required=False,
    )

    typeactivity = schema.TextLine(
        title=_(u'label_applications_typeactivity', u'Type activity Activity'),
        required=True,
    )

    responsables = schema.Text(
        title=_(u'label_applications_responsables', u'Responsable(s) Name'),
        required=True,
    )

    amount = schema.Float(
        title=_(u'label_applications_amount', u'Approved Amount'),
        description=_(u'help_applications_amount', u'Amount when the solicitud was created'),
        required=False,
        min=1.0,
        # max=25000.0,
    )

    start = schema.Datetime(
        title=_(u'label_applications_start_date', default=u'Start date of the activity'),
        required=True,
    )

    end = schema.Datetime(
        title=_(u'label_applications_end_date', default=u'End date of the activity'),
        required=True,
    )

    place_activity = schema.Text(
        title=_(u'label_applications_place_activity', u'Place Activity'),
        required=True,
    )

    description_activity = schema.Text(
        title=_(u'label_applications_description_activity', u'Description Activity'),
        required=True,
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
        # return DateTime(self.start.__str__())
        return DateTime(self.start)

    def actaci(self):
        return self.minute

    def getFechaHasta(self):
        # return DateTime(self.end.__str__())
        return DateTime(self.end)

    def getCiudadPais(self):
        return self.place_activity

    def getPais(self):
        return 'COUNTRY'

    def getObjetoViaje(self):
        return self.description_activity

    def getCantidad_consejo_viaticos(self):
        return self.amount

