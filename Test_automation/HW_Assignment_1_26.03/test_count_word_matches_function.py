import count_word_matches_function
import pytest


@pytest.mark.parametrize("text,target,expected",[
    ("The cat sat on the mat","cat",1),
    ("Dog dog DOG dOg","dog",4),
    ("Hello world","world",1),
    ("hello hello HELLO","hello", 3),
    ("No matches here","yes",0),
    ("catcat cat catdog","cat",1),
    ("a a a","a",3)
])


def test_count_word_matches_function_1(text,target,expected):
    assert count_word_matches_function.count_word_matches(text,target) == expected

@pytest.fixture(scope = "function")
def sample_data():
    return [("None","word",TypeError),
            ("hello world","None",TypeError),
            (123,"word",TypeError),
            ("hello world",456,TypeError),
            (["hello", "world"],"world",TypeError),
            ("hello world",["world"],TypeError)
            ]


def test_input_none(sample_data):
    with pytest.raises(TypeError,match == "Please insert a string value"):
    assert count_word_matches_function.count_word_matches(sample_data) == expected

def test_input_integer(sample_data):
    assert count_word_matches_function.count_word_matches(sample_data) == expected

def test_input_list(sample_data):
    assert count_word_matches_function.count_word_matches(sample_data) == expected