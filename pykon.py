"""Pykon is a module for creating constant and publicly unchangeable data."""


from typing import Any, Union


class PykonError(BaseException):
    """A custom exception for the Pykon type."""
    __slots__: frozenset[str] = frozenset({'message'})

    def __new__(cls: type["PykonError"], message: Union[str, None], /) -> "PykonError":
        if not isinstance(message, str): raise TypeError(f"'{message}' must have type 'str'")
        else: return super(PykonError, cls).__new__(cls)

    def __init__(self: "PykonError", message: Union[str, None], /) -> None:
        self.message = message
        super().__init__(self.message)


class Pykon(object):
    """Allow for the construction of a Pykon type."""
    __slots__: frozenset[str] = frozenset({})

    def __new__(cls: type["Pykon"], kind: Union[type[Any], None], data: Union[Any, None]) -> Union["Pykon", PykonError]:
        if type(kind) is not type:
            cls.kind: Union[type[Any], None] = None
            cls.data: Union[Any, None] = None
            return PykonError(f"'{kind}' must have type 'type'")
        elif type(data) is not kind:
            cls.kind: Union[type[Any], None] = None
            cls.data: Union[Any, None] = None
            return PykonError(f"'{data}' must have type '{kind.__name__}'")
        else:
            cls.kind = kind
            cls.data = data
            return super(Pykon, cls).__new__(cls)

    @classmethod
    def __modify__(cls: type["Pykon"], data: Any, /) -> Union["Pykon", PykonError]:
        return cls.__new__(cls, cls.kind, data)
