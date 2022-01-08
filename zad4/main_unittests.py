import unittest
import main
from mockito import when, mock, unstub


class MainUnitTests(unittest.TestCase):
    mock_FunClass = mock(main.FunClass())
    mock_NotFunClass = mock(main.NotFunClass())
    when(mock_FunClass).what_is_my_tau_mark().thenReturn(4)
    when(mock_FunClass).get_random_popular_game().thenReturn("Dota 2")
    when(mock_NotFunClass).return_Fun_Class_or_None().thenReturn(mock_FunClass)
    when(mock_NotFunClass).get_random_number(1, 5).thenReturn(3)

    def test_fun_class_is_your_name_popular(self):
        when(self.mock_FunClass).is_your_name_popular("Janusz").thenReturn(True)
        self.assertTrue(self.mock_FunClass.is_your_name_popular("Janusz"))

    def test_what_is_my_tau_mark(self):
        mark = self.mock_FunClass.what_is_my_tau_mark()
        self.assertGreaterEqual(mark, 3)

    def test_get_random_popular_game(self):
        popular_game = self.mock_FunClass.get_random_popular_game()
        self.assertIn(popular_game, ["Dota 2", "League of Legends", "CS:GO"])

    def test_get_pi_with_selected_length(self):
        when(self.mock_NotFunClass).get_pi_with_selected_length(10).thenReturn(3.141592653589793)
        self.assertEqual(self.mock_NotFunClass.get_pi_with_selected_length(10), 3.141592653589793)

    def test_return_Fun_Class(self):
        maybe_class = self.mock_NotFunClass.return_Fun_Class_or_None()
        self.assertIsNot(maybe_class, None)

    def test_get_random_number(self):
        fake_random = self.mock_NotFunClass.get_random_number(1, 5)
        self.assertEqual(fake_random, 3)


if __name__ == '__main__':
    unittest.main()