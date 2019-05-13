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


@implementer(IColoquioApplication)
class ColoquioApplication(Item):
    """
    """
