import operator
from functools import reduce

INPUT_PATH = "input.txt"
TARGETS = (2, 3)


def main():
    with open(INPUT_PATH) as f:
        # Read in the file and apply the duplicate check function with a list comprehension
        duplicate_counts = [check_duplicate_letters(line, TARGETS) for line in f]

    # Flatten the list of tuples into a list of integers
    # See: https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists
    duplicate_counts = [n for sublist in duplicate_counts for n in sublist]

    # Count the number of times 2 and 3 appear in the list
    duplicate_counts = [duplicate_counts.count(target) for target in TARGETS]

    # Multiply the two numbers together to get the checksum
    # I'm only doing it this way because I wrote everything else to support arbitrary targets too
    checksum = reduce(operator.mul, duplicate_counts)

    print("Checksum:", checksum)


# Checks whether a string has any letters that occur exactly 2 or 3 times. The optional targets parameter
# let you provide different values if you want. Returns a tuple containing 2 if a letter appeared exactly twice,
# 3 if a letter appeared exactly thrice, neither, or both.
def check_duplicate_letters(haystack, targets=TARGETS):
    # Use a set comprehension to get the set of letters in the string
    unique_items = {x for x in haystack}

    # For each unique letter, count the number of times it occurs in the string
    frequencies = {x: haystack.count(x) for x in unique_items}

    return tuple({x for x in frequencies.values() if x in targets})


if __name__ == "__main__":
    main()
