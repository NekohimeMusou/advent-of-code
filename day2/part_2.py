from itertools import combinations

INPUT_PATH = "input.txt"
SAMPLE_DATA = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']


def main():
    lines = get_input()

    prototype_string = find_prototype_string(lines)

    print('The prototype string is:', prototype_string)


def get_input(path=INPUT_PATH):
    with open(path) as f:
        # There shouldn't be any duplicates but this will filter any out
        return set(f.readlines())


def find_prototype_string(id_list):
    """Find the two box ids that contain the prototype fabric.

    Returns the common characters between the two box IDs.

    Params:
    id_list -- a sequence containing ids to check, which should be unique strings
    """

    # combinations gives us every combination of n items from the list. Perfect! <3
    for id_1, id_2 in combinations(id_list, 2):
        mismatches = []

        for i in range(len(id_1)):
            if id_1[i] != id_2[i]:
                if mismatches:  # We already found a mismatch
                    break
                mismatches.append(i)
        else:
            # Only reached if we finish with 1 mismatch
            n = mismatches[0]
            return ''.join((id_1[0:n], id_1[n+1:len(id_1)]))

    return None


if __name__ == "__main__":
    main()
