import unittest

from trytond.pool import Pool
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import with_transaction

from . import factories


class AuthenticationDummyTestCase(ModuleTestCase):
    'Test Authentication Dummy module'
    module = 'authentication_dummy'

    @with_transaction()
    def test_login_dummy(self):

        # GIVEN
        User = Pool().get('res.user')
        user = factories.User.create(
            login='test',
            password='good_pass'
        )

        # WHEN
        login = User.get_login('test', {})

        # THEN
        self.assertEqual(login, user.id)


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(
            AuthenticationDummyTestCase
        )
    )
    return suite
