"""Pykon is a module for allowing constant and publicly immutable data."""


from typing import Any, Union


class PykonError(BaseException):
    """A custom exception for the Pykon type."""
    __slots__: frozenset[str] = frozenset({'message'})

    def __new__(cls: type["PykonError"], message: str, /) -> "PykonError":
        if not isinstance(message, str):
            raise TypeError(f"'{message}' must have type 'str'")
        else:
            return super(PykonError, cls).__new__(cls)

    def __init__(self: "PykonError", message: Union[str, None], /) -> None:
        self.message = message
        super().__init__(self.message)


class Pykon(object):
    """Allow for the construction of a Pykon type."""
    __slots__: frozenset[str] = frozenset({})

    def __new__(cls: type["Pykon"], kind: type[Any], data: Any) -> Union["Pykon", PykonError]:
        if not isinstance(kind, type):
            cls.error: PykonError = PykonError(f"'{kind}' must have type 'type'")
            return super(Pykon, cls).__new__(cls)
        elif not isinstance(data, kind):
            cls.error: PykonError = PykonError(f"'{data}' must have type '{kind.__name__}'")
            return super(Pykon, cls).__new__(cls)
        else:
            cls.kind = kind
            cls.data = data
            return super(Pykon, cls).__new__(cls)

    @classmethod
    def __modify__(cls: type["Pykon"], data: Any, /) -> Union[None, PykonError]:
        """Allow for the modification of data without modifying its type."""
        if not isinstance(data, cls.kind):
            return PykonError(f"'{data}' must have type '{cls.kind.__name__}'")
        else:
            cls.data = data
            return None
