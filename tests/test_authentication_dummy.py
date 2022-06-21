from trytond.pool import Pool

from . import factories


def test_login_dummy():

    # GIVEN
    User = Pool().get('res.user')
    user = factories.User.create(
        login='test',
        password='good_pass'
    )

    # WHEN
    login = User.get_login('test', {})

    # THEN
    assert login == user.id
