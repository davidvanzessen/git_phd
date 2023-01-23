import pytest
from pow2 import *

def test_pow_number():
    assert pow(5) == 25

def test_pow_number_str():
    assert pow("5") == 25

def test_pow_negative_number_str():
    assert pow("-5") == 25

def test_pow_letter():
    with pytest.raises(ValueError):
        assert pow("a")

def test_main_numbers_txt(capsys: pytest.CaptureFixture):
    main("numbers.txt")
    stdout = capsys.readouterr()
    assert """1
4
9
16
25
36
49
64
81
100
""" == stdout.out

def test_main_numbers_with_letter(capsys: pytest.CaptureFixture):
    with pytest.raises(SystemExit) as exit_info:
        main("numbers_with_letter.txt")
    assert exit_info.value.code == 1
    stdout = capsys.readouterr()
    assert """1
4
9
Could not parse: a
""" == stdout.out