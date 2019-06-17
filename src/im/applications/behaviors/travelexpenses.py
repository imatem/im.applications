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

    directives.read_permission(amount_travel_specialc='matem.solicitudes.SolicitudComisionRevisaSolicitud')
    directives.write_permission(amount_travel_specialc='matem.solicitudes.SolicitudComisionRevisaSolicitud')
    amount_travel_specialc = schema.Float(
        title=_(u'label_applications_amount_travel_specialc', u'Approved Amount by Special Comision for Travel Expenses'),
        required=True,
        min=0.0,
    )

    directives.read_permission(amount_travel_internalc='matem.solicitudes.SolicitudConsejoRevisaSolicitud')
    directives.write_permission(amount_travel_internalc='matem.solicitudes.SolicitudConsejoRevisaSolicitud')
    amount_travel_internalc = schema.Float(
        title=_(u'label_applications_amount_travel_internalc', u'Approved Amount by Consejo Interno for Travel Expenses'),
        required=True,
        min=0.0,
    )

    directives.read_permission(amount_travel_authorized='matem.solicitudes.SolicitudConsejoCambiaSolicitud')
    directives.write_permission(amount_travel_authorized='matem.solicitudes.SolicitudConsejoCambiaSolicitud')
    amount_travel_authorized = schema.Float(
        title=_(u'label_applications_amount_travel_authorized', u'Approved Amount for Travel Expenses'),
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
    def amount_travel_specialc(self):
        if hasattr(self.context, 'amount_travel_specialc'):
            return self.context.amount_travel_specialc
        return None

    @amount_travel_specialc.setter
    def amount_travel_specialc(self, value):
        self.context.amount_travel_specialc = value


    @property
    def amount_travel_internalc(self):
        if hasattr(self.context, 'amount_travel_internalc'):
            return self.context.amount_travel_internalc
        return None

    @amount_travel_internalc.setter
    def amount_travel_internalc(self, value):
        self.context.amount_travel_internalc = value


    @property
    def amount_travel_authorized(self):
        if hasattr(self.context, 'amount_travel_authorized'):
            return self.context.amount_travel_authorized
        return None

    @amount_travel_authorized.setter
    def amount_travel_authorized(self, value):
        self.context.amount_travel_authorized = value


    # @property
    # def project(self):
    #     if hasattr(self.context, 'project'):
    #         return self.context.project
    #     return None

    # @project.setter
    # def project(self, value):
    #     self.context.project = value
