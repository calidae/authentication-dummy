import unittest

import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase
from trytond.transaction import Transaction
from trytond.tests.test_tryton import DB_NAME
from trytond.pool import Pool

from .test_login import LoginTestCase


class AuthenticationDummyTestCase(
        ModuleTestCase,
        LoginTestCase,
):
    'Test Authentication Dummy module'
    module = 'authentication_dummy'

    user = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        with Transaction().start(DB_NAME, 0, autocommit=True):
            User = Pool().get('res.user')
            # TODO: Factories
            (user,) = User.create([{
                'name': 'Test',
                'login': 'test',
                'password': 'dontmind'
            }])
            cls.user = [user.id, user.login]


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(
            AuthenticationDummyTestCase
        )
    )
    return suite
