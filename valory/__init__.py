"""Valory."""

from dataclasses import dataclass
from functools import wraps
from typing import Any, Type


def validate(type: Type) -> Type:
    """Returns a validated type."""

    type = dataclass(frozen=True)(type)  # Immutability.
    
    @wraps(type)
    def validate(*args, **kwargs) -> Any:
        
        instance = type(*args, **kwargs)
        instance.validate()

        return instance
    return validate
