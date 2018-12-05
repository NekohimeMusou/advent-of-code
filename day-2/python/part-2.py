INPUT_PATH = "../input.txt"


def main():
    with open(INPUT_PATH) as f:
        lines = f.readlines()

    prototype_ids = find_prototype_ids(lines)


def find_prototype_ids(id_list):
    """Find the two box ids that contain the prototype fabric.

    Returns a tuple containing the two strings.

    Params:
    id_list -- a sequence containing ids to check, which should be strings
    """

    return None, None


if __name__ == "__main__":
    main()
