import count_word_matches_function


def test_count_word_matches_function():
    assert count_word_matches_function.count_word_matches(text="The cat sat on the mat", target="cat") == 1