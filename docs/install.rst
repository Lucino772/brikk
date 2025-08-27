Installation
============

You can install any brikk package individually:

.. tab:: pip

    .. code-block:: shell

       pip install brikk-returns brikk-cancel

.. tab:: uv

    .. code-block:: shell

       uv add brikk-returns brikk-cancel

.. tab:: poetry

    .. code-block:: shell

       poetry add brikk-returns brikk-cancel

.. tab:: pipenv

    .. code-block:: shell

       pipenv install brikk-returns brikk-cancel

Available Packages
------------------

brikk consists of a collection of small, focused Python packages. Below is the full list of all available packages you can install and use:

.. list-table::
    :widths: 20 80
    :header-rows: 1
    :stub-columns: 1

    * - Package
      - Description
    * - :doc:`brikk-cancel <../packages/cancel/index>`
      - Cooperative cancellation tokens, modeled after Go's context, enabling cancellation of async and sync operations.
    * - :doc:`brikk-config <../packages/config/index>`
      - Type-safe, layered configuration system with environment variables, files, and overrides support.
    * - :doc:`brikk-returns <../packages/returns/index>`
      - Typed ``Result`` and ``Option`` types inspired by Rust for safe and expressive error handling without exceptions.
