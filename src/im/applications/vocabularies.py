# -*- coding: utf-8 -*-
from zope.interface import directlyProvides
from zope.schema.interfaces import IVocabularyFactory

FSD_VOCABULARIES = True
try:
    # from matem.fsdextender.extenders.vocabularies import ClassificationsVocabularyFactory
    from matem.fsdextender.extenders.vocabularies import SedeVocabularyFactory
except ImportError:
    FSD_VOCABULARIES = False


def IMCampusVocabulary(context):
    if FSD_VOCABULARIES:
        return SedeVocabularyFactory
        # campusvocab = SedeVocabularyFactory(context)
        # items = campusvocab._terms
        # items.append(SimpleTerm('NA', 'NA', 'N/A'))
        # return SimpleVocabulary(items)
    return None
directlyProvides(IMCampusVocabulary, IVocabularyFactory)