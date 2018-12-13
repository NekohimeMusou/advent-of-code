from intervaltree import IntervalTree

from day4.common import process_input


def main():
    nap_intervals = process_input()

    sleepiest_guard, sleepiest_minute = calc_guard_with_sleepiest_minute(nap_intervals)

    print('Sleepiest guard (Method 2):', sleepiest_guard, '\nSleepiest minute (Method 2):', sleepiest_minute,
          '\nFinal result (Method 2):', sleepiest_guard * sleepiest_minute)


def calc_guard_with_sleepiest_minute(naps):
    """Find the guard who slept the most during a single minute and return both the guard ID and the minute.

    Params:

    naps - Dictionary of interval lists with guard IDs as keys
    """
    # This is one of the most absurd things I've ever done so here's an example of what the output would look like
    # for the sample data:
    # Input:  {10: ((5, 25), (30, 55), (24, 29)), 99: ((40, 50), (36, 46), (45, 55))}
    # Output: {10: (24, 2), 99: (45, 3)}
    sleepiest_minutes = {guard_id: max(((x, len(it[x])) for x in range(60)), key=lambda x: x[1])
                         for guard_id, it in {guard_id: IntervalTree.from_tuples(i_list)
                                              for guard_id, i_list in naps.items()}.items()}

    sleepiest_guard = max(sleepiest_minutes, key=lambda x: sleepiest_minutes.get(x)[1])
    sleepiest_minute = sleepiest_minutes[sleepiest_guard][0]

    return sleepiest_guard, sleepiest_minute


if __name__ == '__main__':
    main()
