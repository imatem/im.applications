# -*- coding: utf-8 -*-
from im.applications import _
# from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Item
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer

# from plone.directives import dexterity


# from im.applications import _


class IColoquioApplication(model.Schema):
    """ Marker interface and Dexterity Python Schema for ColoquioApplication
    """

    title = schema.TextLine(
        title=_(u'label_applications_coloquio_title', default=u'Speaker Name'),
        required=True,
    )

    institution = schema.TextLine(
        title=_(u'label_applications_coloquio_institution', default=u'Speaker Institution'),
        required=True,
    )

    exposition_date = schema.Date(
        title=_(u'label_applications_coloquio_exposition_date', default=u'Exposition Date'),
        required=True,
    )

    directives.read_permission(specialc_date='Solicitud: Comision Revisa Solicitud')
    directives.write_permission(specialc_date='cmf.ManagePortal')
    specialc_date = schema.Date(
        title=_(u'label_applications_amount_specialc_date', default=u'Special Comision Date'),
        required=True,
    )

    directives.read_permission(minute='Solicitud: Consejo Revisa Solicitud')
    directives.write_permission(minute='cmf.ManagePortal')
    minute = schema.TextLine(
        title=_(u'label_applications_minute', default=u'Minute Number'),
        description=_(u'help_applications_minute', default=u'Minute of Consejo Interno'),
        required=False,
    )

    directives.read_permission(internalc_date='Solicitud: Consejo Revisa Solicitud')
    directives.write_permission(internalc_date='Solicitud: Consejo Revisa Solicitud')
    internalc_date = schema.Date(
        title=_(u'label_applications_amount_internalc_date', default=u'Consejo Interno Date'),
        required=True,
    )


@implementer(IColoquioApplication)
class ColoquioApplication(Item):
    """
    """
