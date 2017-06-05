"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""

import random

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    unique_words_count = {}

    # used .split() method to separate string into list of words
    # for loop used to iterate over each word in list
    for word in phrase.split():

        # adds new words to dict as keys with value of 1
        if word not in unique_words_count:
            unique_words_count[word] = 1

        # increases count of existing words in dict by 1
        else:
            unique_words_count[word] += 1

    return unique_words_count



def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon.

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If melon name does not exist, return 'No price found'.

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """

    # created melon dict to associate melon names and prices
    melon_price_dict = {

        "Watermelon": 2.95,
        "Cantaloupe": 2.50,
        "Musk": 3.25,
        "Christmas": 14.25,

    }

    # conditional checks to see if user input exists in dict
    if melon_name in melon_price_dict:
        # returns melon's price/value from dict
        return melon_price_dict[melon_name]

    # function will return 'No price found' if user input not in dict
    else:
        return 'No price found'


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

        >>> word_length_sorted(["porcupine", "ok"])
        [(2, ['ok']), (9, ['porcupine'])]
    """

    words_and_lengths = {}

    for word in words:

        if len(word) not in words_and_lengths:
            words_and_lengths[len(word)] = [word]

        else:
            words_and_lengths[len(word)] += [word]

    words_and_lengths = sorted(words_and_lengths.items())

    for pair in words_and_lengths:
        pair[1].sort()

    return words_and_lengths


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    pirate_dict = {
        "sir": "matey",
        "hotel": "fleabag inn",
        "student": "swabbie",
        "man": "matey",
        "professor": "foul blaggart",
        "restaurant": "galley",
        "your": "yer",
        "excuse": "arr",
        "students": "swabbies",
        "are": "be",
        "restroom": "head",
        "my": "me",
        "is": "be",
    }

    # split string input into list of strings to find words as keys in dict
    words = phrase.split()

    # for loop will iterate over all words in list of words
    for word in words:

        # conditional checks to see if word exists in dict
        if word in pirate_dict:
            # loop will replace each word with a pirate translation if possible
            phrase = phrase.replace(word, pirate_dict[word])

    return phrase





def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    # this is as far as I could get on this problem
    # the first for loop creates a dictionary - keys are every word in input list
    # values are lists of words that start with the last letter of the key
    # rest of code consistently finds the first and second word
    # but once the second for loop starts the output does not satisfy the doctest
    # I know the problem is that I don't have proper conditionals set up
    # in my second for loop to select words in the correct order
    # but I don't know how to fix it


    chain = {}

    for name in names:

        if name not in chain:
            chain[name] = []

        name_index = len(name) - 1

        name_ends_with = name[name_index]

        for word in names:

            next_starts_with = word[0]

            if next_starts_with == name_ends_with:
                chain[name].append(word)

    first_word = names[0]

    output_words = [first_word]

    try:
        another_word = random.choice(chain[first_word])

        output_words.append(another_word)

    except:
        pass

    for key, value in chain.items():

        if key not in output_words:

            try:
                next_word = random.choice(value)
                output_words.append(next_word)

            except:
                break

    return output_words

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
