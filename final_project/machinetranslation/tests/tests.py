import unittest
from translator import english_to_french, french_to_english

class testEnglishToFrench(unittest.TestCase):
    def testNull(self):
        self.assertEqual(english_to_french(' '), ' ')
    def testHello(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class testFrenchToEnglish(unittest.TestCase):
    def testNull(self):
        self.assertEqual(french_to_english(' '),' ')
    def testBonjour(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
unittest.main()