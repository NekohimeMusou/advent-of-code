import re
from datetime import datetime
from intervaltree import IntervalTree

from day4.common import get_input
from day4.events import EventType, ScheduleEvent


def main():
    # process_events needs a big ol' string
    input_lines = '\n'.join(get_input())

    guard_ids, events = process_events(input_lines)

    nap_intervals = nap_intervals_per_guard(guard_ids, events)

    sleepiest_guard = calc_highest_total_sleep_id(nap_intervals)

    sleepiest_minute = calc_sleepiest_minute(nap_intervals[sleepiest_guard])

    print('Sleepiest guard:', sleepiest_guard, '\nSleepiest minute:', sleepiest_minute,
          '\nFinal result:', sleepiest_guard * sleepiest_minute)


def process_events(lines):
    """Process the sorted input into a set of guard IDs and a list of events.

    I spent like half a day trying to figure out how to do it with one unholy regex and failing graphically but
    this seems more comprehensible to me anyway. See events.py for the ScheduleEvent class and the EventType enum.

    Params:

    lines - A STRING containing the SORTED input, one event per line.
    """
    event_regex = re.compile(r'^\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\] (.+)', re.MULTILINE)
    guard_regex = re.compile(r'Guard #(\d+)')

    # The loop needs to remember the last guard ID it found so it knows who wake/sleep events should belong to
    guard_id = None

    events = []
    guard_ids = set()

    # findall gets every match from the string and returns a list of lists containing only the matching groups
    # The MULTILINE flag is important
    for year, month, day, hour, minute, event_description in event_regex.findall(lines):
        # Use the single-match function to see if there's a guard ID (implying it's a SHIFT_BEGIN)
        id_match = guard_regex.match(event_description)

        if id_match:
            guard_id = int(id_match.group(1))
            guard_ids.add(guard_id)
            event_type = EventType.SHIFT_BEGIN
        elif event_description == 'wakes up':
            event_type = EventType.WAKE
        else:
            event_type = EventType.SLEEP

        events.append(ScheduleEvent(datetime(int(year), int(month), int(day), hour=int(hour), minute=int(minute)),
                                    guard_id, event_type))

    return guard_ids, events


def calc_highest_total_sleep_id(sleep_per_guard):
    """Find the ID of the guard who slept the most in total.

    Params:

    sleep_per_guard - dict-like object with the guard IDs as keys and a list of nap intervals as values
    """
    # For each guard ID, find the length of each interval and sum them up to get that guard's total minutes slept
    # (using a dict comprehension to store them in a dict)
    sleep_per_guard = {guard_id: sum([i[1] - i[0] for i in intervals]) for guard_id, intervals in
                       sleep_per_guard.items()}

    # Find the highest value in the dict and get its key
    return max(sleep_per_guard, key=sleep_per_guard.get)


def nap_intervals_per_guard(guard_ids, events):
    """Parse the event log into tuples that represent the start and end of each nap.

    Params:

    guard_ids - The set of unique guard IDs in the input.
    events - Iterable of ScheduleEvents in the log.
    """
    # Put the events into a dictionary keyed by guard ID with each guard's event list sorted by timestamp
    # We don't need the SHIFT_BEGIN events anymore at all, so get rid of them
    events = {g: sorted([e for e in events if e.guard_id == g and e.type is not EventType.SHIFT_BEGIN],
                        key=lambda x: x.timestamp) for g in guard_ids}

    intervals_per_guard = {}

    for guard_id, event_list in events.items():
        nap_list = []

        # Cluster the event list into groups of 2
        # See https://docs.python.org/3/library/functions.html#zip
        for first, second in zip(*[iter(event_list)] * 2):
            nap_list.append((first.timestamp.minute, second.timestamp.minute))

        intervals_per_guard[guard_id] = tuple(nap_list)

    return intervals_per_guard


def calc_sleepiest_minute(interval_list):
    """Find the minute during which the sleepiest guard slept the most.

    Params:

    interval_list - The list of nap intervals, expressed as tuples: (start, end)
    """
    # Initialize an interval tree from our nap intervals
    it = IntervalTree.from_tuples(interval_list)

    # The endpoints are minutes within [12:00AM-1:00AM)
    # So just walk the tree from 0-59 and find the point where the most intervals lie
    graph = [len(it[x]) for x in range(60)]

    # The array indices just so happen to correspond to individual minutes exactly
    return graph.index(max(graph))


if __name__ == '__main__':
    main()
