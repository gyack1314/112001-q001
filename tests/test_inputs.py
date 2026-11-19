import json
from pathlib import Path
import unittest


class InputShapeTest(unittest.TestCase):
    def test_fixture_records_have_source_and_period(self):
        path = Path(__file__).parents[1] / "data" / "reports.json"
        rows = json.loads(path.read_text(encoding="utf-8"))
        self.assertTrue(rows)
        self.assertTrue(all(row["source"] and row["period"] for row in rows))


if __name__ == "__main__":
    unittest.main()
