# -*- coding: utf-8 -*-

from pyramid.i18n import get_localizer, TranslationStringFactory
from pyramid.events import subscriber, BeforeRender, NewRequest


# use two translator to translate each strings in Make
tsf_server = TranslationStringFactory('waddle-server')
tsf_geoportal = TranslationStringFactory('c2cgeoportal')
tsf_admin = TranslationStringFactory('c2cgeoportal_admin')
tsf_c2cgeoform = TranslationStringFactory('c2cgeoform')


@subscriber(NewRequest)
def add_localizer(event):
    request = event.request
    localizer = get_localizer(request)

    def auto_translate(string):
        if request.path_info.startswith('/admin/'):
            tsf_list = [tsf_admin, tsf_c2cgeoform]
        else:
            tsf_list = [tsf_server, tsf_geoportal]
        for tsf in tsf_list:
            result = localizer.translate(tsf(string))
            if result != string:
                break
        return result

    request.localizer = localizer
    request.translate = auto_translate


@subscriber(BeforeRender)
def add_renderer_globals(event):
    request = event.get('request')
    if request:
        event['_'] = request.translate
        event['localizer'] = request.localizer
