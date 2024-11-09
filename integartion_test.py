import unittest
from word import WordCounter

# Integration testing for the methods
class IntegrationTestWordCounter(unittest.TestCase):
    def test_integration(self):
        text = "Hello World"
        wc = WordCounter()  # Create an instance of WordCounter

        vowels_str = wc.get_vowels(text)  # Get the vowels from the text
        lowercase_count = wc.count_lowercase(vowels_str)  # Count the lowercase letters in the vowels string

        self.assertEqual(vowels_str, "eoo")  # Verify the vowels string
        self.assertEqual(lowercase_count, 3)  # Verify the count of lowercase letters in the vowels string

if __name__ == "__main__":
    unittest.main()