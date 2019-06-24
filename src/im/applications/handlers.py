# -*- coding: utf-8 -*-
from im.applications import _
from im.applications.content.coloquio_application import IColoquioApplication
from zope.component import adapter
# from zope.lifecycleevent.interfaces import IObjectAddedEvent
# from zope.lifecycleevent.interfaces import IObjectCreatedEvent
# from zope.lifecycleevent.interfaces import IObjectModifiedEvent

from Products.DCWorkflow.interfaces import IAfterTransitionEvent


@adapter(IColoquioApplication, IAfterTransitionEvent)
def handlerPrepareToNextState(self, event):

    if not event.transition:
        return

    if event.transition.id == 'submit_commission':
        self.prepareToCommission()

    elif event.transition.id == 'submit_consejo':
        self.prepareToConsejo()

    elif event.transition.id == 'return_commission':
        self.return_commission()

    elif event.transition.id == 'approve':
        self.prepareToFinalize




