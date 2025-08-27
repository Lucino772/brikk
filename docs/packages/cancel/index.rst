brikk-cancel
============

.. toctree::
   :hidden:

   Getting Started <self>
   reference

Installation
------------

.. tab:: pip

    .. code-block:: shell

       pip install brikk-cancel

.. tab:: uv

    .. code-block:: shell

       uv add brikk-cancel

.. tab:: poetry

    .. code-block:: shell

       poetry add brikk-cancel

.. tab:: pipenv

    .. code-block:: shell

       pipenv install brikk-cancel


Usage
-----

:mod:`brikk.cancel` is a lightweight, type-safe way to manage cancellation in synchronous Python code. It uses *cancellation tokens* to signal and respond to cancellation requests, making it easy to stop long-running or cooperative tasks gracefully.

You can start with a **default token**, returned by :func:`default() <brikk.cancel.default>`, which never cancels. This is useful when an API requires a token but no actual cancellation is needed.

To create a cancellable token, use :func:`with_cancel() <brikk.cancel.with_cancel>`:

.. code-block:: python

    from brikk.cancel import with_cancel, default

    token, cancel = with_cancel(default())
    cancel()
    assert token.is_cancelled()

Tokens can also be set to **timeout automatically** using
:func:`with_timeout() <brikk.cancel.with_timeout>`:

.. code-block:: python

    from brikk.cancel import with_timeout, TokenTimeoutError, default

    token, _ = with_timeout(default(), 2.0)

    try:
        token.wait()
    except TokenTimeoutError:
        print("Timed out")

You can **check whether a token is cancelled** with the type guard
:func:`is_token_cancelled() <brikk.cancel.is_token_cancelled>`:

.. code-block:: python

    from brikk.cancel import is_token_cancelled, with_cancel, default

    token, cancel = with_cancel(default())
    cancel()

    if is_token_cancelled(token):
        print("Cancelled with:", token.get_error())
