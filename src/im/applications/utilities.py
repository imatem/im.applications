# -*- coding: utf-8 -*-
""" Module that provides functionality for applications manipulation"""
from DateTime import DateTime
from plone import api
from zope.event import notify
from zope.lifecycleevent import ObjectModifiedEvent
import datetime
from Products.CMFCore.WorkflowCore import WorkflowException
from zope.i18n import translate


def allGroupsCommissions():
    return{
        'commissioners': ['cuer_commissioners', 'jur_commissioners', 'oax_commissioners', 'cu_commissioners'],
        'assistants': ['cuer_assistants_commissioners', 'jur_assistants_commissioners', 'oax_assistants_commissioners', 'cu_assistants_commissioners']
    }


def getGroupsCommision(campusOwner):
    if campusOwner == 'Cuernavaca':
        return {
            'commissioners': 'cuer_commissioners',
            'assistants': 'cuer_assistants_commissioners'
        }

    if campusOwner == 'Juriquilla':
        return {
            'commissioners': 'jur_commissioners',
            'assistants': 'jur_assistants_commissioners'
        }

    if campusOwner == 'Oaxaca':
        return {
            'commissioners': 'oax_commissioners',
            'assistants': 'oax_assistants_commissioners'
        }

    return {
        'commissioners': 'cu_commissioners',
        'assistants': 'cu_assistants_commissioners'
    }


def cleanPermissionsCommissions(obj):
    for gcommissioners in allGroupsCommissions()['commissioners']:
        roles = api.group.get_roles(groupname=gcommissioners, obj=obj, inherit=False)
        if roles:
            api.group.revoke_roles(groupname=gcommissioners, roles=['Reader'], obj=obj)

    for gassistantscommissioners in allGroupsCommissions()['assistants']:
        roles = api.group.get_roles(groupname=gassistantscommissioners, obj=obj, inherit=False)
        if roles:
            api.group.revoke_roles(groupname=gassistantscommissioners, roles=['Reader', 'Editor'], obj=obj)


def createViaticalControl(data):
        portal = api.portal.get()
        uniadmin_path = 'unidad/viaticos'
        uniadmin_folder = portal.unrestrictedTraverse(uniadmin_path)
        viaticalcontrol = api.content.create(
            type='viatical',
            title=data['title'],
            container=uniadmin_folder
        )
        viaticalcontrol.relatedsolicitud = data['relatedsolicitud']
        viaticalcontrol.classification = data['classification']
        viaticalcontrol.campus = data['campus']
        viaticalcontrol.amount = data['amount']
        viaticalcontrol.start = DateTime(data['start'].__str__()).asdatetime().replace(tzinfo=None)
        viaticalcontrol.end = DateTime(data['end'].__str__()).asdatetime().replace(tzinfo=None)
        today = datetime.date.today()
        if (data['start'] - today).days >= 20:
            viaticalcontrol.payment_type = 'payment'
        else:
            viaticalcontrol.payment_type = 'repayment'

        if (data['start'] - today).days >= 20:
            viaticalcontrol.timecontrol_type = 'timely'
        else:
            viaticalcontrol.timecontrol_type = 'untimely'
        notify(ObjectModifiedEvent(viaticalcontrol))


def createAirticketControl(data):
    portal = api.portal.get()
    uniadmin_path = 'unidad/transporte-aereo'
    uniadmin_folder = portal.unrestrictedTraverse(uniadmin_path)
    aircontrol = api.content.create(
        type='airticket',
        title=data['title'],
        container=uniadmin_folder
    )
    aircontrol.relatedsolicitud = data['relatedsolicitud']
    aircontrol.classification = data['classification']
    aircontrol.campus = data['campus']
    aircontrol.amount = data['amount']
    aircontrol.start = DateTime(data['start'].__str__()).asdatetime().replace(tzinfo=None)
    aircontrol.end = DateTime(data['end'].__str__()).asdatetime().replace(tzinfo=None)
    today = datetime.date.today()

    if (data['start'] - today).days >= 20:
        aircontrol.timecontrol_type = 'timely'
    else:
        aircontrol.timecontrol_type = 'untimely'
    notify(ObjectModifiedEvent(aircontrol))


def createLandticketControl(data, status='initial'):
    portal = api.portal.get()
    uniadmin_path = 'unidad/transporte-terrestre'
    uniadmin_folder = portal.unrestrictedTraverse(uniadmin_path)
    landcontrol = api.content.create(
        type='landticket',
        title=data['title'],
        container=uniadmin_folder
    )
    landcontrol.relatedsolicitud = data['relatedsolicitud']
    landcontrol.classification = data['classification']
    landcontrol.campus = data['campus']
    landcontrol.amount = data['amount']
    landcontrol.start = DateTime(data['start'].__str__()).asdatetime().replace(tzinfo=None)
    landcontrol.end = DateTime(data['end'].__str__()).asdatetime().replace(tzinfo=None)
    today = datetime.date.today()

    if (data['start'] - today).days >= 20:
        landcontrol.timecontrol_type = 'timely'
    else:
        landcontrol.timecontrol_type = 'untimely'

    if status == 'block':
        # change status of landcontrol
        wft = api.portal.get_tool('portal_workflow')
        control = api.content.get(UID=landcontrol.UID())
        try:
            wft.doActionFor(control, 'block')
        except WorkflowException:
            # a workflow exception is risen if the state transition is not available
            # (the sampleProperty content is in a workflow state which
            # does not have a "submit" transition)
            pass

    notify(ObjectModifiedEvent(landcontrol))


