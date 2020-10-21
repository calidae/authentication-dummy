# -*- coding: utf-8 -*-
import factory
factory.Faker._DEFAULT_LOCALE = 'es_ES'

from .user import * # NOQA: 401
