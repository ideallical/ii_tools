import pytest
from ii_tools import remove_all_capitals_except_dsq


@pytest.mark.parametrize('test_input,expected', [
    ('', ''),
    ('Hello World', 'ello orld'),
    ('Lorem ipsum DunsimQ', 'orem ipsum DunsimQ'),
])
def test_remove_all_capitals_except_dsq(test_input, expected):
    """Test that function works as expected."""
    assert remove_all_capitals_except_dsq(test_input) == expected


@pytest.mark.parametrize('test_input', [None, {}, [], object(), 1])
def test_remove_all_capitals_except_dsq_value_errors(test_input):
    """Test that function raises ValueError for non-string types."""
    with pytest.raises(ValueError):
        remove_all_capitals_except_dsq(test_input)
