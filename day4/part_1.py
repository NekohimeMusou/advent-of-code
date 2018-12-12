import re
from datetime import datetime

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
            guard_ids.add(guard_id)

        if event_description == 'falls asleep':
            event_type = EventType.SLEEP
        elif event_description == 'wakes up':
            event_type = EventType.WAKE
        else:
            event_type = EventType.SHIFT_BEGIN

        events.append(ScheduleEvent(datetime(int(year), int(month), int(day), hour=int(hour), minute=int(minute)),
                                    guard_id, event_type))

    return tuple(sorted(guard_ids, key=int)), events


def calc_highest_total_sleep_id(sleep_per_guard):
    return max(sleep_per_guard, key=sleep_per_guard.get)


def total_sleep_per_guard(guard_ids, events):
    # Put the events into a dictionary keyed by guard ID and sorted by timestamp
    # Also get rid of the SHIFT_BEGIN events since we don't need them
    events = {g: sorted([e for e in events if e.guard_id == g and e.type is not EventType.SHIFT_BEGIN],
                        key=lambda x: x.timestamp) for g in guard_ids}

    sleep_per_guard = {}

    for guard_id, event_list in events.items():
        # See https://docs.python.org/3/library/functions.html#zip
        total_minutes = 0
        for first, second in zip(*[iter(event_list)]*2):
            # Calculate the time delta
            delta = second.timestamp - first.timestamp
            # Get the change in minutes
            total_minutes += delta.seconds / 60

        sleep_per_guard[guard_id] = total_minutes

    return sleep_per_guard


if __name__ == '__main__':
    main()
