from Palindromo import Palindromo
import unittest

class TestPalindromo(unittest.TestCase):
    __palindromo= None #Palabra que si es palíndromo
    __palindromdont= None #Palabra que no es palíndromo

    def setUp(self) -> None:
        self.__palindromdont= Palindromo("palabra")
        self.__palindromo= Palindromo("anana")


    def testPalindromdont(self):
        self.assertFalse(self.__palindromdont.esPalindromo())

    def testPalindromo(self):
        self.assertTrue(self.__palindromo.esPalindromo())




if __name__ == '__main__':
    unittest.main()
