# -*- coding: utf-8 -*-
from im.applications.behaviors.transportationexpenses import ITransportationexpensesMarker
from im.applications.testing import IM_APPLICATIONS_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class TransportationexpensesIntegrationTest(unittest.TestCase):

    layer = IM_APPLICATIONS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_transportationexpenses(self):
        behavior = getUtility(IBehavior, 'im.applications.transportationexpenses')
        self.assertEqual(
            behavior.marker,
            ITransportationexpensesMarker,
        )
