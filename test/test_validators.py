import pytest
import utils.validators as val

def test_marks_cannot_be_negative():
    with pytest.raises(ValueError):
        val.val_marks(-1)

def test_marks_must_be_int():
    with pytest.raises(ValueError):
        val.val_marks("marks")

def test_marks_cannot_be_empty():
    with pytest.raises(ValueError):
        val.val_marks("")

def test_marks_must_be_between_0_and_100():
    with pytest.raises(ValueError):
        val.val_marks(101)

def test_marks_can_be_100():
    assert val.val_marks(100) is None

def test_name_cannotbe_empty():
    with pytest.raises(ValueError):
        val.val_student_name("")

def test_name_must_be_string():
    with pytest.raises(ValueError):
        val.val_student_name("1")

def test_name_cannotbe_spaces():
    with pytest.raises(ValueError):
        val.val_student_name("   ")

def test_name_must_contain_only_letters():
    with pytest.raises(ValueError):
        val.val_student_name("abc123")

def test_contact_number_too_short():
    with pytest.raises(ValueError):
        val.val_contact_number("123456789")

def test_contact_number_too_long():
    with pytest.raises(ValueError):
        val.val_contact_number("12345678901")

def test_contact_number_must_be_digits():
    with pytest.raises(ValueError):
        val.val_contact_number("abc1234567")

def test_contact_number_cannot_be_empty():
    with pytest.raises(ValueError):
        val.val_contact_number("")

def test_right_contact_number():
    assert val.val_contact_number("1234567890") is None