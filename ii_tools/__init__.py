"""ideallical tools."""

import string

from six import string_types

__all__ = ('remove_all_capitals_except_dsq', )


def remove_all_capitals_except_dsq(string_value):
    """
    Remove all capitals except the letters D, S & Q.

    :param str string_value: the string to filter
    :return: the filtered string
    :rtype: str
    :raises ValueError: if the string_value is not a string_type
    """
    if isinstance(string_value, string_types):
        return ''.join(
            [c for c in string_value if (
                c not in string.ascii_uppercase) or c in 'DSQ'])
    else:
        raise ValueError
