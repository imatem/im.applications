# -*- coding: utf-8 -*-
from im.applications.content.moneysack import IMoneysack  # NOQA E501
from im.applications.testing import IM_APPLICATIONS_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class MoneysackIntegrationTest(unittest.TestCase):

    layer = IM_APPLICATIONS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_ct_moneysack_schema(self):
        fti = queryUtility(IDexterityFTI, name='moneysack')
        schema = fti.lookupSchema()
        self.assertEqual(IMoneysack, schema)

    def test_ct_moneysack_fti(self):
        fti = queryUtility(IDexterityFTI, name='moneysack')
        self.assertTrue(fti)

    def test_ct_moneysack_factory(self):
        fti = queryUtility(IDexterityFTI, name='moneysack')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IMoneysack.providedBy(obj),
            u'IMoneysack not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_moneysack_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='moneysack',
            id='moneysack',
        )

        self.assertTrue(
            IMoneysack.providedBy(obj),
            u'IMoneysack not provided by {0}!'.format(
                obj.id,
            ),
        )

    def test_ct_moneysack_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='moneysack')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_moneysack_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='moneysack')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'moneysack_id',
            title='moneysack container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
