from itertools import permutations
from string import ascii_lowercase

INPUT_PATH = 'input.txt'


def get_input(path=INPUT_PATH):
    """Get the input for day 5.

    This should all be one long string. I tested with the given input and we don't need to join
    the lines but it's just a bit less brittle this way."""
    with open(path) as f:
        return ''.join(f.readlines()).strip()


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

        if polymer == '' or old_polymer == polymer:
            return polymer


def polymer_reductions(polymer):
    return (polymer.replace(l, '').replace(l.upper(), '') for l in ascii_lowercase)


def shortest_reduced_polymer(polymer):
    return min(len(react_polymer(p)) for p in polymer_reductions(polymer))
