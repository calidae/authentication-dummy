from trytond.pool import PoolMeta

__all__ = ['User']


class User(metaclass=PoolMeta):
    __name__ = 'res.user'

    @classmethod
    def _login_dummy(cls, login, parameters):
        user_id, _, _ = cls._get_login(login)
        if user_id:
            return user_id
        return
