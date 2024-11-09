from word import WordCounter

wordcounter = WordCounter()

# Test case for the uppercase count function

def test_count_uppercase():
    text = "HEllo, World" # In put for the test
    expected_result = 3 # Expected out put
    result = wordcounter.count_uppercase(text) # Result for the test
    assert result == expected_result, f"Expected: {expected_result}, but got: {result}"