from itertools import cycle

INPUT_PATH = "../input.txt"


def main():
    lines = get_input()

    final_freq = calc_final_frequency(lines)

    first_rep = find_repetition(lines)

    print("Ending frequency: {0}\nFirst frequency repeated twice: {1}".format(final_freq, first_rep))


def get_input(path=INPUT_PATH):
    with open(path) as f:
        return [int(x) for x in f.readlines()]


def calc_final_frequency(delta_list, initial_freq=0):
    current_freq = initial_freq

    for delta in delta_list:
        current_freq += delta

    return current_freq


def find_repetition(delta_list, initial_freq=0):
    # If I needed to find the nth repetition instead of the 2nd I would use a dict
    freqs_tested = {initial_freq}
    current_freq = initial_freq

    for delta in cycle(delta_list):
        current_freq += delta

        if current_freq in freqs_tested:
            # If it's already in the set, this is the second time we've seen it
            return current_freq
        else:
            freqs_tested.add(current_freq)


if __name__ == "__main__":
    main()
