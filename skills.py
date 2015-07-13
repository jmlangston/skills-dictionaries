# To work on the advanced problems, set to True
ADVANCED = False


def count_unique(input_string):    # DONE
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string as values.


    For example:

        >>> print_dict(count_unique("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time:

        >>> print_dict(count_unique("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different:

        >>> print_dict(count_unique("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}

    """

    # Jessica's pseudocode:
    # input is a string
    # split the string on spaces
    # add and count distinct words in a dictionary
    # ok to leave punctuation and capital letters

    input_words = input_string.split()

    dict_words = {}
    value = 0

    for i in range(len(input_words)):
        key = input_words[i]

        if key not in dict_words:
            dict_words[key] = value

        if key in dict_words:
            dict_words[key] += 1

    return dict_words



def find_common_items(list1, list2):    # DONE
    """Produce the set of common items in two lists.

    Given two lists, return a list of the common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    For example:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    If an item appears more than once in both lists, return it each
    time:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 1, 2, 2]

    (And the order of which has the multiples shouldn't matter, either):

        >>> sorted(find_common_items([1, 1, 2, 2], [1, 2, 3, 4]))
        [1, 1, 2, 2]

    """
    common_items = []

    for item_list1 in list1:
        for item_list2 in list2:
            if item_list1 == item_list2:
                common_items.append(item_list1)

    return common_items


def find_unique_common_items(list1, list2):    # DONE
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    Just like `find_common_items`, this should find [1, 2]:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show
    more than 1 or 2 once:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 2]

    """

    intersection = set(list1) & set(list2)

    return list(intersection)


    # Solution without using sets...
    # Jessica's pseudocode:
    # concatenate lists
    # add words to dictionary and count occurrences
    # if occurrences > 1, add to another list
    # return that list

    # concat_input_lists = list1 + list2

    # dict_items = {}
    # value = 0
    # list_common_items = []

    # for i in range(len(concat_input_lists)):
    #     key = concat_input_lists[i]

    #     if key not in dict_items:
    #         dict_items[key] = value

    #     if key in dict_items:
    #         dict_items[key] += 1

    # for key in dict_items:
    #     if dict_items[key] > 1:
    #         list_common_items.append(key)

    # return list_common_items


def get_sum_zero_pairs(input_list):    # DONE 
    """Given a list of numbers,
    return list of x,y number pair lists where x + y == 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.


    For example:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself):

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    """

    list_pairs = []

    for num in input_list:
        num_times_neg_one = num * -1
        if num_times_neg_one in input_list:
            pair_as_list = [num, num_times_neg_one]
            pair_as_list.sort()
            if pair_as_list not in list_pairs:
                list_pairs.append(pair_as_list)
            input_list.remove(num)

    return list_pairs 


def remove_duplicates(words):    # DONE
    """Given a list of words, return the list with duplicates removed
    without using a Python set.

    For example:

        >>> sorted(remove_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(remove_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

    """

    dict_words = {}
    value = 0
    list_no_duplicates = []

    for i in range(len(words)):
        key = words[i]

        if key not in dict_words:
            dict_words[key] = value

        if key in dict_words:
            dict_words[key] += 1

    for key in dict_words:
        list_no_duplicates.append(key)

    return list_no_duplicates



def encode(phrase):    # DONE
    """Given a phrase, replace all "e" characters with "p",
    replace "a" characters with "d", replace "t" characters with "o",
    and "i" characters with "u". Return the encoded string.

    For example:

        >>> encode("You are a beautiful, talented, brilliant, powerful musk ox.")
        'You drp d bpduouful, odlpnopd, brulludno, powprful musk ox.'
    """

    dict_replace = {"e": "p",
                    "a": "d",
                    "t": "o",
                    "i": "u"}

    for key in dict_replace:
        if key in phrase:
            phrase = phrase.replace(key, dict_replace[key])

    return phrase


def sort_by_word_length(words):    # DONE
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that
    word-length, and the list of words of that word length.

    For example:

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    """

    dict_words = {}

    for word in words:
        key = len(word)
        value = word

        if key not in dict_words:
            dict_words[key] = []

        dict_words[key].append(value)


    tuples = dict_words.items()

    tuples.sort()

    print tuples


def get_pirate_talk(phrase):   # DONE
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak equivalent.
    Words that cannot be translated into Pirate-speak should pass through
    unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    madam       proud beauty
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    lawyer      foul blaggart
    the         th'
    restroom    head
    my          me
    hello       avast
    is          be
    man         matey

    For example:

        >>> get_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words:

        >>> get_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """

    pirate_dict = { "sir": "matey",
                    "hotel": "fleabag inn",
                    "student": "swabbie",
                    "boy": "matey",
                    "madam": "proud beauty",
                    "professor": "foul blaggart",
                    "restaurant": "galley",
                    "your": "yer",
                    "excuse": "arr",
                    "students": "swabbies",
                    "are": "be",
                    "lawyer": "foul blaggart",
                    "the": "th'",
                    "restroom": "head",
                    "my": "me",
                    "hello": "avast",
                    "is": "be",
                    "man": "matey"
                    }


    words = phrase.split()

    for i in range(len(words)):
        if words[i] in pirate_dict:
            words[i] = pirate_dict[words[i]]

    new_phrase = " ".join(words)

    return new_phrase


# End of skills. See below for advanced problems.
# To work on them, set ADVANCED=True at the top of this file.
############################################################################


def adv_get_top_letter(input_string):
    """Given an input string, return a list of letter(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the letters in the returned
    list should be alphabetical.

    For example:
        >>> adv_get_top_letter("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:
        >>> adv_get_top_letter("Shake it off, shake it off. Shake it off, Shake it off.")
        ['f']

    Spaces do not count as letters.

    """

    return ''

def adv_alpha_sort_by_word_length(words):
    """    
    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--a number that is a word-length,
    and the list of words of that word length. In addition to ordering
    the list by word length, order each sub-list of words alphabetically.
    Now try doing it with only one call to .sort() or sorted(). What does the
    optional "key" argument for .sort() and sorted() do?

    For example:

        >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """

    return []


##############################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is just used to print dictionaries in key-alphabetical
    # order, and is only used for our documentation tests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is used only
    # for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)

if __name__ == "__main__":
    print
    import doctest
    for k, v in globals().items():
        if k[0].isalpha():
            if k.startswith('adv_') and not ADVANCED:
                continue
            a = doctest.run_docstring_examples(v, globals(), name=k)
    print "** END OF TEST OUTPUT"
    print
