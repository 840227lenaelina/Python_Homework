import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world!", "Hello world!"),
    ("text123", "Text123")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize("input_str, expected", [
    ("1234test", "1234test"),
    ("!", "!"),
    ("", "")
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive_test
@pytest.mark.parametrize("string_str, expected", [
    (" Hello", "Hello"),
    (" 56", "56"),
    (" text 25", "text 25")
])
def test_trim_positive(string_str, expected):
    assert string_utils.trim(string_str) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize("string_str, expected", [
    (" ", ""),
    ("   123", "123")
])
def test_trim_negative(string_str, expected):
    assert string_utils.trim(string_str) == expected


@pytest.mark.positive_test
@pytest.mark.parametrize("string_str, symbol_str, result", [
    ("Skypro", "S", True),
    ("Skypro", "y", True),
    ("Привет", "П", True),
    ("Привет", "и", True),
    ("Skypro", "l", False),
    ("Привет", "а", False),
    ("123456", "3", True),
    ("123456", "8", False)
])
def test_contains_positive(string_str, symbol_str, result):
    assert string_utils.contains(string_str, symbol_str) == result


@pytest.mark.negative_test
@pytest.mark.parametrize("string_str, symbol_str, result", [
    ("Skypro", "Ф", False),
    ("Skypro", "6", False),
    ("", "a", False)
])
def test_contains_negative(string_str, symbol_str, result):
    assert string_utils.contains(string_str, symbol_str) == result


@pytest.mark.positive_test
@pytest.mark.parametrize("string_str, symbol_str, expected", [
    ("Skypro", "r", "Skypo"),
    ("Привет", "р", "Пивет"),
    ("Skypro", "pro", "Sky"),
    ("text 987", "8", "text 97")
])
def test_delete_symbol_positive(string_str, symbol_str, expected):
    assert string_utils.delete_symbol(string_str, symbol_str) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize("string_str, symbol_str, expected", [
    ("Skypro", "l", "Skypro"),
    ("Привет", "", "Привет"),
    ("text 28", "5", "text 28")
])
def test_delete_symbol_negative(string_str, symbol_str, expected):
    assert string_utils.delete_symbol(string_str, symbol_str) == expected
