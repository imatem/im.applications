# -*- coding: utf-8 -*-
# from im.applications import _
from Products.Five.browser import BrowserView


class AppImBudgetFolderView(BrowserView):

    def __init__(self, context, request):
        self.context = context
        self.request = request

