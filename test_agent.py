import unittest
from agent import recommend_events


class EventTests(unittest.TestCase):
    def test_matching_event_ranks_first_and_does_not_book(self):
        events = [{"id": "1", "name": "Jazz", "city": "Chennai", "tags": ["music"]}, {"id": "2", "name": "Other", "city": "Delhi", "tags": []}]
        result = recommend_events({"city": "Chennai", "interests": ["music"]}, events)
        self.assertEqual(result[0]["event_id"], "1")
        self.assertFalse(result[0]["booking_completed"])


if __name__ == "__main__":
    unittest.main()
