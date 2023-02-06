<div align=center>
	<img src='https://github.com/oelin/constrictor/blob/main/images/constrictor.svg' width=30%>
</div>


# Constrictor: Type Safety And Determinism For Python

[**Installation**](#) | [**Documentation**](#) | [**Examples**](#) 

Constrictor is lightweight Python library focused on improving type saftey and determinism, primarily through the use of decorators. Currently WIP. 


```py
# Perform strict type checking.

from typing import List, Any
from constrictor.decorators import strict

@strict
def head(list: List) -> Any:
	return list[0]
```
