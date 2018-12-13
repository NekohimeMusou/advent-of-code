import unittest
from datetime import datetime

from day4.common import process_events, nap_intervals_per_guard
from day4.events import EventType, ScheduleEvent
from day4.part_1 import calc_highest_total_sleep_id, calc_sleepiest_minute
from day4.part_2 import calc_guard_with_sleepiest_minute


class TestPart1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sample_input = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up"""

        cls.sample_events = \
            [ScheduleEvent(datetime(year=1518, month=11, day=1, hour=0, minute=0), 10, EventType.SHIFT_BEGIN),
             ScheduleEvent(datetime(year=1518, month=11, day=1, hour=0, minute=5), 10, EventType.SLEEP),
             ScheduleEvent(datetime(year=1518, month=11, day=1, hour=0, minute=25), 10, EventType.WAKE),
             ScheduleEvent(datetime(year=1518, month=11, day=1, hour=0, minute=30), 10, EventType.SLEEP),
             ScheduleEvent(datetime(year=1518, month=11, day=1, hour=0, minute=55), 10, EventType.WAKE),
             ScheduleEvent(datetime(year=1518, month=11, day=1, hour=23, minute=58), 99, EventType.SHIFT_BEGIN),
             ScheduleEvent(datetime(year=1518, month=11, day=2, hour=0, minute=40), 99, EventType.SLEEP),
             ScheduleEvent(datetime(year=1518, month=11, day=2, hour=0, minute=50), 99, EventType.WAKE),
             ScheduleEvent(datetime(year=1518, month=11, day=3, hour=0, minute=5), 10, EventType.SHIFT_BEGIN),
             ScheduleEvent(datetime(year=1518, month=11, day=3, hour=0, minute=24), 10, EventType.SLEEP),
             ScheduleEvent(datetime(year=1518, month=11, day=3, hour=0, minute=29), 10, EventType.WAKE),
             ScheduleEvent(datetime(year=1518, month=11, day=4, hour=0, minute=2), 99, EventType.SHIFT_BEGIN),
             ScheduleEvent(datetime(year=1518, month=11, day=4, hour=0, minute=36), 99, EventType.SLEEP),
             ScheduleEvent(datetime(year=1518, month=11, day=4, hour=0, minute=46), 99, EventType.WAKE),
             ScheduleEvent(datetime(year=1518, month=11, day=5, hour=0, minute=3), 99, EventType.SHIFT_BEGIN),
             ScheduleEvent(datetime(year=1518, month=11, day=5, hour=0, minute=45), 99, EventType.SLEEP),
             ScheduleEvent(datetime(year=1518, month=11, day=5, hour=0, minute=55), 99, EventType.WAKE)]

        cls.guard_ids = {10, 99}

        cls.nap_intervals_by_guard = {10: ((5, 25), (30, 55), (24, 29)),
                                      99: ((40, 50), (36, 46), (45, 55))}

        cls.sleepiest = {1: {'id': 10, 'minute': 24},
                         2: {'id': 99, 'minute': 45}}

        cls.method_2_result = calc_guard_with_sleepiest_minute(cls.nap_intervals_by_guard)

    def test_event_parsing(self):
        _, test_events = process_events(self.sample_input)

        self.assertEqual(self.sample_events, test_events)

    def test_guard_id_list(self):
        guard_ids, _ = process_events(self.sample_input)

        self.assertEqual(self.guard_ids, guard_ids)

    def test_nap_intervals(self):
        self.assertEqual(self.nap_intervals_by_guard, nap_intervals_per_guard(self.guard_ids, self.sample_events))

    def test_sleepiest_guard_method_1(self):
        self.assertEqual(self.sleepiest[1]['id'], calc_highest_total_sleep_id(self.nap_intervals_by_guard))

    def test_sleepiest_minute_method_1(self):
        self.assertEqual(self.sleepiest[1]['minute'], calc_sleepiest_minute(self.nap_intervals_by_guard[10]))

    def test_sleepiest_guard_method_2(self):
        self.assertEqual(self.sleepiest[2]['id'], self.method_2_result[0])

    def test_sleepiest_minute_method_2(self):
        self.assertEqual(self.sleepiest[2]['minute'], self.method_2_result[1])
