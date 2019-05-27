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

    directives.read_permission(amount_registration_specialc='matem.solicitudes.SolicitudComisionRevisaSolicitud')
    directives.write_permission(amount_registration_specialc='matem.solicitudes.SolicitudComisionRevisaSolicitud')
    amount_registration_specialc = schema.Float(
        title=_(u'label_applications_amount_registration_specialc', u'Approved Amount by Special Comision for Registration Fees'),
        required=True,
        min=0.0,
    )

    directives.read_permission(amount_registration_internalc='matem.solicitudes.SolicitudConsejoRevisaSolicitud')
    directives.write_permission(amount_registration_internalc='matem.solicitudes.SolicitudConsejoRevisaSolicitud')
    amount_registration_internalc = schema.Float(
        title=_(u'label_applications_amount_registration_internalc', u'Approved Amount by Consejo Interno for Registration Fees'),
        required=True,
        min=0.0,
    )


@implementer(IRegistrationfees)
@adapter(IRegistrationfeesMarker)
class Registrationfees(object):
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
