import count_word_matches_function

def test_count_word_matches_function():
    assert count_word_matches_function.count_word_matches(text="The cat sat on the mat", target="cat") == 1

def test_count_word_matches_function():
    assert count_word_matches_function.count_word_matches(text="Dog dog DOG dOg", target="dog") == 4

def test_count_word_matches_function():
    assert count_word_matches_function.count_word_matches(text="Hello world", target="world") == 1

def test_count_word_matches_function():
    assert count_word_matches_function.count_word_matches(text="hello hello HELLO", target="hello") == 3

def test_count_word_matches_function():
    assert count_word_matches_function.count_word_matches(text="No matches here", target="yes" ) == 0

def test_count_word_matches_function():
    assert count_word_matches_function.count_word_matches(text="catcat cat catdog", target="cat" ) == 1

def test_count_word_matches_function():
    assert count_word_matches_function.count_word_matches(text="a a a", target="a") == 3