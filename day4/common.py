import re
from datetime import datetime

from day4.events import EventType, ScheduleEvent

INPUT_PATH = "input.txt"


def process_input():
    # process_events needs a big ol' string
    input_lines = '\n'.join(get_input())

    guard_ids, events = process_events(input_lines)

    return nap_intervals_per_guard(guard_ids, events)


def get_input(path=INPUT_PATH):
    """Get the input from the file and return it as a list of lines.

    Reading each line into a list and sorting lexicographically does the trick.
    """
    with open(path) as f:
        return sorted(f.readlines())


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
