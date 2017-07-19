def parse_url(path: str, params: dict = None) -> str:
    """
    This function is an url parser that simplifies URL writing
    by automatically formatting a simple string (with given
    parameters) to a regular expression.

    :param path: URL path.
    :param params: URL parameters.
    :return: "Djangofied" url.
    """

    if params:
        for key, value in params:
            if value == 'numbers':
                path += '/(?P<{}>[0-9]+)'.format(key)
            elif value == 'chars':
                path += '/(?P<{}>[a-Z]+)'.format(key)
            elif value == '*':
                path += '/(?P<{}>.*)'.format(key)
    return path
