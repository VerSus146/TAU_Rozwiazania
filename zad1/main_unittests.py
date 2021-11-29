import unittest
import main


class MainUnitTests(unittest.TestCase):
    def test_Add_Zero(self):
        self.assertEqual(main.add_numbers(1, 0), 1)

    def test_Add_Positive(self):
        self.assertEqual(main.add_numbers(1, 1), 2)

    def test_Add_Negative(self):
        self.assertEqual(main.add_numbers(1, -1), 0)

    def test_Add_Float(self):
        self.assertEqual(main.add_numbers(1, 1.5), 2.5)

    def test_Join_Strings(self):
        self.assertEqual(main.join_strings("Unit", "Test"), "Unit Test")

    def test_Alphabet_Show_First_3(self):
        self.assertEqual(main.show_alphabet(3), "ABC")

    def test_Alphabet_Show_All_But_Last_3(self):
        self.assertEqual(main.show_alphabet(-3), "ABCDEFGHIJKLMNOPQRSTUVW")

    def test_Show_Alphabet_Based_On_Add_Numbers(self):
        self.assertEqual(main.show_alphabet(main.add_numbers(1, 5)), "ABCDEF")

    def test_Get_Country_From_Language(self):
        self.assertEqual(main.language_dictionary("Polish"), "Poland")

    def test_Get_Language_From_Country(self):
        self.assertEqual(main.language_dictionary("Germany"), "German")


if __name__ == '__main__':
    unittest.main()