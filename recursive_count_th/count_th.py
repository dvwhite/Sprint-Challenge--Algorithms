'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
#import ipdb


def count_th(word):
    # 'th' is a substring, so split the word into
    # substrings until you reach the base case

    # ipdb.set_trace()
    # Base case
    if len(word) < 2:
        return 0
    # Recursive case
    # If it matches, increment the count
    if word[:2] == 'th':
        return count_th(word[1:]) + 1
    # Otherwise, keep looking for matches
    else:
        return count_th(word[1:])


# Manual testing
print(count_th("athatha"))
