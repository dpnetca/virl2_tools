from virl2_tools import interview
from pytest import raises


# Interview Candidate Creation
def test_reject_nonstring_fist_name():
    with raises(ValueError):
        interview.Candidate(123, "smith")


def test_reject_numeric_fist_name():
    with raises(ValueError):
        interview.Candidate("123", "smith")


def test_reject_blank_fist_name():
    with raises(ValueError):
        interview.Candidate("", "smith")


def test_reject_null_fist_name():
    with raises(ValueError):
        interview.Candidate(None, "smith")


def test_reject_nonstring_last_name():
    with raises(ValueError):
        interview.Candidate("John", 123)


def test_reject_numeric_last_name():
    with raises(ValueError):
        interview.Candidate("John", "123")


def test_reject_blank_last_name():
    with raises(ValueError):
        interview.Candidate("John", "")


def test_reject_null_last_name():
    with raises(ValueError):
        interview.Candidate("John", None)


def test_candidate_lowercase_username():
    user = interview.Candidate("John", "Smith")
    assert user.username == "john.smith"


def test_reject_nonstring_password():
    with raises(ValueError):
        interview.Candidate("John", "Smith", 123)


# Interview VIRL2 Environment Creation
def test_create_environment():
    candidate = interview.Candidate("John", "Smith")
    interview.Environment(candidate)


# TODO test user creation - need to learn how to use mock data
