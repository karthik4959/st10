from word import WordCounter
wordcounter = WordCounter

def test_count_uppercade():
    text = "HEllo, World"
    expected_result = 3
    result = wordcounter.count_uppercase(text)
    assert result == expected_result, f"Expected: {expected_result}, but got: {result}"