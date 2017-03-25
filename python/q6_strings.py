# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    def donuts(count):
    try: 
        count = int(count)
        if count >= 0 and count <= 10: print ("Number of donuts:", count)
        elif count >= 11: print ("Number of donuts: many")
        else: print ("Please enter an integer.")
    except: 
        print ("Please enter an integer.")
       
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    raise NotImplementedError


def both_ends(s):
    if len(s) <= 1: print ( )
    elif len(s) >= 2: print (s[0] + s[1] + s[-2] + s[-1])
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    raise NotImplementedError


def fix_start(s):
    old = list(s)
    first_letter = old[0]
    new = list()
    for letter in old:
        if letter == first_letter: 
            letter = '*'
        new.append(letter)
    new[0] = first_letter
    print (''.join(new))
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    raise NotImplementedError


def mix_up(a, b):
    first_word = list(a)
    second_word = list(b)
    q, p = first_word[0], first_word[1]
    x, y = second_word[0], second_word[1]
    first_word[0], first_word[1] = x, y
    second_word[0], second_word[1] = q, p
    print (''.join(first_word), ''.join(second_word))
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    raise NotImplementedError


def verbing(s):
    if len(s) <= 2: print(s)
    elif len(s) >= 3 and s[-3] == 'i' and s[-2] == 'n' and s[-1] == 'g': print(s + 'ly')
    else: print (s + 'ing')
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    raise NotImplementedError


def not_bad(s):
    import re
    sentence = re.findall(r"[\w']+|[.,!?;]", s)
    x = 0
    y = 0
    z = 0
    for word in sentence:
        x = x + 1
        if word == "not": y = x
        elif word == "bad": z = x
    if z > y:
        sentence[y-1] = "good"
        del sentence[y:z]
        output = ' '.join(sentence)
        print (re.sub(r'\s([?.!"](?:\s|$))', r'\1', output))
    else:
        output = ' '.join(sentence)
        print (re.sub(r'\s([?.!"](?:\s|$))', r'\1', output))
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    raise NotImplementedError


def front_back(a, b):
    first_word = list(a)
    second_word = list(b)
    t = len(first_word) / 2
    s = len(second_word) / 2
    x = t + 0.5
    y = s + 0.5
    if int(len(first_word)) % 2 == 1 and int(len(second_word)) % 2 == 1:
        new_word = first_word[:int(x)] + second_word[:int(y)] + first_word[int(x):] + second_word[int(y):]
        print (''.join(new_word))
    elif int(len(first_word)) % 2 == 1:
        new_word = first_word[:int(x)] + second_word[:int(s)] + first_word[int(x):] + second_word[int(s):]
        print (''.join(new_word))
    elif int(len(second_word)) % 2 == 1:
        new_word = first_word[:int(t)] + second_word[:int(y)] + first_word[int(t):] + second_word[int(y):]
        print (''.join(new_word))
    else: 
        new_word = first_word[:int(t)] + second_word[:int(s)] + first_word[int(t):] + second_word[int(s):]
        print (''.join(new_word))
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    raise NotImplementedError
