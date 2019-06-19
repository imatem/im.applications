# -*- coding: utf-8 -*-
from im.applications import _
# from plone import schema
from plone.autoform import directives
from zope import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider


class IRegistrationfeesMarker(Interface):
    pass

@provider(IFormFieldProvider)
class IRegistrationfees(model.Schema):
    """
    """

    amount_registration = schema.Float(
        title=_(u'label_applications_amount_registration', u'Amount for Registration Fees'),
        required=True,
        min=0.0,
    )

    directives.read_permission(amount_registration_recommended='im.applications.ViewComision')
    directives.write_permission(amount_registration_recommended='im.applications.EditComision')
    amount_registration_recommended = schema.Float(
        title=_(u'label_applications_amount_registration_recommended', u'Approved Amount by Special Comision for Registration Fees'),
        required=True,
        min=0.0,
    )

    directives.read_permission(amount_registration_authorized='im.applications.ViewConsejo')
    directives.write_permission(amount_registration_authorized='im.applications.EditConsejo')
    amount_registration_authorized = schema.Float(
        title=_(u'label_applications_amount_registration_authorized', u'Approved Amount by Consejo Interno for Registration Fees'),
        required=True,
        min=0.0,
    )

    directives.read_permission(amount_registration_used='im.applications.ViewConsejo')
    directives.write_permission(amount_registration_used='im.applications.EditConsejo')
    amount_registration_used = schema.Float(
        title=_(u'label_applications_amount_registration_used', u'Used Amount for Registration Fees'),
        required=True,
        min=0.0,
    )


@implementer(IRegistrationfees)
@adapter(IRegistrationfeesMarker)
class Registrationfees(object):
    def __init__(self, context):
        self.context = context


    @property
    def amount_registration(self):
        if hasattr(self.context, 'amount_registration'):
            return self.context.amount_registration
        return None

    @amount_registration.setter
    def amount_registration(self, value):
        self.context.amount_registration = value

    @property
    def amount_registration_recommended(self):
        if hasattr(self.context, 'amount_registration_recommended'):
            return self.context.amount_registration_recommended
        return None

    @amount_registration_recommended.setter
    def amount_registration_recommended(self, value):
        self.context.amount_registration_recommended = value

    @property
    def amount_registration_authorized(self):
        if hasattr(self.context, 'amount_registration_authorized'):
            return self.context.amount_registration_authorized
        return None

    @amount_registration_authorized.setter
    def amount_registration_authorized(self, value):
        self.context.amount_registration_authorized = value

    @property
    def amount_registration_used(self):
        if hasattr(self.context, 'amount_registration_used'):
            return self.context.amount_registration_used
        return None

    @amount_registration_used.setter
    def amount_registration_used(self, value):
        self.context.amount_registration_used = value

