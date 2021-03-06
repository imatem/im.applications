# -*- coding: utf-8 -*-
from im.applications import _
from plone.dexterity.content import Container
from plone.supermodel import model
from zope import schema
from zope.interface import Invalid
from zope.interface import invariant
from zope.interface import implementer
from plone import api


class IMoneysack(model.Schema):
    """ Marker interface and Dexterity Python Schema for Moneysack
    """
    title = schema.TextLine(
        title=_(u'label_applications_moneysack_title', default=u'Title of sack'),
        required=True,
    )

    start = schema.Date(
        title=_(u'label_applications_moneysack_start_date', default=u'Start date of the activity'),
        required=True,
    )

    end = schema.Date(
        title=_(u'label_applications_moneysack_end_date', default=u'End date of the activity'),
        required=True,
    )

    amount = schema.Float(
        title=_(u'label_applications_moneysack_amount', u'Approved Amount'),
        required=True,
        min=1.0,
        # max=25000.0,
    )

    amountmax = schema.Float(
        title=_(u'label_applications_moneysack_amountmax', u'Max Approved Amount by application'),
        description=_(u'help_applications_moneysack_amountmax', u'If this field is empty the max amount application is the Approved Amount'),
        required=False,
        min=1.0,
        # max=25000.0,
    )

    @invariant
    def validateDateFields(data):
        if data.end < data.start:
            message = 'Invalid Dates: the Star Date must be greater that End Date, please correct it.'
            raise Invalid(_('label_applications_error_datesbefore', default=message))


@implementer(IMoneysack)
class Moneysack(Container):
    """
    """

    def amount_used(self):
        brains = api.content.find(context=self, portal_type='coloquio_application', review_state='approved')
        values = [b.getObject().amount_used() for b in brains]
        return sum(values)

    def remaining_amount(self):
        return self.amount - self.amount_used()




