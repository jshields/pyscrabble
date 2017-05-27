import sys
import itertools


def build_word_list():
    """
    open dictionary as list of words
    :returns: list of words
    :rtype: list
    """
    with open('words.txt') as words_file:
        return [word.strip() for word in words_file.readlines()]


def scrabble(input_letters, all_words):
    """
    :param str letters: letters to use to find words
    :param list words: words considered valid matches / dictionary words
    :returns: all words that match a permutation of the input
    :rtype: list
    """

    # this completely chokes on longer strings of letters,
    # which is exciting to watch
    #all_perms = set()
    #for length in range(1, len(letters) + 1):
    #    all_perms.update(
    #        set([
    #            ''.join(perm) for perm
    #            in itertools.permutations(letters, length)
    #        ])
    #    )
    #all_matches = sorted(
    #    [match for match in filter(lambda perm: perm in all_words, all_perms)]
    #)

    matches = []
    for word in all_words:
        # if each letter in the word can be found in the input
        letters_available = input_letters
        for letter in word:
            if letter in letters_available:
                # consume the letter
                letters_available = letters_available.replace(letter, '', 1)
            else:
                break
        else:
            matches.append(word)
    return matches


def interactive_mode():
    print('Starting pyscrabble interactively. Give letters, get words.')
    all_words = build_word_list()
    scrabbling = True
    while scrabbling:
        try:
            # get user input
            in_letters = input('Letters to scrabble: ')
            all_matches = scrabble(in_letters, all_words)
            print('Matches: \n', all_matches)
            input('Press Enter to scrabble again, or Ctrl+C to quit.')
        except KeyboardInterrupt:
            scrabbling = False
    else:
        print('\nThanks for scrabbling.')


if __name__ == '__main__':
    # running from command line, not being imported
    if len(sys.argv) == 1 and sys.argv[0] == __file__:
        # no letters given from command line
        interactive_mode()
    else:
        print(scrabble(sys.argv[1], build_word_list()))
