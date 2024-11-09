import re

class WordCounter:
    """
    A class to perform various word and character counts on a given string.
    """

    def count_uppercase(self, text):
        """
        Count the total number of uppercase letters in the given string.

        :param text: The input string to be analyzed.
        :return: The number of uppercase letters in the string.
        """
        return sum(1 for char in text if char.isupper())

    def count_lowercase(self, text):
        """
        Count the total number of lowercase letters in the given string.

        :param text: The input string to be analyzed.
        :return: The number of lowercase letters in the string.
        """
        return sum(1 for char in text if char.islower())

    def count_vowels(self, text):
        """
        Count the total number of vowels in the given string.

        :param text: The input string to be analyzed.
        :return: The number of vowels in the string.
        """
        vowels = 'aeiouAEIOU'
        return sum(1 for char in text if char in vowels)

    def get_vowels(self, text):
        """
        Return the vowels in the given string as a new string.

        :param text: The input string to be analyzed.
        :return: A string containing all the vowels from the input string.
        """
        vowels = 'aeiouAEIOU'
        return ''.join(char for char in text if char in vowels)

    def count_total_chars(self, text):
        """
        Count the total number of characters in the given string, including spaces and special characters.

        :param text: The input string to be analyzed.
        :return: The total number of characters in the string.
        """
        return len(text)

    def count_total_words(self, text):
        """
        Count the total number of words in the given string.

        :param text: The input string to be analyzed.
        :return: The total number of words in the string.
        """
        words = re.findall(r'\b\w+\b', text)
        return len(words)
