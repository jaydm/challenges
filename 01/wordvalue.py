from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    lineList = [line.rstrip('\n') for line in open(DICTIONARY)]

    return lineList

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    value = 0

    for chr in word:
        if chr.upper() in LETTER_SCORES:
            value += LETTER_SCORES[chr.upper()]

    return value
    

def max_word_value(words = load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_value = 0
    max_word = ''

    for word in words:
        if calc_word_value(word) > max_value:
            max_value = calc_word_value(word)
            max_word = word

    return max_word

if __name__ == "__main__":
    pass # run unittests to validate
