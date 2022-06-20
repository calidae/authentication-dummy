from trytond.pool import Pool
from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import with_transaction

from trytond.modules.authentication_dummy.tests import factories


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


del ModuleTestCase
