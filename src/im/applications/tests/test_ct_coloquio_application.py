# -*- coding: utf-8 -*-
from im.applications.content.coloquio_application import IColoquioApplication  # NOQA E501
from im.applications.testing import IM_APPLICATIONS_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class ColoquioApplicationIntegrationTest(unittest.TestCase):

    layer = IM_APPLICATIONS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_ct_coloquio_application_schema(self):
        fti = queryUtility(IDexterityFTI, name='coloquio_application')
        schema = fti.lookupSchema()
        self.assertEqual(IColoquioApplication, schema)

    def test_ct_coloquio_application_fti(self):
        fti = queryUtility(IDexterityFTI, name='coloquio_application')
        self.assertTrue(fti)

    def test_ct_coloquio_application_factory(self):
        fti = queryUtility(IDexterityFTI, name='coloquio_application')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IColoquioApplication.providedBy(obj),
            u'IColoquioApplication not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_coloquio_application_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='coloquio_application',
            id='coloquio_application',
        )

        self.assertTrue(
            IColoquioApplication.providedBy(obj),
            u'IColoquioApplication not provided by {0}!'.format(
                obj.id,
            ),
        )

    def test_ct_coloquio_application_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='coloquio_application')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )
