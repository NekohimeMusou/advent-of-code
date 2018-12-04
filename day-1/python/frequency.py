INPUT_PATH = "../input.txt"


def main():
    lines = get_input()

    final_freq = calc_final_frequency(lines)

    print("Ending frequency: {0}".format(final_freq))


def get_input(path=INPUT_PATH):
    with open(path) as f:
        return [int(x) for x in f.readlines()]


def calc_final_frequency(delta_list, initial_freq=0):
    current_freq = initial_freq

    for delta in delta_list:
        current_freq += delta

    return current_freq


if __name__ == "__main__":
    main()
