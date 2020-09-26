import pytest
from src import utils

@pytest.mark.parametrize('value,expected', [
    ('normal value input', '"normal value input"'),
    ('content with " in it', '"content with \\" in it"'),
    (42, '42')
])
def test_sanitize(value, expected):
    sanitized_value = utils.sanitize(value)

    assert sanitized_value == expected
