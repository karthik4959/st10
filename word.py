import re
class WordCounter:
    def count_uppercase(self, text):
        return sum(1 for char in text if char.isupper())
