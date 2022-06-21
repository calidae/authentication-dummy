
import pytest

from trytond.pool import Pool


@pytest.fixture(scope='session')
def trytond_modules():
    yield [
        'tests',
        'authentication_dummy',
    ]


@pytest.fixture
def pool(transaction):
    return Pool()
