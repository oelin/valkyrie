from typing import Callable


def strict(callable: Callable) -> Callable:
        """
        Ensures that arguments passed to a function lie in
        accordance with its type annotations. Note that
        arguments must be passed to the decorated function
        in keyword format.


        Parameters
        ----------

        callable: Callable

                The function to be decorated.


        Returns
        -------

        callable: Callable

                The decorated function.


        Examples
        --------

        >>> @strict
            def upper(string: str) -> str:
                return string.upper()

        >>> upper(string=1234)

        TypeError: Argument "string" must be an instance of str.

        >>> upper(string='hello')

        'HELLO'
        """


        def decorated(*args, **kwargs):

                for keyword, argument in kwargs.items():
                        type = callable.__annotations__.get(keyword)

                        if not type: continue
                        if not isinstance(argument, type):
                                raise ValueError(f'Argument {keyword} must be an instance of {type}.')

                return callable(**kwargs)

        return decorated
