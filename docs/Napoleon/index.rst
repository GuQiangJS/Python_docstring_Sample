Google风格示例
---------------------

Google的风格基本与reStructured相似，支持所有reStructured的标签，
只是为了提高代码的简洁性做了部分调整。

`Example Google Style Python Docstrings`_

`Napoleon - Marching toward legible docstrings`_

1. 使用前需要安装扩展 ``$ pip install sphinxcontrib-napoleon``

2. 在 ``conf.py`` 文件中增加使用扩展 ``sphinxcontrib.napoleon``::

    # Add autodoc and napoleon to the extensions list
    extensions = ['sphinx.ext.autodoc', 'sphinxcontrib.napoleon']

.. _Napoleon - Marching toward legible docstrings:
    https://sphinxcontrib-napoleon.readthedocs.io/en/latest/

.. _Example Google Style Python Docstrings:
    https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html#example-google

谷歌风格::

    def func(arg1, arg2):
        """Summary line.

        Extended description of function.

        Args:
            arg1 (int): Description of arg1
            arg2 (str): Description of arg2

        Returns:
            bool: Description of return value

        """
        return True


NumPy风格::


    def func(arg1, arg2):
        """Summary line.

        Extended description of function.

        Parameters
        ----------
        arg1 : int
            Description of arg1
        arg2 : str
            Description of arg2

        Returns
        -------
        bool
            Description of return value

        """
        return True


示例
=====

.. py:module:: Napoleon

.. literalinclude:: ../../Napoleon/__init__.py
    :language: python
    :lines: 1-15

.. autofunction:: example

特别说明
=========

示例文档需要写成 `doctest` 的风格::

    Examples:
        Examples should be written in doctest format, and should illustrate how
        to use the function.

        >>> print([i for i in example_generator(4)])
        [0, 1, 2, 3]
