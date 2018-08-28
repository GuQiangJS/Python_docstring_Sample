def example(param1, param2, param3, param4, param5):
    """描述示例

    Args:
        param1 (str): 第一个描述。接受一个字符串作为参数。
        param2 (int): 第二个描述。接受一个数字作为参数。
        param3 (tuple[str]): 第三个描述。接受一个字符串元组作为参数。
        param4 (int or str or list[str] or list[int]):
            第四个描述。接受数字或字符串或数字列表或字符串列表作为参数。
        param5 (:py:class:`pandas.DataFrame`):
            第五个描述。接受 :py:class:`pandas.DataFrame` 作为参数。

    Returns:
        dict[str,int]: 返回值描述。返回字典。Key类型为字符串，Value类型为整数。
    """
    pass


def function_with_types_in_docstring(param1, param2):
    """包含类型描述的docstring

    支持 `PEP 484`_ 类型注释。如果属性，参数和返回类型根据 `PEP 484`_ 进行注释，
    它们不需要包含在docstring中。

    Args:
        param1(int): 这是第一个参数的描述。
        param2(str): 这是第二个参数的描述。

    Returns:
        bool: True if successful, False otherwise.

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/

    See Also:
        :py:func:`Napoleon.function_with_pep484_type_annotations`

    """
    pass


def function_with_pep484_type_annotations(param1: int, param2: str) -> bool:
    """符合 `PEP 484`_ 所支持的類型。

    :param param1: 这是第一个参数的描述。
    :param param2: 这是第二个参数的描述。
    :return: 返回值描述。
    """
    pass


def example_generator(n):
    """Generators have a ``Yields`` section instead of a ``Returns`` section.

    Args:
        n (int): The upper limit of the range to generate, from 0 to `n` - 1.

    Yields:
        int: The next number in the range of 0 to `n` - 1.

    Examples:
        Examples should be written in doctest format, and should illustrate how
        to use the function.

        >>> print([i for i in example_generator(4)])
        [0, 1, 2, 3]

    """
    for i in range(n):
        yield i


def example_generator_code_block(n):
    """Generators have a ``Yields`` section instead of a ``Returns`` section.

    Args:
        n (int): The upper limit of the range to generate, from 0 to `n` - 1.

    Yields:
        int: The next number in the range of 0 to `n` - 1.

    Examples:
        Examples should be written in doctest format, and should illustrate how
        to use the function.

        .. code-block:: python

            >>> print([i for i in example_generator(4)])
            [0, 1, 2, 3]

    """
    for i in range(n):
        yield i
