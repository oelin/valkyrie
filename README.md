<div align=center>
        <img src='https://github.com/oelin/constrictor/blob/main/images/constrictor.svg' width=40%>
</div>

# Valance: Validated Typing for Python

![License](https://img.shields.io/badge/license-MIT-blue.svg)

[**Features**](#features) | [**Getting Started**](#getting-started) | [**Examples**](https://github.com/oelin/constrictor/tree/main/examples)

Valance implements validated typing for Python. A validated type is an *immutable* type for which every instance satisfies a predicate $P(\cdot)$. 

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

Introduction
------------

Validated typing is a functional data validation method that relies on immutability. Suppose we have a type $\mathbf{T}$.


## Installation

You can 


Introduction
------------

 in Constrictor are your trusty allies for enforcing data validation and maintaining code cleanliness. They bring determinism to your data structures, ensuring that objects are correctly formed from the moment of creation. Say goodbye to the hassle of manually validating input data and hello to code that's not only robust but also elegant. With Constrictor, you can define your data structures and attach validation rules to them, so every instance adheres to visible, well-defined criteria. This means cleaner functions, fewer validation checks, and code that's easier to read and maintain. Let Constrictor do the heavy lifting for you, so you can focus on what matters.

Features
--------

* **✅ Correctness:** Eliminate inconsistent data using validated types.
  
* **🔄 Predictability:** Prevent your code from entering opaque states.

* **🧩 Modularity:** Write validated types once; use them everywhere.
  
* **🔮 Clarity:** Streamline your code by abstracting validation boilerplate.
  
* **⚡ Productivity:** Debug 10x faster by minimizing implicit assumptions.

Getting Started
---------------

### Installation

First, install Constrictor using `pip`:

pip install constrictor


### Creating Validated Types

To begin, let's say you have a data structure like a `User` class and you want to ensure it always follows specific rules. Here's how you can create a validated type using Constrictor:

```python
from dataclasses import dataclass
from constrictor import Validated

@dataclass(frozen=True)
class User:
    username: str
    password: str
    age: int
```

Now, let's define a validation function for the `User` class. This function will enforce rules for the `User` type, such as the age range and data types:

```python
def UserValidator(user: User) -> User:
    assert isinstance(user, User)
    assert isinstance(user.username, str)
    assert isinstance(user.password, str)
    assert isinstance(user.age, int)

    assert 13 <= user.age <= 100  # Ensure age is within a valid range
    return user
```

With the `User` class and the `UserValidator` function in place, you can create a `ValidatedUser` type using Constrictor:

```python
ValidatedUser = Validated(User, UserValidator)
```

### Using Validated Types

Now, you have a `ValidatedUser` type that ensures the correctness of `User` instances. Here's how you can use it in a function:

```python
def greet_user(user: ValidatedUser) -> str:
    """Greets the user by their username."""

    assert isinstance(user, ValidatedUser)  # Ensures the input is a ValidatedUser

    return f"Hello, {user.username}!"
```

```python
user = ValidatedUser(username="john_doe", password="secret", age=25)
```

```python
greet_user(user)  # Hello, john_doe!
```

By using `ValidatedUser` as the parameter type for `greet_user`, you can be confident that the input is correctly formed, and the function can operate without needing additional validation checks. Constrictor simplifies your code and enhances code clarity. That's all there is to it 😄👌.
