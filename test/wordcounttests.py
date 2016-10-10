import unittest
from word_count.count import words

class TestWordCounts(unittest.TestCase):
    """
        Counts the occurrences or characters in a word
    """

    def test_word_occurance1(self):
        self.assertDictEqual(
            {'word': 1},
            words('word'),
            msg='should count one word'
        )


if __name__ == '__main__':
    unittest.main()