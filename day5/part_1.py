from day5.common import get_input


def main():
    polymer = get_input()

    reacted_polymer = react_polymer(polymer)

    print('Polymer chain after reaction:', reacted_polymer, '\nUnits in new chain:', len(reacted_polymer))


def react_polymer(polymer):
    return polymer


if __name__ == '__main__':
    main()
