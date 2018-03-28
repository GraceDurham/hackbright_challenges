

def hbhas_unique(word):
    """Returns True if that given word contains unique characters. Returns False if given word does not contain unique characters"""

    unique_char = set(word)
    #remove duplicates with set and save to variable
    # print len(unique_char)
    # print len(word)

    return len(unique_char) == len(word)
    #return True if length of set is equal to original word bc words contains unique characters. Return false if length is not equal to words bc does not contain unique characters

print hbhas_unique("Moonday")


def has_unique(words):

    have_seen = set()

    for word in words:
        if word not in have_seen:
            have_seen.add(word)
            print have_seen
        elif word in have_seen:
            #if word already in the set than the words are not unique characters return false
            return False
    return True

print has_unique("bob")