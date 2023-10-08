"""Validated types."""

from typing import Callable, Type


Validator = Callable


def Validated(type: Type, validator: Validator) -> Type:
    """Creates a validated type."""

    assert isinstance(type, Type)
    assert isinstance(validator, Validator)

    class ValidatedType(type):
        def __init__(self, *args, **kwargs) -> None:

            super().__init__(*args, **kwargs)
            assert validator(self)

    return ValidatedType
