<div align=center>
        <img src='https://github.com/oelin/valary/blob/main/images/valary.svg' width=40%>
</div>

# Valary

Valary implements validated typing for Python. A validated type is an *immutable* type for which every instance satisfies a predicate $P(\cdot)$. 

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
from constrictor import Validated

ValidatedUser = Validated(User, user_validator) 
```

Every instance of `ValidatedUser` satisfies `user_validator` by definition.
