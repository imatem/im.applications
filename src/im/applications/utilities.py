# -*- coding: utf-8 -*-
""" Module that provides functionality for applications manipulation"""

from plone import api


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
    for gcommissioners in allGroupsCommissions['commissioners']:
        roles = api.group.get_roles(groupname=gcommissioners, obj=obj, inherit=False)
        if roles:
            api.group.revoke_roles(groupname=gcommissioners, roles=['Reader'], obj=obj)

    for gassistantscommissioners in allGroupsCommissions['assistants']:
        roles = api.group.get_roles(groupname=gassistantscommissioners, obj=obj, inherit=False)
        if roles:
            api.group.revoke_roles(groupname=gassistantscommissioners, roles=['Reader', 'Editor'], obj=obj)