# {'owner_comments': '',
# 'owner_name': 'Antol\xc3\xadn Camarena, Omar ',
# 'workflow_state': 'revisioncomision',
# 'quantity_of_days': 3,
# 'creation_date': '22/07/2019',
# 'sede': 'C.U.',
# 'cargo_presupuesto': 'Asignaci\xc3\xb3n anual',
# 'country_code': ('MX',),
# 'parentid': '2019',
# 'transportation_means': (),
# 'parent_folder': <SolicitudFolder at /infomatem/servicios/servicios-internos/solicitudes/2019>,
# 'institutional_budget': {'registration_expenses': 0.0, 'food_expenses': 0.0, 'transport_expenses': 0.0},
# 'id': 'solicitud.2019-07-22.3870045398',
# 'workflow_state_name': 'Solicitud en revision por Comision Especial',
# 'city': 'M\xc3\xa9rida',
# 'from': '14/08/2019',
# 'revision_ce_date': '',
# 'transportation_quantity': 0.0,
# 'url': 'http://localhost:8080/infomatem/servicios/servicios-internos/solicitudes/2019/solicitud.2019-07-22.3870045398',
# 'country': 'Mexico',
# 'total_quantity': 0.0,
# 'special_fields': {'readable_meta_type': 'Solicitud de Licencia', 'inscription_quantity': 0.0, 'type': 'Licencia', 'work_title': ''},
# 'annual_budget': {'registration_expenses': 0.0, 'food_expenses': 0.0, 'transport_expenses': 0.0},
# 'institution': 'UADY y CIMAT M\xc3\xa9rida',
# 'total_recommended_quantity': 0.0,
# 'to': '16/08/2019',
# 'total_consejo_quantity': 0.0,
# 'meta_type': 'Solicitud',
# 'research_areas': ('55-xx',),
# 'total_approved_quantity': 0.0,
# 'objective': 'Voy a (1) ser sinodal en el ex\xc3\xa1men de maestr\xc3\xada de \xc3\x81ngel Jim\xc3\xa9nez Cruz, un alumno de la UADY, (2) dar\xc3\xa9 el coloquio conjunto de la UADY y el CIMAT M\xc3\xa9rida, (3) dar\xc3\xa9 una pl\xc3\xa1tica en el seminario de topolog\xc3\xada que organiza Jos\xc3\xa9 Mar\xc3\xada Cantarero del CIMAT M\xc3\xa9rida. ',
# 'revision_ci_date': '',
# 'acta_ci': '',
# 'travel_expense_quantity': 0.0,
# 'owner_id': 'omar'}


def getIMAppInformation(brain):
    data = {}
    obj = brain.getObject()
    # this informations is for merge imapplications for matem.solicitud, this is in queries
    data['meta_type'] = obj.portal_type  # or meta_type
    data['id'] = obj.getId()
    data['sede'] = obj.campus_owner()
    data['owner_name'] = obj.nombre_owner().encode('utf-8')
    data['owner_id'] = obj.getIdOwner()
    data['institution'] = obj.institution
    data['city'] = obj.getCiudadPais()
    data['country'] = obj.getPais()
    data['country_code'] = ('MX',)
    data['from'] = obj.getFechaDesde().strftime('%d/%m/%Y')
    data['to'] = obj.getFechaHasta().strftime('%d/%m/%Y')
    data['quantity_of_days'] = obj.getCantidadDeDias()
    # data['research_areas'] = ()
    data['objective'] = obj.getObjetoViaje()
    data['owner_comments'] = obj.comments
    data['transportation_means'] = tuple(obj.getTipo_pasaje())
    data['travel_expense_quantity'] = obj.amount_travel
    data['transportation_quantity'] = obj.amount_transportation
    data['total_quantity'] = obj.getTotal()
    data['total_recommended_quantity'] = obj.getCantidadRecomendadaTotal()
    data['total_consejo_quantity'] = obj.getCantidadConsejoTotal()
    data['total_approved_quantity'] = obj.getCantidadAutorizadaTotal()
    data['creation_date'] = obj.creation_date.strftime('%d/%m/%Y')
    data['revision_ci_date'] = obj.internalc_date and obj.internalc_date.strftime('%d/%m/%Y') or ''
    data['revision_ce_date'] = obj.specialc_date and obj.specialc_date.strftime('%d/%m/%Y') or ''
    data['acta_ci'] = obj.actaci()
    data['workflow_state'] = brain.review_state
    # data['workflow_state_name'] = obj.getWFStateName()
    data['workflow_state_name'] = translate(obj.getWFStateName(), domain='im.applications', target_language=obj.REQUEST.LANGUAGE)
    data['url'] = obj.absolute_url()
    readable_meta_type = translate(obj.getTypeInfo().title, domain='im.applications', target_language=obj.REQUEST.LANGUAGE) + ' (' + obj.title + ')'
    data['special_fields'] = {'readable_meta_type': readable_meta_type, }
    data['cargo_presupuesto'] = obj.getCargo_presupuesto()

    data['parent_folder'] = obj.aq_parent
    data['annual_budget'] = {'registration_expenses': 0.0, 'food_expenses': 0.0, 'transport_expenses': 0.0}
    data['institutional_budget'] = {'registration_expenses': 0.0, 'food_expenses': 0.0, 'transport_expenses': 0.0}
    data['parentid'] = obj.aq_parent.getId()
    data['uid'] = obj.UID()

    return data

def getIMApplicationsByWState(wstate):
    imapplications = api.content.find(portal_type=['coloquio_application'], review_state=wstate)

    datas = []

    for imapp in imapplications:
        data = getIMAppInformation(imapp)
        datas.append(data)

    return datas


def getIMApplicationsByWStateAndUser(wstate, userid):
    imapplications = api.content.find(portal_type=['coloquio_application'], review_state=wstate, Creator=userid)

    datas = []

    for imapp in imapplications:
        data = getIMAppInformation(imapp)
        datas.append(data)

    return datas

