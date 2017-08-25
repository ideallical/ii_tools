"""ideallical tools."""

import string

from six import string_types

__all__ = ('remove_all_capitals_except_dsq')


def remove_all_capitals_except_dsq(s):
    """
    Remove all capitals except the letters D, S & Q.

    :param str s: The string to filter
    :return: the filtered string
    :raises: ValueError: if the s is not a string_type
    """
    if isinstance(s, string_types):
        return ''.join(
            [c for c in s if (c not in string.ascii_uppercase) or c in 'DSQ'])
    else:
        raise ValueError
