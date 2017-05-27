#!/usr/bin/python
# coding: utf-8
"""
A wildly inefficient version of a word unscrambler.
This is 2017 and my computer is fast so it's okay.
Let's just brute force it!
"""

import itertools
"""
1. user input

I decided to make matches case sensitive,
to avoid false positives on things like the chemical symbol "Rb"
"""
in_letters = input('Letters to scrabble: ')

with open('words.txt') as words_f:
    # 2. list of all words
    all_words = [word.strip() for word in words_f.readlines()]

    """
    3. find permutations of input letters

    We need permutations of all lengths, not just the length of the word,
    so that 'llab' will match different length words
    like 'a', 'lab', and 'ball'.
    """
    all_perms = set()
    for length in range(1, len(in_letters) + 1):
        all_perms.update(
            set(
                [
                    ''.join(perm) for perm
                    in itertools.permutations(in_letters, length)
                ]
            )
        )

    # 4. find matches and print the result
    all_matches = sorted([
        match for match
        in filter(lambda perm: perm in all_words, all_perms)
    ])
    print('Matches: \n', all_matches)


"""
Gotta go fast
░░░░░░░░░▄▄▄▄▄
░░░░░░░░▀▀▀██████▄▄▄
░░░░░░▄▄▄▄▄░░█████████▄
░░░░░▀▀▀▀█████▌░▀▐▄░▀▐█
░░░▀▀█████▄▄░▀██████▄██
░░░▀▄▄▄▄▄░░▀▀█▄▀█════█▀
░░░░░░░░▀▀▀▄░░▀▀███░▀░░░░░░▄▄
░░░░░▄███▀▀██▄████████▄░▄▀▀▀██▌
░░░██▀▄▄▄██▀▄███▀░▀▀████░░░░░▀█▄
▄▀▀▀▄██▄▀▀▌████▒▒▒▒▒▒███░░░░▌▄▄▀
▌░░░░▐▀████▐███▒▒▒▒▒▐██▌
▀▄░░▄▀░░░▀▀████▒▒▒▒▄██▀
░░▀▀░░░░░░▀▀█████████▀
░░░░░░░░▄▄██▀██████▀█
░░░░░░▄██▀░░░░░▀▀▀░░█
░░░░░▄█░░░░░░░░░░░░░▐▌
░▄▄▄▄█▌░░░░░░░░░░░░░░▀█▄▄▄▄▀▀▄
▌░░░░░▐░░░░░░░░░░░░░░░░▀▀▄▄▄▀
"""
