__version__ = '6.2.1'

from trytond.pool import Pool

from .user import User  # NOQA: 401

__all__ = ['register']


def register():
    Pool.register(
        User,
        module='authentication_dummy', type_='model')
