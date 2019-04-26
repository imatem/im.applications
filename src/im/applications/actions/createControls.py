# -*- coding: utf-8 -*-
# from DateTime import DateTime
from OFS.SimpleItem import SimpleItem
from plone import api
from im.applications import _
# from plone.app.contentrules.browser.formhelper import NullAddForm
from plone.contentrules.rule.interfaces import IExecutable, IRuleElementData
# from plone.i18n.normalizer import idnormalizer
# from Products.CMFCore.WorkflowCore import WorkflowException
# from Products.CMFPlone import utils
# from Products.statusmessages.interfaces import IStatusMessage
from zope.component import adapts
# from zope.event import notify
from zope.interface import implements
from zope.interface import Interface
# from zope.lifecycleevent import ObjectModifiedEvent


class ICreateControlsAction(Interface):
    """Interface for the configurable aspects of create controls action.
    """


class CreateControlsAction(SimpleItem):
    """The actual persistent implementation of the action element.
    """
    implements(ICreateControlsAction, IRuleElementData)

    message = ''
    element = 'matem.actions.applications.CreateControls'

    @property
    def summary(self):
        return _(u"The im applications information will be saved in the Uni Admin Section")


class CreateControlsActionExecutor(object):
    """The executor for this action.
    """
    implements(IExecutable)
    adapts(Interface, ICreateControlsAction, Interface)

    def __init__(self, context, element, event):
        self.context = context
        self.element = element
        self.event = event

    def __call__(self):

        obj = self.event.object
        with api.env.adopt_user(username='admin'):
            self.createControls(obj)

        return True


def createControls(self, obj)
