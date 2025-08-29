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