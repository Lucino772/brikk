from brikk.returns import Error, Nothing, Ok, Some, collect, unpack, zipped


def test_collect():
    assert collect(Ok(tuple()), [Ok(1), Ok(2), Ok(3)]) == Ok((1, 2, 3))
    assert collect(Ok(tuple()), [Ok(1), Error("error"), Ok(3)]) == Error("error")
    assert collect(Some(tuple()), [Some(1), Some(2), Some(3)]) == Some((1, 2, 3))
    assert collect(Some(tuple()), [Some(1), Nothing(), Some(3)]) == Nothing()


def test_zipped():
    assert Ok(2).and_then(zipped(lambda x: Ok(x * 10))) == Ok((2, 20))
    assert Error("error").and_then(zipped(lambda x: Ok(x * 10))) == Error("error")
    assert Some(2).and_then(zipped(lambda x: Some(x * 10))) == Some((2, 20))
    assert Nothing().and_then(zipped(lambda x: Some(x * 10))) == Nothing()


def test_unpack():
    assert Ok((2, "hello")).and_then(unpack(lambda n, msg: Ok(msg * n))) == Ok(
        "hellohello"
    )
    assert Some((2, "hello")).and_then(unpack(lambda n, msg: Some(msg * n))) == Some(
        "hellohello"
    )
