import unittest
from funwithwords import FunWithWords


class TestFunWithWords(unittest.TestCase):
    def test_is_palindrom_uppercase(self):
        self.assertEqual(FunWithWords("WaAx").is_palindrom(), False)

    def test_is_palindrom_phrase(self):
        temp = FunWithWords("Rats live on no evil star")
        self.assertEqual(temp.is_palindrom(),True)

    def test_is_palindrom_special_character(self):
        temp = FunWithWords("A to kawa kota?")
        self.assertEqual(temp.is_palindrom(), True)

    def test_is_anagram_uppercase(self):
        temp = FunWithWords("Debit card")
        self.assertEqual(temp.is_anagram("Bad credit"), True)

    def test_is_anagram_special_characters(self):
        temp = FunWithWords("Norwid")
        self.assertEqual(temp.is_anagram("On drwi!!!"), True)


if __name__ == '__main__':
    unittest.main()
