reStructured风格示例
---------------------


Sphinx 中关于 reStructuredText 的简单说明：`reStructuredText Primer`_

另一个解释的不错的网站：`Restructured Text (reST) and Sphinx CheatSheet`_

.. _reStructuredText Primer:
    http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

.. _Restructured Text (reST) and Sphinx CheatSheet:
    http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html

.. py:module:: reStructured

示例
=====

.. literalinclude:: ../../reStructured/__init__.py
    :language: python
    :lines: 11-26
.. autofunction:: example

代码段示例
===========

.. literalinclude:: ../../reStructured/__init__.py
    :language: python
    :lines: 53-72
.. autofunction:: code_block

颜色框(note;warning;error;todo)示例
=============================

.. literalinclude:: ../../reStructured/__init__.py
    :language: python
    :lines: 30-50
.. autofunction:: colored_box

数学符号示例
==============

.. literalinclude:: ../../reStructured/__init__.py
    :language: python
    :lines: 75-83
.. autofunction:: math

其他示例
=========

.. literalinclude:: ../../reStructured/__init__.py
    :language: python
    :lines: 86-104
.. autofunction:: function_with_types_in_docstring
.. literalinclude:: ../../reStructured/__init__.py
    :language: python
    :lines: 107-117
.. autofunction:: function_with_pep484_type_annotations