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


# def ActivityTypeVocabulary(context):
#     items = [
#         # (_(u'Car'), 'car'),
#         (_(u'Ground transportation'), 'groudtransportation'),
#         (_(u'Air Transport'), 'airtransport'),
#     ]

#     items = [SimpleTerm(i[1], i[1], i[0]) for i in items]
#     return SimpleVocabulary(items)
# directlyProvides(ActivityTypeVocabulary, IVocabularyFactory)


def TypeActivityIMVocabularyFactory(context):
    items = [
        (_(u'Coloquio'), '01'),
        (_(u'Conferencia'), '02'),
        (_(u'Congreso'), '03'),
        (_(u'Curso'), '04'),
        (_(u'Diplomado'), '05'),
        (_(u'Encuentro'), '06'),
        (_(u'Foro'), '07'),
        (_(u'Jornada'), '08'),
        (_(u'Mesa redonda'), '09'),
        (_(u'Módulos de exposiciones'), '10'),
        (_(u'Módulos de ferias'), '11'),
        (_(u'Reunión'), '12'),
        (_(u'Seminario'), '13'),
        (_(u'Simposio'), '14'),
        (_(u'Taller'), '15'),
        (_(u'Videoconferencia'), '16'),
        (_(u'Feria'), '17'),
        (_(u'Cátedra'), '32'),
        (_(u'Escuela'), '101'),
        (_(u'Otra actividad'), '99'),
    ]
    items = [SimpleTerm(i[1], i[1], i[0]) for i in items]
    return SimpleVocabulary(items)
directlyProvides(TypeActivityIMVocabularyFactory, IVocabularyFactory)
