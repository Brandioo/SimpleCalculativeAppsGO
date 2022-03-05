from CountVowels import vowel_count

def test_count_vowels():
    assert vowel_count("Celebration") == 5
    assert vowel_count("Palm") == 1
    assert vowel_count("Prediction") == 4
    assert vowel_count("") == 0
    assert vowel_count(1) == 0
    assert vowel_count([]) == 0
    assert vowel_count("&") == 0
