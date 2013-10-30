# -*- coding: utf-8 -*-

import os

from django.conf import settings

from pdfdocument.document import cm, mm


def create_stationery_fn(*fns):
    def _fn(canvas, document):
        for fn in fns:
            fn(canvas, document.PDFDocument)
    return _fn


class ULBStationery(object):
    def __call__(self, canvas, pdfdocument):
        left_offset = 28.6*mm

        canvas.saveState()
        canvas.setFont('%s' % pdfdocument.style.fontName, 12)
        canvas.drawString(26*mm, 284*mm, 'Conference Registration Platform')
        canvas.setFont('%s' % pdfdocument.style.fontName, 12)
        canvas.drawString(26*mm, 276*mm, u'Université libre de Bruxelles')
        canvas.setFont('%s' % pdfdocument.style.fontName, 10)
        canvas.drawString(26*mm, 268*mm, u'Av. F. Roosevelt, 50 - 1050 Brussels - Belgium')
        canvas.setFont('%s' % pdfdocument.style.fontName, 12)
        canvas.drawString(26*mm, 260*mm, u'EuroSciPy 2013 - The 6th European Conference on Python in Science')
        pdfdocument.draw_watermark(canvas)
        canvas.restoreState()

        canvas.saveState()
        canvas.setFont('%s' % pdfdocument.style.fontName, 6)
        for i, text in enumerate(reversed([pdfdocument.doc.page_index_string()])):
            canvas.drawRightString(190*mm, (8+3*i)*mm, text)

        logo = getattr(settings, 'PDF_LOGO_SETTINGS', None)
        if logo:
            canvas.drawImage(os.path.join(settings.APP_BASEDIR, 'metronom', 'reporting', 'images', logo[0]),
                **logo[1])

        canvas.restoreState()


class PageFnWrapper(object):
    """
    Wrap an old-style page setup function
    """

    def __init__(self, fn):
        self.fn = fn

    def __call__(self, canvas, pdfdocument):
        self.fn(canvas, pdfdocument.doc)
