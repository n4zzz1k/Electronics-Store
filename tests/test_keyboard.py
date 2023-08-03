from unittest import TestCase
from src.keyboard import Keyboard

class TestKeyboard(TestCase):
    def test_change_lang(self):
        kb = Keyboard('Dark Project KD87A', 9600, 0.05, 5)
        self.assertEqual(repr(kb), "Keyboard('Dark Project KD87A', 9600, 0.05, 5)")

        self.assertEqual(str(kb.language), "EN")

        kb.change_lang()
        self.assertEqual(str(kb.language), "RU")

        # Сделали RU -> EN -> RU
        kb.change_lang().change_lang()
        self.assertEqual(str(kb.language), "RU")

        kb.language = 'CH'  # Теперь это должно работать
        self.assertEqual(str(kb.language), "CH")

    def test_init(self):
        kb = Keyboard('Dark Project KD87A', 9600, 0.05, 5)
        self.assertEqual(repr(kb), "Keyboard('Dark Project KD87A', 9600, 0.05, 5)")
        self.assertEqual(kb.price, 9600)
        self.assertEqual(kb.discount, 0.05)
        self.assertEqual(kb.quantity, 5)

    def test_repr(self):
        kb = Keyboard('Dark Project KD87A', 9600, 0.05, 5)
        self.assertEqual(repr(kb), "Keyboard('Dark Project KD87A', 9600, 0.05, 5)")
        self.assertEqual(repr(kb), str(kb))  # Можно также проверить, что repr(kb) равно str(kb))
