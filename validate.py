"""With this module you can get the type of element, check if it is
a list or a string, etc."""

from typing import Union, Any

def _type(obj: Any) -> str:

    """Returns the type of objects"""

    type_of_object = str(type(obj)).split("'")[1]
    return type_of_object


def is_string(*args: str) -> bool:

    """Validates attribute(s) and redurned True if it is string"""

    if (len(args) != 0) and all([_type(i) == "str" for i in args]):
        return True
    else:
        return False


def is_list(x: list) -> bool:

    """Validates attribute x and return True if it is list"""

    if _type(x) == "list":
        return True
    else:
        return False


def is_list_or_tuple(x: Union[list, tuple]) -> bool:

    """Validates attribute x and return True if it is list or tuple"""

    if _type(x) in ("list", "tuple"):
        return True
    else:
        return False


def is_string_or_none(*args: str) -> bool:

    """Validates attribute(s) and redurned True if it is string or
None"""

    if ((len(args) != 0) and all([True if (_type(i) in ("NoneType", "str"))
        else False for i in args])):
        return True
    else:
        return False


def is_string_list_tuple_or_none(x: Union[str, list, tuple]) -> bool:

    """Validates attribute x and return True if it is string, list,
tuple or None"""

    if _type(x) in ("NoneType", "str", "list", "tuple"):
        return True
    else:
        return False
