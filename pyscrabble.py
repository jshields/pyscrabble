import itertools

# 1. get user input
in_letters = input('Letters to scrabble: ')
with open('words.txt') as words_file:
    # 2. open dictionary as list of words
    all_words = [word.strip() for word in words_file.readlines()]
    # 3. get all permutations of input
    all_perms = set()
    for length in range(1, len(in_letters) + 1):
        all_perms.update(
            set([
                ''.join(perm) for perm
                in itertools.permutations(in_letters, length)
            ])
        )
    # 4. find and print all words that match a permutation of the input
    all_matches = sorted(
        [match for match in filter(lambda perm: perm in all_words, all_perms)]
    )
    print('Matches: \n', all_matches)
