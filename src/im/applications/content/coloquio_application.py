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

    directives.read_permission(specialc_date='matem.solicitudes.SolicitudComisionRevisaSolicitud')
    directives.write_permission(specialc_date='matem.solicitudes.SolicitudComisionRevisaSolicitud')
    specialc_date = schema.Date(
        title=_(u'label_applications_amount_specialc_date', default=u'Special Comision Date'),
        required=True,
    )

    directives.read_permission(minute='matem.solicitudes.SolicitudComisionRevisaSolicitud')
    directives.write_permission(minute='matem.solicitudes.SolicitudComisionRevisaSolicitud')
    minute = schema.TextLine(
        title=_(u'label_applications_minute', default=u'Minute Number'),
        description=_(u'help_applications_minute', default=u'Minute of Consejo Interno'),
        required=False,
    )

    directives.read_permission(internalc_date='matem.solicitudes.SolicitudConsejoRevisaSolicitud')
    directives.write_permission(internalc_date='matem.solicitudes.SolicitudConsejoRevisaSolicitud')
    internalc_date = schema.Date(
        title=_(u'label_applications_amount_internalc_date', default=u'Consejo Interno Date'),
        required=True,
    )


@implementer(IColoquioApplication)
class ColoquioApplication(Item):
    """
    """

    def pasarValorComisionado(self):
        import pdb; pdb.set_trace()
        # pasaje = self.getCantidadPasaje()
        # viaticos = self.getCantidadViaticos()
        # inscripcion = self.getCantidadInscripcion()

        # self.setCantidad_recomendada_pasaje(pasaje)
        # self.setCantidad_recomendada_viaticos(viaticos)
        # self.setCantidad_recomendada_inscripcion(inscripcion)
        return True
