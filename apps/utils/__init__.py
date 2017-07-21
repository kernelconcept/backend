from enum import Enum, auto


class TYPES(Enum):
    NUMBERS = auto()
    CHARS = auto()
    ALL = auto()  # but not /


def parse_url(path: str = '^/', params: dict = {}) -> str:
    """
    This function is an url parser that simplifies URL writing
    by automatically formatting a simple string (with given
    parameters) to a regular expression.

    :param path: URL path.
    :param params: URL parameters.
    :return: "Djangofied" url.
    """

    last_char = str[-1:]
    first = '' if last_char == '/' else '/'

    for key, value in params:
        if value is TYPES.NUMBERS:
            path += '{}(?P<{}>[0-9]+)'.format(first, key)
        elif value is TYPES.CHARS:
            path += '{}(?P<{}>[A-z]+)'.format(first, key)
        elif value is TYPES.ALL:
            path += '{}(?P<{}>.*)'.format(first, key)
        else:
            path += '{}(?P<{}>{})'.format(first, key, value)

    return path
