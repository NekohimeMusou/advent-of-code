INPUT_PATH = "input.txt"


def get_input(path=INPUT_PATH):
    """Get the input from the file and return it as a list of lines.

    Reading each line into a list and sorting lexicographically does the trick.
    """
    with open(path) as f:
        return sorted(f.readlines())
