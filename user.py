from future.utils import with_metaclass

from trytond.pool import PoolMeta

__all__ = ['User']


class User(with_metaclass(PoolMeta)):
    __name__ = 'res.user'

    @classmethod
    def _login_dummy(cls, login, parameters):
        user_id, _, _ = cls._get_login(login)
        if user_id:
            return user_id
        return
