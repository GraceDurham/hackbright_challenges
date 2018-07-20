
def find_longest_word(words):
    """Return longest word in list of words"""

    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)

    return longest
       
    

print find_longest_word(["hi", "hello"])