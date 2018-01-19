from trytond.pool import Pool

__all__ = ['register']
from .user import User


def register():
    Pool.register(
        User,
        module='authentication_dummy', type_='model')
