<div align=center>
        <img src='https://github.com/oelin/valary/blob/main/images/valary.svg' width=40%>
</div>

# Valkyrie

Validated types for Python.

## Installation

```bash
pip install git+https://github.com/oelin/valkyrie
```

## Usage

```python
from valkyrie import validate

@validate
class User:
    username: str
    password: str

    def validate(self) -> None:
        """Validates the user."""

        assert isinstance(self.username, str)
        assert isinstance(self.password, str)
```
