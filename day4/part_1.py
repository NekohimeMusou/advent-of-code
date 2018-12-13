from intervaltree import IntervalTree

from day4.common import process_input


def main():
    nap_intervals = process_input()

    sleepiest_guard = calc_highest_total_sleep_id(nap_intervals)

    sleepiest_minute = calc_sleepiest_minute(nap_intervals[sleepiest_guard])

    print('Sleepiest guard (Method 1):', sleepiest_guard, '\nSleepiest minute (Method 1):', sleepiest_minute,
          '\nFinal result (Method 1):', sleepiest_guard * sleepiest_minute)


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
