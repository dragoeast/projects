def token_transform(tokens, s):
    """Return the transformed version of string s,
    where all tokens(included the nested ones too) replaced.
    >>> tokens = {\
        '$LOCATION$': '$ANIMAL$ park',\
        '$ANIMAL$': 'dog',\
    }
    >>> token_transform(tokens, 'Walk the $ANIMAL$ in the $LOCATION$!')
    'Walk the dog in the dog park!'
    """
    result_lst = []
    i, j = 0, 1
    while i < len(s):
        if s[i] != "$":
            result_lst.append(s[i])
            i += 1
            j = i + 1
        elif s[j] != "$":
            j += 1
        else:
            key = s[i:j+1]
            value = tokens[key]
            evaluated_value = token_transform(tokens, s=value)
            tokens[key] = evaluated_value #this will act as a memoization
            result_lst.append(evaluated_value)
            i = j + 1
            j = i + 1

    return ''.join(result_lst)

def testing():
    tokens = {
    '$B$': "epicly $C$",
    '$A$': "pretty $B$ problem $D$",
    '$D$': "we have",
    '$C$': "clever",
    }
    print(f"tokens before the memoization")
    for token_item in tokens.items():
        print(token_item)

    result = 'What a pretty epicly clever problem we have here!'
    assert token_transform(tokens, s="What a $A$ here!") == result, f"should be '{result}'"
    print(f"tokens after the memoization")
    for token_item in tokens.items():
        print(token_item)

if __name__ == "__main__":
    testing()
    print("="*20)
    print("Everything passed")
