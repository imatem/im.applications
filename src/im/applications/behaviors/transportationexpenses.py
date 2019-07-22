# -*- coding: utf-8 -*-
from im.applications import _
# from plone import schema
from zope import schema
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope.component import adapter
from zope.interface import implementer
from zope.interface import Interface
from zope.interface import Invalid
from zope.interface import invariant
from zope.interface import provider
from z3c.form.browser.checkbox import CheckBoxFieldWidget


class ITransportationexpensesMarker(Interface):
    pass


@provider(IFormFieldProvider)
class ITransportationexpenses(model.Schema):
    """
    """

    amount_transportation = schema.Float(
        title=_(u'label_applications_amount_transportation', u'Amount for Transportation Expenses'),
        required=True,
        min=0.0,
    )

    directives.widget(transportation_type=CheckBoxFieldWidget)
    transportation_type = schema.Set(
        title=_(u'label_applications_transportation_type', default=u'Type Transportation'),
        value_type=schema.Choice(
            vocabulary='im.applications.TransportationType',
        ),
        required=False,
    )

    directives.read_permission(amount_transportation_recommended='im.applications.ViewComision')
    directives.write_permission(amount_transportation_recommended='im.applications.EditComision')
    amount_transportation_recommended = schema.Float(
        title=_(u'label_applications_amount_transportation_recommended', u'Approved Amount by Special Comision for Transportation Expenses'),
        required=True,
        min=0.0,
    )

    directives.read_permission(amount_transportation_authorized='im.applications.ViewCantidadAutorizada')
    directives.write_permission(amount_transportation_authorized='im.applications.EditConsejo')
    amount_transportation_authorized = schema.Float(
        title=_(u'label_applications_amount_transportation_authorized', u'Approved Amount by Consejo Interno for Transportation Expenses'),
        required=True,
        min=0.0,
    )

    directives.read_permission(amount_transportation_used='im.applications.ViewCantidadUtilizada')
    directives.write_permission(amount_transportation_used='im.applications.EditCantidadUtilizada')
    amount_transportation_used = schema.Float(
        title=_(u'label_applications_amount_transportation_used', u'Used Amount for Transportation Expenses'),
        required=True,
        min=0.0,
    )

    @invariant
    def validateFields(data):
        if data.amount_transportation > 0 and data.transportation_type == set([]):
            message = 'Invalid Transportation Type: You must select at least one transportation, please correct it.'
            raise Invalid(_('label_im_applications_error_transportation', default=message))
        elif data.amount_transportation == 0:
            if data.transportation_type.__contains__('groudtransportation') or data.transportation_type.__contains__('airtransport'):
                message = 'Invalid Transportation Type: You amount transportation is zero the transportation type must be empty, please correct it.'
                raise Invalid(_('label_im_applications_error_transportation2', default=message))


@implementer(ITransportationexpenses)
@adapter(ITransportationexpensesMarker)
class Transportationexpenses(object):
    def __init__(self, context):
        self.context = context

    @property
    def amount_transportation(self):
        if hasattr(self.context, 'amount_transportation'):
            return self.context.amount_transportation
        return None

    @amount_transportation.setter
    def amount_transportation(self, value):
        self.context.amount_transportation = value

    @property
    def transportation_type(self):
        if hasattr(self.context, 'transportation_type'):
            return self.context.transportation_type
        return None

    @transportation_type.setter
    def transportation_type(self, value):
        self.context.transportation_type = value

    @property
    def amount_transportation_recommended(self):
        if hasattr(self.context, 'amount_transportation_recommended'):
            return self.context.amount_transportation_recommended
        return None

    @amount_transportation_recommended.setter
    def amount_transportation_recommended(self, value):
        self.context.amount_transportation_recommended = value

    @property
    def amount_transportation_authorized(self):
        if hasattr(self.context, 'amount_transportation_authorized'):
            return self.context.amount_transportation_authorized
        return None

    @amount_transportation_authorized.setter
    def amount_transportation_authorized(self, value):
        self.context.amount_transportation_authorized = value

    @property
    def amount_transportation_used(self):
        if hasattr(self.context, 'amount_transportation_used'):
            return self.context.amount_transportation_used
        return None

    @amount_transportation_used.setter
    def amount_transportation_used(self, value):
        self.context.amount_transportation_used = value
