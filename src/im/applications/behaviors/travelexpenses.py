# -*- coding: utf-8 -*-
from im.applications import _
# from plone import schema
from zope import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider


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

    amount_travel_specialc = schema.Float(
        title=_(u'label_applications_amount_travel_specialc', u'Approved Amount by Special Comision for Travel Expenses'),
        required=True,
        min=0.0,
    )

    amount_travel_internalc = schema.Float(
        title=_(u'label_applications_amount_travel_internalc', u'Approved Amount by Consejo Interno for Travel Expenses'),
        required=True,
        min=0.0,
    )


@implementer(ITravelexpenses)
@adapter(ITravelexpensesMarker)
class Travelexpenses(object):
    def __init__(self, context):
        self.context = context

    # @property
    # def project(self):
    #     if hasattr(self.context, 'project'):
    #         return self.context.project
    #     return None

    # @project.setter
    # def project(self, value):
    #     self.context.project = value
