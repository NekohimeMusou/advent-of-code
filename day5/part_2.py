from day5.common import get_input, shortest_reduced_polymer


def main():
    polymer = get_input()

    shortest_length = shortest_reduced_polymer(polymer)

    print('Shortest possible length:', shortest_length)


if __name__ == '__main__':
    main()
