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

    directives.read_permission(amount_transportation_specialc='matem.solicitudes.SolicitudComisionRevisaSolicitud')
    directives.write_permission(amount_transportation_specialc='matem.solicitudes.SolicitudComisionRevisaSolicitud')
    amount_transportation_specialc = schema.Float(
        title=_(u'label_applications_amount_transportation_specialc', u'Approved Amount by Special Comision for Transportation Expenses'),
        required=True,
        min=0.0,
    )

    directives.read_permission(amount_transportation_internalc='matem.solicitudes.SolicitudConsejoRevisaSolicitud')
    directives.write_permission(amount_transportation_internalc='matem.solicitudes.SolicitudConsejoRevisaSolicitud')
    amount_transportation_internalc = schema.Float(
        title=_(u'label_applications_amount_transportation_internalc', u'Approved Amount by Consejo Interno for Transportation Expenses'),
        required=True,
        min=0.0,
    )

    directives.read_permission(amount_transportation_authorized='matem.solicitudes.SolicitudConsejoCambiaSolicitud')
    directives.write_permission(amount_transportation_authorized='matem.solicitudes.SolicitudConsejoCambiaSolicitud')
    amount_transportation_authorized = schema.Float(
        title=_(u'label_applications_amount_transportation_authorized', u'Approved Amount for Transportation Expenses'),
        required=True,
        min=0.0,
    )


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
    def amount_transportation_specialc(self):
        if hasattr(self.context, 'amount_transportation_specialc'):
            return self.context.amount_transportation_specialc
        return None

    @amount_transportation_specialc.setter
    def amount_transportation_specialc(self, value):
        self.context.amount_transportation_specialc = value

    @property
    def amount_transportation_internalc(self):
        if hasattr(self.context, 'amount_transportation_internalc'):
            return self.context.amount_transportation_internalc
        return None

    @amount_transportation_internalc.setter
    def amount_transportation_internalc(self, value):
        self.context.amount_transportation_internalc = value

    @property
    def amount_transportation_authorized(self):
        if hasattr(self.context, 'amount_transportation_authorized'):
            return self.context.amount_transportation_authorized
        return None

    @amount_transportation_authorized.setter
    def amount_transportation_authorized(self, value):
        self.context.amount_transportation_authorized = value
