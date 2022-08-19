''' Unit test for Final Project, English - French, French to English '''
import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    ''' Test class for English to French translation '''
    def test1(self):
        ''' Test translation from English to French, no input '''
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('The World'), 'Le Monde')
        self.assertIsNotNone(english_to_french, None)

class TestFrenchToEnglish(unittest.TestCase):
    ''' Test class for French to English translation '''
    def test1(self):
        ''' Test translation from French to English, no input '''
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Le Monde'), 'The World')
        self.assertIsNotNone(french_to_english, None)

unittest.main()
