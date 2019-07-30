# -*- coding: utf-8 -*-
from im.applications.content.campus_application import ICampusApplication  # NOQA E501
from im.applications.testing import IM_APPLICATIONS_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class CampusApplicationIntegrationTest(unittest.TestCase):

    layer = IM_APPLICATIONS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_ct_campus_application_schema(self):
        fti = queryUtility(IDexterityFTI, name='campus_application')
        schema = fti.lookupSchema()
        self.assertEqual(ICampusApplication, schema)

    def test_ct_campus_application_fti(self):
        fti = queryUtility(IDexterityFTI, name='campus_application')
        self.assertTrue(fti)

    def test_ct_campus_application_factory(self):
        fti = queryUtility(IDexterityFTI, name='campus_application')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ICampusApplication.providedBy(obj),
            u'ICampusApplication not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_campus_application_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='campus_application',
            id='campus_application',
        )

        self.assertTrue(
            ICampusApplication.providedBy(obj),
            u'ICampusApplication not provided by {0}!'.format(
                obj.id,
            ),
        )

    def test_ct_campus_application_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='campus_application')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )
