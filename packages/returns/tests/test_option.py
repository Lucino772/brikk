from unittest.mock import Mock

import pytest
from brikk.returns import Error, Nothing, Ok, OptionExpectError, OptionUnwrapError, Some


def test_option_is_some():
    assert Some(2).is_some() is True
    assert Nothing().is_some() is False


def test_option_is_some_and():
    assert Some(2).is_some_and(lambda val: val > 1) is True
    assert Some(0).is_some_and(lambda val: val > 1) is False
    assert Nothing().is_some_and(lambda val: val > 1) is False


def test_option_is_none():
    assert Some(2).is_none() is False
    assert Nothing().is_none() is True


def test_option_is_none_or():
    assert Some(2).is_none_or(lambda val: val > 1) is True
    assert Some(0).is_none_or(lambda val: val > 1) is False
    assert Nothing().is_none_or(lambda val: val > 1) is True


def test_option_expect():
    assert Some(2).expect("error occured") == 2
    with pytest.raises(OptionExpectError):
        Nothing().expect("error occured")


def test_option_unwrap():
    assert Some(2).unwrap() == 2
    with pytest.raises(OptionUnwrapError):
        Nothing().unwrap()


def test_option_unwrap_or():
    assert Some(2).unwrap_or(4) == 2
    assert Nothing().unwrap_or(4) == 4


def test_option_unwrap_or_else():
    assert Some(2).unwrap_or_else(lambda: 4) == 2
    assert Nothing().unwrap_or_else(lambda: 4) == 4


def test_option_map():
    assert Some(2).map(lambda val: val * 2) == Some(4)
    assert Nothing().map(lambda val: val * 2) == Nothing()


def test_option_inspect():
    _inspect_func = Mock().inspect_value
    Some(2).inspect(_inspect_func)
    Nothing().inspect(_inspect_func)
    _inspect_func.assert_called_once_with(2)


def test_option_map_or():
    assert Some("foo").map_or(-1, len) == 3
    assert Nothing().map_or(-1, len) == -1


def test_option_map_or_else():
    assert Some("foo").map_or_else(lambda: -1, len) == 3
    assert Nothing().map_or_else(lambda: -1, len) == -1


def test_option_ok_or():
    assert Some("foo").ok_or(0) == Ok("foo")
    assert Nothing().ok_or(0) == Error(0)


def test_option_ok_or_else():
    assert Some("foo").ok_or_else(lambda: 0) == Ok("foo")
    assert Nothing().ok_or_else(lambda: 0) == Error(0)


def test_option_iter():
    assert next(Some(5).iter()) == 5
    with pytest.raises(StopIteration):
        next(Nothing().iter())


def test_option_and():
    assert Some(2).and_(Nothing()) == Nothing()
    assert Nothing().and_(Some("foo")) == Nothing()
    assert Some(2).and_(Some("foo")) == Some("foo")
    assert Nothing().and_(Nothing()) == Nothing()


def test_option_and_then():
    assert Some(2).and_then(
        lambda val: Some(str(val * 2)) if val < 50 else Nothing()
    ) == Some("4")
    assert (
        Some(50).and_then(lambda val: Some(str(val * 2)) if val < 50 else Nothing())
        == Nothing()
    )
    assert (
        Nothing().and_then(lambda val: Some(str(val * 2)) if val < 50 else Nothing())
        == Nothing()
    )


def test_option_filter():
    assert Nothing().filter(lambda val: val % 2 == 0) == Nothing()
    assert Some(3).filter(lambda val: val % 2 == 0) == Nothing()
    assert Some(4).filter(lambda val: val % 2 == 0) == Some(4)


def test_option_or():
    assert Some(2).or_(Nothing()) == Some(2)
    assert Nothing().or_(Some(2)) == Some(2)
    assert Some(2).or_(Some(10)) == Some(2)
    assert Nothing().or_(Nothing()) == Nothing()


def test_option_or_else():
    assert Some("barbarians").or_else(lambda: Some("vikings")) == Some("barbarians")
    assert Nothing().or_else(lambda: Some("vikings")) == Some("vikings")
    assert Nothing().or_else(lambda: Nothing()) == Nothing()


def test_option_xor():
    assert Some(2).xor(Nothing()) == Some(2)
    assert Nothing().xor(Some(2)) == Some(2)
    assert Some(2).xor(Some(2)) == Nothing()
    assert Nothing().xor(Nothing()) == Nothing()


def test_option_flatten():
    assert Some(Some(6)).flatten() == Some(6)
    assert Some(Nothing()).flatten() == Nothing()
    assert Nothing().flatten() == Nothing()


def test_option_transpose():
    assert Some(Ok(5)).transpose() == Ok(Some(5))


def test_result_zip():
    assert Some(2).zip(Some(3)) == Some((2, 3))
    assert Some(2).zip(Nothing()) == Nothing()
    assert Nothing().zip(Some(3)) == Nothing()
    assert Some(2).zip(Some(3)).zip(Some(5)) == Some((2, 3, 5))
    assert Some(2).zip(Nothing()).zip(Some(5)) == Nothing()
