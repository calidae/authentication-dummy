
import pytest


@pytest.fixture(scope='session')
def trytond_modules():
    yield [
        'tests',
    ]