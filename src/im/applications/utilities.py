# -*- coding: utf-8 -*-
""" Module that provides functionality for applications manipulation"""
from DateTime import DateTime
from plone import api
from zope.event import notify
from zope.lifecycleevent import ObjectModifiedEvent
import datetime


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

