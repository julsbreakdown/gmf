# -*- coding: utf-8 -*-

import logging

from pyramid.i18n import TranslationStringFactory

from c2cgeoportal_commons.models.main import *  # noqa

_ = TranslationStringFactory('waddle-server')
LOG = logging.getLogger(__name__)
