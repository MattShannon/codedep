codedep
=======

This package provides a simple, semi-automated way to do code-level dependency
tracking for python projects.

Problem
-------

The central idea is to be able to compute, for a given function or class, a
hash of all the python source code that the function or class depends on.
A given function or class is considered to depend on its immediate source code
definition, on the source code defining functions or classes referred to in its
immediate definition, and so on.
For example if a class ``Foo`` uses a function ``bar`` in one of its methods,
then the hash value for ``Foo`` is based on the source code defining both
``Foo`` and ``bar``.

The ability to compute such a hash value allows automated tracking of when the
behaviour of a given function or class changes (or rather, might have changed).
For example the author's original use case was for distributing jobs on a
compute grid, where it was useful to be able to determine automatically when
a job needed to be re-run because of changes to the source code.

Approach used by codedep
------------------------

Computing such a hash value is presumably very difficult to do in a fully
automated way, partly because of the dynamic nature of python.
The approach taken in this package is to require an explicit annotation for
each function ``fn`` (or class) giving the list of functions or classes that
are referred to in the definition of ``fn``.
For example if a class ``Foo`` uses functions ``bar`` and ``baz`` in its
methods, then ``Foo`` could be decorated with ``@codeDeps(bar, baz)``.
Everything else required to compute the hash value is looked-up automatically
using existing tools such as the inspect module.
To help with the burden of maintaining the ``@codeDeps`` lists, an automated
tool is provided which suggests dependencies which may have been forgotten or
may have been added unnecessarily.
This semi-automated approach has the advantage that it can cope with the common
cases easily while allowing the user control when they know better than the
tool.

There are a few limitations on what the scheme used here can do:

- It only allows dependencies to be specified and hash values to be computed
  for top-level functions and classes, not nested ones.
- Behind the scenes the decorators add special values to the dictionary of the
  thing being decorated, so the thing being decorated has to have such a
  dictionary.
  This is the case for standard functions and classes.
- Global (module-level) variables cannot be declared as dependencies since
  it is not possible to find their source code definitions using inspect.
  For safety it is therefore recommended to have no global variables (other
  than function and class definitions) when using this package.

The scheme used here has the advantage of being relatively simple.
The entire code to do the decoration and compute hashes is around 200 lines.
It is hoped that this simplicity will allow reasoning about how the scheme will
operate in any tricky edge cases.

Usage
-----

A sample python project is provided in the ``example`` directory.
The file ``example/foo.py`` defines some functions and classes.
The script ``example/print_hash.py`` prints some of the computed hashes for the
functions and classes, together with some values computed by the functions and
classes.

Typing::

    PYTHONPATH=. python -m example.print_hash

should give the output::

    hash of baz = 1a0ebbff92a8a8691c17a460b8eeb4cb38399c60
    hash of Foo = 96a9e852464e99d68d2769655a8113de33ee0721
    value1 = 6
    value2 = 0

If you now change the definition of ``qux`` in ``example/foo.py`` to multiply
by 3 instead of 2, then the above command will output::

    hash of baz = 0c955f9963b6acb422501d5ee64e6bdedc5c204b
    hash of Foo = 572f8685fde1670fa720df6ebbf89a6cc8dd1e4c
    value1 = 9
    value2 = 0

Suitable ``@codeDeps`` decorator lines can be suggested using an automated
tool.
Running::

    bin/codedep_check example/foo.py

should print ``(no change)`` as one of its lines of output.
If you now change the definition of ``baz`` in ``example/foo.py`` to
``return qux(bar(x) - 2)`` and re-run the automated tool then you should be
taken to a vimdiff of the original and suggested files.
The tool picks up the fact that ``baz`` now depends on ``bar``.

Note that ``bin/codedep_check`` is a wrapper around
``codedep/check_deps.py``.
The wrapper makes certain assumptions about the structure of the project
(see ``bin/codedep_check`` for details).
In complicated cases it is intended that this wrapper be copied and customized
to a version suitable for the specific project.

License
-------

Please see the file ``License`` for details of the license and warranty for
codedep.

Source
------

`codedep <https://github.com/MattShannon/codedep>`_ is hosted on github.
To obtain the latest source code using git::

    git clone git://github.com/MattShannon/codedep.git

Bugs
----

Please use the
`issue tracker <https://github.com/MattShannon/codedep/issues>`_ to submit bug
reports.

Contact
-------

The author of codedep is `Matt Shannon <mailto:matt.shannon@cantab.net>`_.
