# -*- coding: utf-8 -*-
from im.applications import _
from zope.interface import directlyProvides
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


FSD_VOCABULARIES = True
try:
    # from matem.fsdextender.extenders.vocabularies import ClassificationsVocabularyFactory
    from matem.fsdextender.extenders.vocabularies import SedeVocabularyFactory
except ImportError:
    FSD_VOCABULARIES = False


def IMCampusVocabulary(context):
    if FSD_VOCABULARIES:
        campusvocab = SedeVocabularyFactory(context)
        items = campusvocab._terms
        # items.append(SimpleTerm('NA', 'NA', 'N/A'))
        return SimpleVocabulary(items)
    return None
directlyProvides(IMCampusVocabulary, IVocabularyFactory)


def TransportationTypeVocabulary(context):
    items = [
        # (_(u'Car'), 'car'),
        (_(u'Ground transportation'), 'groudtransportation'),
        (_(u'Air Transport'), 'airtransport'),
    ]

    items = [SimpleTerm(i[1], i[1], i[0]) for i in items]
    return SimpleVocabulary(items)
directlyProvides(TransportationTypeVocabulary, IVocabularyFactory)

