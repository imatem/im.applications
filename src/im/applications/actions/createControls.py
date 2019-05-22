# -*- coding: utf-8 -*-
from DateTime import DateTime
from OFS.SimpleItem import SimpleItem
from plone import api
from im.applications import _
from plone.app.contentrules.browser.formhelper import NullAddForm
from plone.contentrules.rule.interfaces import IExecutable, IRuleElementData
# from plone.i18n.normalizer import idnormalizer
# from Products.CMFCore.WorkflowCore import WorkflowException
# from Products.CMFPlone import utils
# from Products.statusmessages.interfaces import IStatusMessage
from zope.component import adapts
from zope.event import notify
from zope.interface import implements
from zope.interface import Interface
from zope.lifecycleevent import ObjectModifiedEvent

import datetime


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


class CreateControlsForAppicationsActionExecutor(object):
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


    def createControls(self, obj):

        data = {}
        data['title'] = obj.Title()
        data['relatedsolicitud'] = obj.UID()
        # data['ownerid'] = obj.getOwner().getId()
        # obj_person = api.content.find(portal_type='FSDPerson', id=data['ownerid'])[0].getObject()
        # classifications = [c.id for c in obj_person.getClassifications()]
        # data['classifications'] = classifications
        data['classification'] = 'NA'
        data['campus'] = 'NA'
        # data['fecha_desde'] = DateTime(obj.start.__str__())
        # data['fecha_desde'] = DateTime(obj.start)
        data['start'] = obj.start
        # data['start'] = DateTime(obj.start.__str__())
        data['end'] = obj.end
        # data['end'] = DateTime(obj.end.__str__())
        data['amount'] = obj.amount

        if obj.portal_type == 'Activities Budget Application':
            self.createViaticalControl(data)

    def createViaticalControl(self, data):
        portal = api.portal.get()
        uniadmin_path = 'unidad/viaticos'
        uniadmin_folder = portal.unrestrictedTraverse(uniadmin_path)
        viaticalcontrol = api.content.create(
            type='viatical',
            title=data['title'],
            container=uniadmin_folder
        )
        viaticalcontrol.relatedsolicitud = data['relatedsolicitud']
        viaticalcontrol.classification = data['classification']
        viaticalcontrol.campus = data['campus']
        viaticalcontrol.amount = data['amount']
        # viaticalcontrol.start = data['start']
        # viaticalcontrol.end = data['end']
        viaticalcontrol.start = DateTime(data['start'].__str__())
        viaticalcontrol.end = DateTime(data['end'].__str__())
        # today = DateTime()
        today = datetime.date.today()
        # if data['fecha_desde'] - today >= 20:
        if (data['start'] - today).days >= 20:
            viaticalcontrol.payment_type = 'payment'
        else:
            viaticalcontrol.payment_type = 'repayment'

        # if data['fecha_desde'] - today >= 20:
        if (data['start'] - today).days >= 20:
            viaticalcontrol.timecontrol_type = 'timely'
        else:
            viaticalcontrol.timecontrol_type = 'untimely'
        notify(ObjectModifiedEvent(viaticalcontrol))


class CreateControlsForApplicationsAddForm(NullAddForm):
    """A degenerate "add form"" for FillHRegisters actions.
    """

    def create(self):
        # a = CategorizationAction()
        # form.applyChanges(a, self.form_fields, data)
        # return a
        return CreateControlsAction()

