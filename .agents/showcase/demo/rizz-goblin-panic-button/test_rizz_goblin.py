import unittest

from rizz_goblin import report


class GoblinReportTests(unittest.TestCase):
    def test_one_signal_leaves_vibes_intact(self):
        self.assertEqual(report(["cold-pizza"]), "Goblin alert: VIBES INTACT (1 chaos points)")

    def test_combined_signals_trigger_touch_grass(self):
        self.assertEqual(
            report(["cursed-tabs", "keyboard-crumbs"]),
            "Goblin alert: TOUCH GRASS (5 chaos points)",
        )
