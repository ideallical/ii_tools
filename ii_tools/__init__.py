import string

__all__ = ('remove_all_capitals_except_dsq')


def remove_all_capitals_except_dsq(s):
    return ''.join(
        [c for c in s if (c not in string.ascii_uppercase) or c in 'DSQ'])
