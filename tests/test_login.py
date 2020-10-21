

from trytond.tests.test_tryton import DB_NAME
from werkzeug.test import Client
from trytond.wsgi import app
from werkzeug.wrappers import Response
from werkzeug.wrappers.json import JSONMixin, _JSONModule
from trytond.protocols.jsonrpc import JSONDecoder, JSONEncoder


class TrytonJSONModule(_JSONModule):
    @classmethod
    def dumps(cls, obj, **kw):
        kw.setdefault('cls', JSONEncoder)
        return super().dumps(obj, **kw)

    @staticmethod
    def loads(s, **kw):
        kw.setdefault('object_hook', JSONDecoder())
        return _JSONModule.loads(s, **kw)


class JSONResponse(JSONMixin, Response):
    json_module = TrytonJSONModule


class LoginTestCase(object):

    def test_login_dummy(self):
        # GIVEN
        client = Client(app, JSONResponse)

        # WHEN
        user_id, user_login = self.user
        result = client.post(
            '/{}/'.format(DB_NAME),
            json={
                'method': 'common.db.login',
                'params': [user_login, 'chupala']
            },
        )
        result, _ = result.json

        # THEN
        self.assertEqual(result, user_id)
