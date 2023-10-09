<div align=center>
        <img src='https://github.com/oelin/valary/blob/main/images/valary.svg' width=40%>
</div>

# Valkyrie

Valkyrie implements validated typing for Python. A validated type is an immutable type that *shall not be instantiated* unless certain criteria are met.

## Installation

```bash
pip install git+https://github.com/oelin/valkyrie
```

## Usage

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    username: str
    password: str
```

```python
def user_validator(user: User) -> bool:
    """Validates a User."""

    assert isinstance(user.username, str)
    assert isinstance(user.password, str)
    assert len(user.username) < 256

    return True
```

```python
from valkyrie import Validated

ValidatedUser = Validated(User, user_validator) 
```
