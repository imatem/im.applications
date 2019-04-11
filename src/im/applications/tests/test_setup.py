# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from im.applications.testing import IM_APPLICATIONS_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest

try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that im.applications is properly installed."""

    layer = IM_APPLICATIONS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if im.applications is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'im.applications'))

    def test_browserlayer(self):
        """Test that IImApplicationsLayer is registered."""
        from im.applications.interfaces import (
            IImApplicationsLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IImApplicationsLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = IM_APPLICATIONS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['im.applications'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if im.applications is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'im.applications'))

    def test_browserlayer_removed(self):
        """Test that IImApplicationsLayer is removed."""
        from im.applications.interfaces import \
            IImApplicationsLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IImApplicationsLayer,
            utils.registered_layers())
