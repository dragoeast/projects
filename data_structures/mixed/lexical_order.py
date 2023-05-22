def lexical_order(word_1, word_2, alphabet):
    """Return True if word_1 should appear before word_2 
    in lexical order according to the alphabet.
    Otherwise return False.
    >>> english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    >>> lexical_order(word_1='apple', word_2='apply', alphabet=english_alphabet)
    True
    >>> lexical_order(word_1='app', word_2='apply', alphabet=english_alphabet)
    True
    >>> lexical_order(word_1='banana', word_2='apple', alphabet=english_alphabet)
    False
    """
    alph_dict= get_alphabetical_dict(alphabet)

    return compare(word_1, word_2, alph_dict)

def get_alphabetical_dict(alphabet):
    """Return a dictionary whrere:
    key: the character in the alphabet
    value: the index of the character in the alphabet
    >>> alphabet = 'abc'
    >>> get_alphabetical_dict(alphabet)
    {'a': 0, 'b': 1, 'c': 2}
    """
    alph_dict = {}

    for index, char in enumerate(alphabet):
        alph_dict[char] = index

    return alph_dict

def compare(word_1, word_2, alph_dict):
    """Return True if word_1 should appear before word_2 
    in lexical order according to the alphabet.
    Otherwise return False.
    >>> _alph_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
    >>> compare(word_1='abc', word_2='abd', alph_dict=_alph_dict)
    True
    >>> compare(word_1='ab', word_2='abc', alph_dict=_alph_dict)
    True
    >>> compare(word_1='abcd', word_2='abcc', alph_dict=_alph_dict)
    False
    """
    i, j = 0, 0
    while i < len(word_1) and j < len(word_2):
        char_1, char_2 = word_1[i], word_2[j]
        if char_1 == char_2:
            i, j = i+1, j+1
        else:
            return alph_dict[char_1] < alph_dict[char_2]
    
    if i >= len(word_1):
        return True
    else:
        return False
