# Valory

Validated types for Python.

Installation
------------

```sh
pip install git+https://github.com/oelin/valory
```

Usage
-----

```python
from valory import dataclass

@dataclass
class User:
    username: str
    password: str

    def validate(self):
        assert isinstance(self.username, str)
        assert isinstance(self.password, str)
```

```python
user = User('Alice', 1234)  # Throws an exception.
```
