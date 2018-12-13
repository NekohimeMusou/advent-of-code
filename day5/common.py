INPUT_PATH = 'input.txt'


def get_input(path=INPUT_PATH):
    """Get the input for day 5.

    This should all be one long string. I tested with the given input and we don't need to join
    the lines but it's just a bit less brittle this way."""
    with open(path) as f:
        return ''.join(f.readlines())
