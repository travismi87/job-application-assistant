import re


def camel_to_snake_case(name: str) -> str:
    """
    Convert a camelCase string to snake_case.
    """
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()


def snake_to_camel_case(name: str) -> str:
    """
    Convert a snake_case string to camelCase.
    """
    components = name.split("_")
    return components[0] + "".join(x.title() for x in components[1:])
