What is Brikk ?
===============

.. toctree::
   :caption: Getting Started
   :hidden:

   self
   install

.. toctree::
   :caption: Packages
   :hidden:
   :glob:

   packages/**/index


**brikk** is a collection of small, focused Python packages, foundational building blocks designed to help you write better code.

Each package in ``brikk`` solves a single problem well, whether it's managing configuration, handling errors, or supporting cooperative cancellation. You can use one package or many, they're designed to be **independent, lightweight, and composable**.

The name comes from *brick*, as in *building blocks*. brikk aims to be a toolkit of composable primitives for building Python applications from the ground up.

Why Brikk ?
-----------

- 🧩 **Modular**: only install what you need
- 📦 **Typed**: built with modern Python type hints and static analysis in mind
- 🔍 **Minimal**: no heavy dependencies, no hidden magic
- 🛠️ **Practical**: inspired by proven ideas from Rust, Go, and other ecosystems
- ⛓️ **Composable**: use brikk in scripts, libraries, or full applications

Intended Use Cases
------------------

brikk is designed to be a reliable foundation for a wide range of Python projects, from small libraries to large-scale applications. It's especially suited for:

- Developers building maintainable libraries, services, or internal tools
- Teams that value strong typing, clear semantics, and composable design
- Projects where explicitness and simplicity are more important than frameworks or hidden magic
- Codebases that aim to grow sustainably over time without becoming rigid or complex

Design
------

brikk is developed as a monorepo of standalone Python packages, each one published independently and following semantic versioning. The project is managed using `uv <https://github.com/astral-sh/uv>`_ workspaces, making it easy to evolve brikk as a consistent, long-term toolkit.

New packages may be introduced over time, but the philosophy will stay the same: **small, well-crafted tools that do one thing well**, and play nicely with the rest of your stack.
