
def decode(s):
    """Decode a string."""


    word = ""

    i = 0

    while i < len(s):

        num_to_skip = int(s[i])
        print num_to_skip

        i = i + num_to_skip + 1

        word = word + s[i]
        print word

        i = i + 1
        print i

    return word

print decode("0h1ae2bcy")