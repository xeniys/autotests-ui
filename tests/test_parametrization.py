import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize('number', [1, 2, 3, -1])
def test_numbers(number):
    assert number > 0


@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9), (-1, 1)])
def test_several_numbers(number, expected):
    assert number * number == expected


@pytest.mark.parametrize('os', ['mac', 'windows', 'linux', 'debian'])
@pytest.mark.parametrize('browser', ['chromium', 'webkit', 'firefox'])
def test_multiplication_of_numbers(os, browser):
    assert len(os + browser) > 0


@pytest.fixture(params=['chromium', 'webkit', 'firefox'])
def browser(request):
    return request.param


def test_open_browser(browser: str):
    print("Running test:", browser)


@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOperations:
    @pytest.mark.parametrize('account', ['credit', 'debit'])
    def test_user_with_operations(self, user, account):
        ...

    def test_user_without_operations(self, user):
        ...


users = {
    '232323': 'user with money on bank acc',
    '23232323': 'user without money on bank acc',
    '12342': 'user with operations on bank acc'
}


@pytest.mark.parametrize('phone', users.keys(),
                         ids=lambda phone_number: f'{phone_number}: {users[phone_number]}')
def test_identifiers(phone):
    ...
