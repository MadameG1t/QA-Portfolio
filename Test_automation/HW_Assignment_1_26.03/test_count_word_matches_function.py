from nis import match

from count_word_matches_function import count_word_matches
import pytest


@pytest.mark.parametrize("text,target,expected",[
    ("The cat sat on the mat","cat",1),
    ("Dog dog DOG dOg","dog",4),
    ("Hello world","world",1),
    ("hello hello HELLO","hello", 3),
    ("No matches here","yes",0),
    ("catcat cat catdog","cat",1),
    ("a a a","a",3),
    ("", "word", 0),
    ("hello world", "", 0),
    ("", "", 0),
    ("hello  world", "world", 1),
    (" cat ", "cat", 1),
    ("cat,dog cat", "cat", 1),
    ("x y z", "x", 1),
])


def test_count_word_matches_function(text,target,expected):
    assert count_word_matches(text,target) == expected


@pytest.fixture(params=[
 (None, "word"),  # None as text
 ("hello world", None),  # None as target
 (123, "word"),  # Integer as text
 ("hello world", 456),  # Integer as target
 (["hello", "world"], "world"),  # List as text
 ("hello world", ["world"])

 ])

def invalid_input_case(request):
    return request.param

def test_count_word_matches_invalid_input(invalid_input_case):
    text,target = invalid_input_case
    if not isinstance(text, str):
        expected = f"text must be a string, got {type(text).__name__}"
    else:
        expected = f"target must be a string, got {type(target).__name__}"

    with pytest.raises(TypeError, match=expected):
        count_word_matches(text, target)
