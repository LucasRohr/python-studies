from unittest import TestCase, main
from capitalize import capitalize

class CapitalizeTest(TestCase):

    def test_one_word(self):
        text = 'paitu'
        result = capitalize(text)

        self.assertEquals(result, 'Paitu')

    def test_multiple_words(self):
        text = 'paitu rocks'
        result = capitalize(text)

        self.assertEquals(result, 'Paitu Rocks')

if __name__ == '__main__':
    main()