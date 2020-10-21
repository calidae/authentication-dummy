# -*- coding: utf-8 -*-

import factory

from factory_trytond import TrytonFactory


class User(TrytonFactory):
    class Meta:
        model = 'res.user'

    name = factory.Faker('name')
    login = factory.Faker('user_name')
    email = factory.Faker('ascii_company_email')
    password = factory.Faker('password', length=10)
