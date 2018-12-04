INPUT_PATH = "day-1/input.txt"


def main():
    lines = get_input()


def get_input(path=INPUT_PATH):
    with open(path) as f:
        return f.readlines()


if __name__ == "__main__":
    main()
