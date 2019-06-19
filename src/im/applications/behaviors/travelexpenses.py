# -*- coding: utf-8 -*-
from im.applications import _
# from plone import schema
from zope import schema
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider
from zope.interface import alsoProvides


class ITravelexpensesMarker(Interface):
    pass

@provider(IFormFieldProvider)
class ITravelexpenses(model.Schema):
    """
    """

    amount_travel = schema.Float(
        title=_(u'label_applications_amount_travel', u'Amount for Travel Expenses'),
        required=True,
        min=0.0,
    )

    directives.read_permission(amount_travel_recommended='im.applications.ViewComision')
    directives.write_permission(amount_travel_recommended='im.applications.EditComision')
    amount_travel_recommended = schema.Float(
        title=_(u'label_applications_amount_travel_recommended', u'Approved Amount by Special Comision for Travel Expenses'),
        required=True,
        min=0.0,
    )

    directives.read_permission(amount_travel_authorized='im.applications.ViewConsejo')
    directives.write_permission(amount_travel_authorized='im.applications.EditConsejo')
    amount_travel_authorized = schema.Float(
        title=_(u'label_applications_amount_travel_authorized', u'Approved Amount by Consejo Interno for Travel Expenses'),
        required=True,
        min=0.0,
    )

    directives.read_permission(amount_travel_used='im.applications.ViewConsejo')
    directives.write_permission(amount_travel_used='im.applications.EditConsejo')
    amount_travel_used = schema.Float(
        title=_(u'label_applications_amount_travel_used', u'Used Amount for Travel Expenses'),
        required=True,
        min=0.0,
    )



@implementer(ITravelexpenses)
@adapter(ITravelexpensesMarker)
class Travelexpenses(object):
    def __init__(self, context):
        self.context = context

    @property
    def amount_travel(self):
        if hasattr(self.context, 'amount_travel'):
            return self.context.amount_travel
        return None

    @amount_travel.setter
    def amount_travel(self, value):
        self.context.amount_travel = value

    @property
    def amount_travel_recommended(self):
        if hasattr(self.context, 'amount_travel_recommended'):
            return self.context.amount_travel_recommended
        return None

    @amount_travel_recommended.setter
    def amount_travel_recommended(self, value):
        self.context.amount_travel_recommended = value


    @property
    def amount_travel_authorized(self):
        if hasattr(self.context, 'amount_travel_authorized'):
            return self.context.amount_travel_authorized
        return None

    @amount_travel_authorized.setter
    def amount_travel_authorized(self, value):
        self.context.amount_travel_authorized = value


    @property
    def amount_travel_used(self):
        if hasattr(self.context, 'amount_travel_used'):
            return self.context.amount_travel_used
        return None

    @amount_travel_used.setter
    def amount_travel_used(self, value):
        self.context.amount_travel_used = value


    # @property
    # def project(self):
    #     if hasattr(self.context, 'project'):
    #         return self.context.project
    #     return None

    # @project.setter
    # def project(self, value):
    #     self.context.project = value
