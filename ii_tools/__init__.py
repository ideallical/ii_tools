"""ideallical tools."""

import string

from six import string_types

__all__ = ('remove_all_capitals_except_dsq')


def remove_all_capitals_except_dsq(string_value):
    """
    Remove all capitals except the letters D, S & Q.

    :param str string_value: The string to filter
    :return: the filtered string
    :raises: ValueError: if the s is not a string_type
    """
    if isinstance(string_value, string_types):
        return ''.join(
            [c for c in string_value if (
                c not in string.ascii_uppercase) or c in 'DSQ'])
    else:
        raise ValueError
