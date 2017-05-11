import unittest


from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import suite as test_suite


class AuthenticationDummyTestCase(ModuleTestCase):
    'Test Authentication Dummy module'
    module = 'authentication_dummy'


def suite():
    suite = test_suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            AuthenticationDummyTestCase))
    return suite
