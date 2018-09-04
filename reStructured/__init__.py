def square(a):
    """short description of the function square longish explanation: returns
    the square of a: :math:`a^2`

    :param a: an input argument
    :returns: a*a
    """
    return a * a


def example(param1, param2, param3, param4, param5):
    """描述示例

    :param param1: 第一个描述。接受一个字符串作为参数。
    :type param1: str
    :param param2: 第二个描述。接受一个数字作为参数。该值会参考 `param1` 。
    :type param2: int
    :param param3: 第三个描述。接受一个字符串元组作为参数。
    :type param3: tuple[str]
    :param param4: 第四个描述。接受数字或字符串或数字列表或字符串列表作为参数。
    :type param4: int or str or list[str] or list[int]
    :param param5: 第五个描述。接受 :py:class:`pandas.DataFrame` 作为参数。
    :type param5: :py:class:`pandas.DataFrame`
    :return: 返回值描述。返回字典。Key类型为字符串，Value类型为整数。
    :rtype: dict[str,int]
    """
    pass


def colored_box():
    """

    .. seealso::
        * :py:func:`reStructured.function_with_types_in_docstring`
        * :py:obj:`numpy.int32`

    .. warning::
        :py:obj:`numpy.nan`

        关联到第三方项目时，需要在 ``conf.py`` 中配置 ``intersphinx_mapping`` 结点。
        比如，需要连接到 `numpy` 时，需要在配置字典中增加
        ``'numpy': ('http://docs.scipy.org/doc/numpy', None)``。

    .. error::
        :py:class:`numpy.int32`

    .. todo::
        还有很多事情没做。这里需要在 ``conf.py`` 中增加 ``sphinx.ext.todo`` 扩展，
        同时设置 ``todo_include_todos=True``
    """


def code_block():
    """
    采用 literalinclude 方式包含文件中的代码段::
        .. literalinclude:: ../../reStructured/__init__.py
            :language: python
            :lines: 1-8

    采用 ``..code-block::`` 方式显示代码段。
    **..code-block:: 下面需要空一行。** ::
        .. code-block:: python

            print("Hello!")

    直接使用 ``::`` 展示代码段：::

        >>> s = 'Hello, world.'
        >>> str(s)
        'Hello, world.'

    """


def math():
    """以下内容展示数学符号使用
    .. math::

        n_{\mathrm{offset}} = \sum_{k=0}^{N-1} s_k n_k

    :math:`{\alpha > \beta}`
    """
    pass


def function_with_types_in_docstring(param1, param2):
    """包含类型描述的docstring
        支持 `PEP 484`_ 类型注释。如果属性，参数和返回类型根据 `PEP 484`_ 进行注释，
        它们不需要包含在docstring中。参见 :func:`function_with_pep484_type_annotations`

    :param param1: 这是第一个参数的描述。
    :type param1: int
    :param param2: 这是第二个参数的描述。
    :type param2: int
    :return: 返回值描述。
    :rtype: bool

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/

    .. seealso::
        :py:func:`reStructured.function_with_pep484_type_annotations`
    """
    pass


def function_with_pep484_type_annotations(param1: int, param2: str) -> bool:
    """以 `PEP 484`_ 格式撰写方法定义时，docstring中无需再次描述类型。

    :param param1: 这是第一个参数的描述。
    :param param2: 这是第二个参数的描述。
    :return: 返回值描述。

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/
    """
    pass
