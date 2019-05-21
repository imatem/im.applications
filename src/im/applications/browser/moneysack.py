# -*- coding: utf-8 -*-
# from collections import OrderedDict
from im.applications import _
# from operator import itemgetter
from plone.autoform.view import WidgetsView
from plone.dexterity.interfaces import IDexterityFTI
from plone.dexterity.utils import getAdditionalSchemata
# from UNAM.imateCVct.tools.cv_pdfconfig import titleByType
from zope.component import getUtility
# from zope.schema.interfaces import IVocabularyFactory
# import collections

# from plone import api
# import ast
# from zope.component.hooks import getSite
# from plone.i18n.normalizer import idnormalizer as idn

# import copy
# import ast


class MoneySackView(WidgetsView):
    """This class is the same in plone.dexterity.browser.view.DefaultView
    The default view for Dexterity content. This uses a WidgetsView and
    renders all widgets in display mode.
    """

    @property
    def schema(self):
        fti = getUtility(IDexterityFTI, name=self.context.portal_type)
        return fti.lookupSchema()

    @property
    def additionalSchemata(self):
        return getAdditionalSchemata(context=self.context)
