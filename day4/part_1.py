import re
from datetime import datetime
import intervaltree

from day4.common import get_input
from day4.events import EventType, ScheduleEvent


def main():
    # process_events wants everything as one string
    lines = '\n'.join(get_input())

    guard_ids, events = process_events(lines)


# Event: (datetime, guard_num, event_type)
# Just get the lines as an entire string
def process_events(lines):
    event_regex = re.compile(r'^\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\] (.+)', re.MULTILINE)
    guard_regex = re.compile(r'Guard #(\d+)')

    guard_id = None

    events = []
    guard_ids = set()

    for year, month, day, hour, minute, event_description in event_regex.findall(lines):
        id_match = guard_regex.match(event_description)

        if id_match:
            guard_id = id_match.group(1)
            guard_ids.add(int(guard_id))

        if event_description == 'falls asleep':
            event_type = EventType.SLEEP
        elif event_description == 'wakes up':
            event_type = EventType.WAKE
        else:
            event_type = EventType.SHIFT_BEGIN

        events.append(ScheduleEvent(datetime(int(year), int(month), int(day), hour=int(hour), minute=int(minute)),
                                    int(guard_id), event_type))

    return tuple(sorted(guard_ids)), events


def calc_highest_total_sleep_id(sleep_per_guard):
    return max(sleep_per_guard, key=sleep_per_guard.get)


def nap_intervals_per_guard(guard_ids, events):
    # Put the events into a dictionary keyed by guard ID and sorted by timestamp
    # Also get rid of the SHIFT_BEGIN events since we don't need them
    events = {g: sorted([e for e in events if e.guard_id == g and e.type is not EventType.SHIFT_BEGIN],
                        key=lambda x: x.timestamp) for g in guard_ids}

    intervals_per_guard = {}

    for guard_id, event_list in events.items():
        nap_list = []
        for first, second in zip(*[iter(event_list)]*2):
            nap_list.append((first.timestamp.minute, second.timestamp.minute))

        intervals_per_guard[guard_id] = tuple(nap_list)

    return intervals_per_guard


def total_sleep_per_guard(naps_per_guard):
    pass


if __name__ == '__main__':
    main()
