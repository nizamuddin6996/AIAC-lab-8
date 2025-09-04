import unittest
from tas3 import is_sentence_palindrome

class TestIsSentencePalindrome(unittest.TestCase):
    def test_simple_palindrome(self):
        self.assertTrue(is_sentence_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_sentence_palindrome("Madam In Eden, I'm Adam"))
        self.assertTrue(is_sentence_palindrome("No lemon, no melon"))
        self.assertTrue(is_sentence_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(is_sentence_palindrome("Eva, can I see bees in a cave?"))
        self.assertTrue(is_sentence_palindrome("Able was I, I saw Elba"))
        self.assertTrue(is_sentence_palindrome("Step on no pets"))
        self.assertTrue(is_sentence_palindrome("Never odd or even"))
        self.assertTrue(is_sentence_palindrome("Red roses run no risk, sir, on Nurse's order."))
        self.assertTrue(is_sentence_palindrome("Go hang a salami, I'm a lasagna hog."))

    def test_non_palindrome(self):
        self.assertFalse(is_sentence_palindrome("This is not a palindrome"))
        self.assertFalse(is_sentence_palindrome("Hello, world!"))
        self.assertFalse(is_sentence_palindrome("Palindrome"))
        self.assertFalse(is_sentence_palindrome("Python programming"))
        self.assertFalse(is_sentence_palindrome("OpenAI is awesome"))

    def test_empty_and_single_character(self):
        self.assertTrue(is_sentence_palindrome(""))
        self.assertTrue(is_sentence_palindrome("a"))
        self.assertTrue(is_sentence_palindrome("Z"))

    def test_palindrome_with_numbers(self):
        self.assertTrue(is_sentence_palindrome("12321"))
        self.assertTrue(is_sentence_palindrome("1 2 3 2 1"))
        self.assertTrue(is_sentence_palindrome("12, 3-21"))
        self.assertFalse(is_sentence_palindrome("12345"))

    def test_palindrome_with_mixed_case_and_punctuation(self):
        self.assertTrue(is_sentence_palindrome("Madam, in Eden, I'm Adam."))
        self.assertTrue(is_sentence_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(is_sentence_palindrome("Yo, Banana Boy!"))
        self.assertTrue(is_sentence_palindrome("Sir, I demand, I am a maid named Iris."))

if __name__ == "__main__":
    unittest.main()
