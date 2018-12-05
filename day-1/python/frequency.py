from itertools import cycle

INPUT_PATH = "../input.txt"


def main():
    lines = get_input()

    final_freq = calc_final_frequency(lines)

    first_rep = find_repetition(lines)

    print("Ending frequency: {0}\nFirst frequency repeated twice: {1}".format(final_freq, first_rep))


# Open the input file and convert each line to a number.
# int() strips whitespace and understands the + symbol
def get_input(path=INPUT_PATH):
    with open(path) as f:
        # This here's a list comprehension
        return [int(x) for x in f.readlines()]


# Calculate the final frequency after all changes in the list.
# Since our starting frequency is known and the operations are transitive
# we can just sum the array for this
def calc_final_frequency(delta_list, initial_freq=0):
    return sum(delta_list, initial_freq)


def find_repetition(delta_list, initial_freq=0):
    # If I needed to find the nth repetition instead of the 2nd I would use a dict
    freqs_tested = {initial_freq}
    current_freq = initial_freq

    # itertools.cycle gives us a generator that works like an infinitely-repeating list
    # This won't actually loop forever since we return when we find our target
    for delta in cycle(delta_list):
        current_freq += delta

        if current_freq in freqs_tested:
            # If it's already in the set, this is the second time we've seen it
            return current_freq
        else:
            freqs_tested.add(current_freq)


def time():
    import timeit

    reps = 1000
    output = timeit.timeit('main()', globals=globals(), number=reps)
    print(output / reps)


if __name__ == "__main__":
    main()
