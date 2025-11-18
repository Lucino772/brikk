from unittest.mock import Mock

import pytest
from brikk.returns import (
    Error,
    Nothing,
    Ok,
    Option,
    Result,
    ResultExpectError,
    ResultUnwrapError,
    Some,
)


def test_result_is_ok():
    assert Ok(2).is_ok() is True
    assert Error("error").is_ok() is False


def test_result_is_ok_and():
    assert Ok(2).is_ok_and(lambda x: x > 1) is True
    assert Ok(0).is_ok_and(lambda x: x > 1) is False
    assert Error("error").is_ok_and(lambda x: x > 1) is False


def test_result_is_err():
    assert Ok(2).is_err() is False
    assert Error("error").is_err() is True


def test_result_is_err_and():
    assert Error("error").is_err_and(lambda e: e == "error") is True
    assert Error("other").is_err_and(lambda e: e == "error") is False
    assert Ok(2).is_err_and(lambda e: e == "error") is False


def test_result_ok():
    assert Ok(2).ok() == Some(2)
    assert Error("error").ok() == Nothing()


def test_result_err():
    assert Ok(2).err() == Nothing()
    assert Error("error").err() == Some("error")


def test_result_map():
    assert Ok(2).map(lambda x: x**2) == Ok(4)
    assert Error("error").map(lambda x: x**2) == Error("error")


def test_result_map_or():
    assert Ok("foo").map_or(-1, lambda v: len(v)) == 3
    assert Error("error").map_or(-1, lambda v: len(v)) == -1


def test_result_map_or_else():
    assert Ok("foo").map_or_else(lambda e: -1, lambda v: len(v)) == 3
    assert Error("error").map_or_else(lambda e: -1, lambda v: len(v)) == -1


def test_result_map_err():
    assert Ok(2).map_err(lambda e: str(e)) == Ok(2)
    assert Error(14).map_err(lambda e: str(e)) == Error("14")


def test_result_inspect():
    _inspect_func = Mock().inspect_value
    Ok(2).inspect(_inspect_func)
    Error("error").inspect(_inspect_func)
    _inspect_func.assert_called_once_with(2)


def test_result_inspect_err():
    _inspect_func = Mock().inspect_value
    Ok(2).inspect_err(_inspect_func)
    Error("error").inspect_err(_inspect_func)
    _inspect_func.assert_called_once_with("error")


def test_result_iter():
    assert next(Ok(2).iter()) == 2
    with pytest.raises(StopIteration):
        next(Error("error").iter())


def test_result_expect():
    assert Ok(2).expect("what happend?") == 2
    with pytest.raises(ResultExpectError):
        Error("error").expect("what happend?")


def test_result_unwrap():
    assert Ok(2).unwrap() == 2
    with pytest.raises(ResultUnwrapError):
        Error("error").unwrap()


def test_result_expect_err():
    assert Error("error").expect_err("what happend?") == "error"
    with pytest.raises(ResultExpectError):
        Ok(2).expect_err("what happend?")


def test_result_unwrap_err():
    assert Error("error").unwrap_err() == "error"
    with pytest.raises(ResultUnwrapError):
        Ok(2).unwrap_err()


def test_result_and():
    assert Ok(2).and_(Error("error")) == Error("error")
    assert Error("error").and_(Ok(2)) == Error("error")
    assert Error("first error").and_(Error("second errror")) == Error("first error")
    assert Ok(2).and_(Ok("other value")) == Ok("other value")


def test_result_and_then():
    assert Ok(2).and_then(lambda v: Ok(v * 2) if v < 50 else Error("too big")) == Ok(4)
    assert Ok(100).and_then(
        lambda v: Ok(v * 2) if v < 50 else Error("too big")
    ) == Error("too big")
    assert Error("error").and_then(
        lambda v: Ok(v * 2) if v < 50 else Error("too big")
    ) == Error("error")


def test_result_or():
    assert Ok(2).or_(Ok(100)) == Ok(2)
    assert Ok(2).or_(Error("error")) == Ok(2)
    assert Error("error").or_(Ok(2)) == Ok(2)
    assert Error("error").or_(Error("other")) == Error("other")


def test_result_or_else():
    assert Ok(2).or_else(lambda x: Ok(x**2)) == Ok(2)
    assert Ok(2).or_else(lambda _: Error("error")) == Ok(2)
    assert Error(2).or_else(lambda x: Ok(x**2)) == Ok(4)
    assert Error(2).or_else(lambda _: Error("error")) == Error("error")


def test_result_unwrap_or():
    assert Ok(4).unwrap_or(2) == 4
    assert Error("error").unwrap_or(2) == 2


def test_result_unwrap_or_else():
    assert Ok(2).unwrap_or_else(lambda x: len(x)) == 2
    assert Error("foo").unwrap_or_else(lambda x: len(x)) == 3


def test_result_unwrap_or_raise():
    assert Ok(2).unwrap_or_raise() == 2
    with pytest.raises(ValueError):
        Error(ValueError()).unwrap_or_raise()


def test_result_flatten():
    assert Ok(Ok(2)).flatten() == Ok(2)
    assert Ok(Error("error")).flatten() == Error("error")
    assert Error("error").flatten() == Error("error")


def test_result_transpose():
    val: Result[Option[int], Exception] = Ok(Some(5))
    val.transpose()
    assert Ok(Some(5)).transpose() == Some(Ok(5))


def test_result_zip():
    assert Ok(2).zip(Ok(3)) == Ok((2, 3))
    assert Ok(2).zip(Error("error")) == Error("error")
    assert Error("error").zip(Ok(3)) == Error("error")
    assert Ok(2).zip(Ok(3)).zip(Ok(5)) == Ok((2, 3, 5))
    assert Ok(2).zip(Error("test")).zip(Ok(5)) == Error("test")
