"""Valory."""

from typing import Any
from dataclasses import dataclass as dc
from functools import wraps


def dataclass(cls) -> dc:
    """Create a validated dataclass.

    Parameters
    ----------

    cls - The unvalidated class.

    Returns
    -------

    dataclass - The validated dataclass.

    Example
    -------

    >>> @dataclass
    ... class User:
    ...     username: str
    ...     password: str
    ...   
    ...     def validate(self) -> None:
    ...         assert isinstance(self.username, str)
    ...         assert isinstance(self.password, str)
    """

    cls = dc(frozen=True)(cls)  # Immutability.
    
    @wraps(cls)
    def dataclass(*args, **kwargs) -> cls:
        
        instance = cls(*args, **kwargs)
        instance.validate()

        return instance
    return dataclass
