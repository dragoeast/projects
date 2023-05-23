def token_replace(tokens, s):
    """Replace all tokens in the string s.
    Return the transformed string.
    >>> tokens = {'$LOCATION$': 'park', '$ANIMAL$': 'dog'}
    >>> s = "Walk the $ANIMAL$ in the $LOCATION$!"
    >>> token_replace(tokens, s)
    'Walk the dog in the park!'
    """
    result_lst = []
    i, j = 0, 1
    while i < len(s):
        if s[i] != '$':
            result_lst.append(s[i])
            i += 1
            j = i + 1
        elif s[j] != '$':
            j += 1
        else:
            key = s[i:j+1]
            replacement = tokens[key]
            result_lst.append(replacement)
            i = j + 1
            j = i + 1

    return ''.join(result_lst)


def testing():
    tokens = {
    '$LOCATION$': 'park',
    '$ANIMAL$': 'dog',
    }
    result = 'Walk the dog in the park!'
    assert token_replace(tokens, s='Walk the $ANIMAL$ in the $LOCATION$!') == result, f"should be '{result}'"

    tokens = {
    '$greeting$': 'hey programmer',
    }
    result = 'his greeting is always hey programmer.'
    assert token_replace(tokens, s='his greeting is always $greeting$.') == result, f"should be '{result}'"

    tokens = {
    '$A$': 'lions',
    '$B$': 'tigers',
    '$C$': 'bears',
    }
    result = 'lionstigersbears, oh my.'
    assert token_replace(tokens, s='$A$$B$$C$, oh my.') == result, f"should be '{result}'" 

if __name__ == "__main__":
    testing()
    print("Everyting passed")
