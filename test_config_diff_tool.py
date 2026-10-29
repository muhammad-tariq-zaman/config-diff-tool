import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import normalise, diff_configs


class TestConfigDiff(unittest.TestCase):
    def test_normalise_drops_comments_and_blanks(self):
        self.assertEqual(normalise("# c\n\n; s\nkey=1\n"), ["key=1"])

    def test_added_and_removed(self):
        added, removed, _ = diff_configs("a=1\nb=2\n", "a=1\nc=3\n")
        self.assertEqual(added, ["c=3"])
        self.assertEqual(removed, ["b=2"])

    def test_comment_only_change_is_no_diff(self):
        added, removed, _ = diff_configs("a=1\n", "# note\na=1\n")
        self.assertEqual((added, removed), ([], []))

    def test_unified_diff_mentions_change(self):
        _, _, unified = diff_configs("a=1\n", "a=2\n")
        self.assertTrue(any("a=2" in l for l in unified))


if __name__ == "__main__":
    unittest.main()
