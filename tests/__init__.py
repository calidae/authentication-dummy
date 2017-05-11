try:
    from trytond.modules.authentication_dummy.tests.test_authentication_dummy import suite
except ImportError:
    from .test_authentication_dummy import suite

__all__ = ['suite']
