from itertools import permutations

from day5.common import get_input


def main():
    polymer = get_input()

    reacted_polymer = react_polymer(polymer)

    print('Polymer chain after reaction:', reacted_polymer,
          '\nUnits in new chain:', len(reacted_polymer))


def react_polymer(polymer):
    """React the polymer with a brute force method.

    Just iterate the possible character pairs and remove them, then check whether the
    new string is the same as the old one."""

    pairs = [''.join(s) for s in permutations('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 2)
             if s[0].casefold() == s[1].casefold() and s[0].islower() != s[1].islower()]

    while True:
        old_polymer = polymer

        for pair in pairs:
            polymer = polymer.replace(pair, '')
        if old_polymer == '' or old_polymer == polymer:
            return polymer


if __name__ == '__main__':
    main()
