import pytest


@pytest.fixture(scope='session')
def before_suite():
    print("Método executado no inicio da suíte")
