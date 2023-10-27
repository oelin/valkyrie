"""Contextual validation."""

from typing import Type, Optional


def Contextual(type: Type) -> Type:
    """Creates a contextual type."""

    class ContextualType(type):

        def __init__(self, *args, context: Optional = None, **kwargs) -> None:
            super().__init__(*args, **kwargs)

            self.context = context
            
    return ContextualType
