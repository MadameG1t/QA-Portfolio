import count_word_matches_function
import pytest


@pytest.mark.parametrize("text,target,expected",[
    ("text="The cat sat on the mat"","target="cat"","Expected`1`"),
    ("text="Dog dog DOG dOg"","target="dog"","Expected `4`"),
    ("text="Hello world"", "target="world"","Expected `1`"),
    ("text="hello hello HELLO"", "target="hello"","Expected `3`"),
    ("text="No matches here"", "target="yes"","Expected `0`"),
    ("text="catcat cat catdog"", "target="cat"","Expected `1`"),
    ("text="a a a"", "target="a"","Expected `3`")
])

def test_count_word_matches_function1(text,target,expected):
    assert count_word_matches_function.count_word_matches(text,target) == expected

'''
def test_count_word_matches_function1():
    assert count_word_matches_function.count_word_matches(text="The cat sat on the mat", target="cat") == 1

def test_count_word_matches_function2():
    assert count_word_matches_function.count_word_matches(text="Dog dog DOG dOg", target="dog") == 4

def test_count_word_matches_function3():
    assert count_word_matches_function.count_word_matches(text="Hello world", target="world") == 1

def test_count_word_matches_function4():
    assert count_word_matches_function.count_word_matches(text="hello hello HELLO", target="hello") == 3

def test_count_word_matches_function5():
    assert count_word_matches_function.count_word_matches(text="No matches here", target="yes" ) == 0

def test_count_word_matches_function6():
    assert count_word_matches_function.count_word_matches(text="catcat cat catdog", target="cat" ) == 1

def test_count_word_matches_function7():
    assert count_word_matches_function.count_word_matches(text="a a a", target="a") == 3

'''