# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
import unittest
from CasinoSlot import Game, payout, STAKE

class SlotTests(unittest.TestCase):
    def test_triple(self):
        self.assertEqual(payout(("BAR", "BAR", "BAR")), 50)
    def test_pair(self):
        self.assertEqual(payout(("BAR", "BAR", "SEVEN")), 20)
    def test_all_different(self):
        self.assertEqual(payout(("BAR", "CHERRY", "SEVEN")), 0)
    def test_balance(self):
        game = Game()
        game.spin(("BAR", "BAR", "BAR"))
        self.assertEqual(game.credits, 100 - STAKE + 50)
    def test_no_negative_credit(self):
        with self.assertRaises(ValueError):
            Game(credits=0).spin()
    def test_invalid_reels(self):
        with self.assertRaises(ValueError):
            payout(("BAR", "BAR", "UNKNOWN"))

if __name__ == "__main__":
    unittest.main()
