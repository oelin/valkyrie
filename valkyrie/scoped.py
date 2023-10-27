"""Scoped types."""

from typing import Type
from dataclasses import dataclass


def Scoped(type: Type) -> Type:
    """Creates a scoped type."""

    class ScopedType(type):
        def __init__(self, scope: Scope, *args, **kwargs) -> None:
            
            super().__init__(*args, **kwargs)
            self.scope = scope
            
    return ScopedType


@dataclass(frozen=True)
class Scope:
    ...
