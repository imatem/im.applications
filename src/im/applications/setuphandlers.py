# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer
from plone import api
from im.applications.utilities import allGroupsCommissions


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            'im.applications:uninstall',
        ]


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.

    actual_groups = [gp.id for gp in api.group.get_groups()]

    # We will create groups for permissions
    if 'imconsejeros' not in actual_groups:
        api.group.create(groupname='imconsejeros')
        group_tool = api.portal.get_tool(name='portal_groups')
        group_tool.editGroup(
            'imconsejeros',
            title='IM Consejeros',
            description='Group for Consejo Interno Members',
        )

    if 'assistants_imconsejeros' not in actual_groups:
        api.group.create(groupname='assistants_imconsejeros')
        group_tool = api.portal.get_tool(name='portal_groups')
        group_tool.editGroup(
            'assistants_imconsejeros',
            title='Assistants IM Consejeros',
            description='Group for Assistants of Consejo Interno Members',
        )

    if 'cu_commissioners' not in actual_groups:
        api.group.create(groupname='cu_commissioners')
        group_tool = api.portal.get_tool(name='portal_groups')
        group_tool.editGroup(
            'cu_commissioners',
            # roles=['Reader'],
            title='C.U. Commissioners',
            description='Group for the Special Commission in C.U.',
        )

    if 'cu_assistants_commissioners' not in actual_groups:
        api.group.create(groupname='cu_assistants_commissioners')
        group_tool = api.portal.get_tool(name='portal_groups')
        group_tool.editGroup(
            'cu_assistants_commissioners',
            # roles=['Reader'],
            title='C.U. Assistants Commissioners',
            description='Group for the Assistants of Special Commission in C.U.',
        )

    if 'cuer_commissioners' not in actual_groups:
        api.group.create(groupname='cuer_commissioners')
        group_tool = api.portal.get_tool(name='portal_groups')
        group_tool.editGroup(
            'cuer_commissioners',
            title='Cuernacava Commissioners',
            description='Group for the Special Commission in Cuernacava',
        )

    if 'cuer_assistants_commissioners' not in actual_groups:
        api.group.create(groupname='cuer_assistants_commissioners')
        group_tool = api.portal.get_tool(name='portal_groups')
        group_tool.editGroup(
            'cuer_assistants_commissioners',
            title='Cuernacava Assistants Commissioners',
            description='Group for the Assistants of Special Commission in Cuernacava',
        )

    if 'jur_commissioners' not in actual_groups:
        api.group.create(groupname='jur_commissioners')
        group_tool = api.portal.get_tool(name='portal_groups')
        group_tool.editGroup(
            'jur_commissioners',
            title='Juriquilla Commissioners',
            description='Group for the Special Commission in Juriquilla',
        )

    if 'jur_assistants_commissioners' not in actual_groups:
        api.group.create(groupname='jur_assistants_commissioners')
        group_tool = api.portal.get_tool(name='portal_groups')
        group_tool.editGroup(
            'jur_assistants_commissioners',
            title='Juriquilla Assistants Commissioners',
            description='Group for the Assistants of Special Commission in Juriquilla',
        )

    if 'oax_commissioners' not in actual_groups:
        api.group.create(groupname='oax_commissioners')
        group_tool = api.portal.get_tool(name='portal_groups')
        group_tool.editGroup(
            'oax_commissioners',
            title='Oaxaca Commissioners',
            description='Group for the Special Commission in Oaxaca',
        )

    if 'oax_assistants_commissioners' not in actual_groups:
        api.group.create(groupname='oax_assistants_commissioners')
        group_tool = api.portal.get_tool(name='portal_groups')
        group_tool.editGroup(
            'oax_assistants_commissioners',
            title='Oaxaca Assistants Commissioners',
            description='Group for the Asistants of Special Commission in Oaxaca',
        )


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
    # actual_groups = [gp.id for gp in api.group.get_groups()]

    # for gcommissioners in allGroupsCommissions['commissioners']:
    #     if gcommissioners in actual_groups:
    #         api.group.delete(groupname=gcommissioners)

    # for gassistantscommissioners in allGroupsCommissions['assistants']:
    #     if gassistantscommissioners in actual_groups:
    #         api.group.delete(groupname=gassistantscommissioners)












