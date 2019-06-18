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

    directives.read_permission(amount_transportation_recommended='matem.solicitudes.SolicitudComisionRevisaSolicitud')
    directives.write_permission(amount_transportation_recommended='matem.solicitudes.SolicitudComisionRevisaSolicitud')
    amount_transportation_recommended = schema.Float(
        title=_(u'label_applications_amount_transportation_recommended', u'Approved Amount by Special Comision for Transportation Expenses'),
        required=True,
        min=0.0,
    )

    directives.read_permission(comments_recommended='matem.solicitudes.SolicitudComisionRevisaSolicitud')
    directives.write_permission(comments_recommended='matem.solicitudes.SolicitudComisionRevisaSolicitud')
    comments_recommended = schema.Text(
        title=_(u'label_applications_comments_recommended', u'Special Comision Comments'),
        required=False,
    )

    directives.read_permission(amount_transportation_authorized='matem.solicitudes.SolicitudConsejoRevisaSolicitud')
    directives.write_permission(amount_transportation_authorized='matem.solicitudes.SolicitudConsejoRevisaSolicitud')
    amount_transportation_authorized = schema.Float(
        title=_(u'label_applications_amount_transportation_authorized', u'Approved Amount by Consejo Interno for Transportation Expenses'),
        required=True,
        min=0.0,
    )

    directives.read_permission(comments_authorized='matem.solicitudes.SolicitudConsejoRevisaSolicitud')
    directives.write_permission(comments_authorized='matem.solicitudes.SolicitudConsejoRevisaSolicitud')
    comments_authorized = schema.Text(
        title=_(u'label_applications_comments_authorized', u'Consejo Interno Comments'),
        required=False,
    )

    directives.read_permission(amount_transportation_used='matem.solicitudes.SolicitudConsejoCambiaSolicitud')
    directives.write_permission(amount_transportation_used='matem.solicitudes.SolicitudConsejoCambiaSolicitud')
    amount_transportation_used = schema.Float(
        title=_(u'label_applications_amount_transportation_used', u'Approved Amount for Transportation Expenses'),
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
