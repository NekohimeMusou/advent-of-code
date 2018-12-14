from day5.common import get_input, react_polymer


def main():
    polymer = get_input()

    reacted_polymer = react_polymer(polymer)

    print('Polymer chain after reaction:', reacted_polymer,
          '\nUnits in new chain:', len(reacted_polymer))


if __name__ == '__main__':
    main()
