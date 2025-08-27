brikk-returns
=============

.. toctree::
   :hidden:

   Getting Started <self>
   reference

:mod:`brikk.returns` provides two main types inspired by Rust: :class:`Result` and :class:`Option`. These types make success and failure (or presence and absence) explicit in your APIs, improving clarity and type safety.

Installation
------------

.. tab:: pip

    .. code-block:: shell

       pip install brikk-returns

.. tab:: uv

    .. code-block:: shell

       uv add brikk-returns

.. tab:: poetry

    .. code-block:: shell

       poetry add brikk-returns

.. tab:: pipenv

    .. code-block:: shell

       pipenv install brikk-returns

Working with ``Result``
-----------------------

A :class:`Result` represents either success (``Ok``) or failure (``Err``):

.. code-block:: python

    from brikk.returns import Ok, Err

    def divide(a: float, b: float):
        if b == 0:
            return Err("division by zero")
        return Ok(a / b)

    result = divide(10, 2)

    if result.is_ok():
        print("Success:", result.unwrap())
    else:
        print("Error:", result.unwrap_err())

Working with ``Option``
-----------------------

An :class:`Option` represents an optional value: ``Some(value)`` when present,
or ``Nothing`` when absent.

.. code-block:: python

    from brikk.returns import Some, Nothing

    def find_username(user_id: int):
        if user_id == 1:
            return Some("alice")
        return Nothing

    username = find_username(1).unwrap_or("guest")
    print(username)  # "alice"

Chaining and Mapping
--------------------

Both :class:`Result` and :class:`Option` support transformation and chaining
methods such as ``map``, ``map_err``, and ``and_then``:

.. code-block:: python

    value = Some(2).map(lambda x: x * 10).unwrap()
    print(value)  # 20

    total = Ok(5).and_then(lambda x: Ok(x * 2)).unwrap()
    print(total)  # 10
