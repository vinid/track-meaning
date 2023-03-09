

def is_word_in_text(text, word):
    """
    Simplest word
    :param text:
    :param word:
    :return:
    """
    return word in text.split()

def get_words_close(text, word, context_window=10):
    """
    Finds words that appear in context of a word
    :param text:
    :param word:
    :param context_window:
    :return:
    """
    split = text.split()
    idx = split.index(word)
    return " ".join(split[idx-context_window:idx+context_window])
