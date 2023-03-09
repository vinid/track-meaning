import string
from nltk.corpus import stopwords


def text_remove_punct(mess: str):
    """
    Simple punctuation remover. Also removes new line and return car characters
    :param mess:
    :return:
    """
    for punct in string.punctuation:
        mess = mess.replace(punct, "")
    mess = mess.lower().replace("\n", " ").replace("\r", " ")
    return " ".join(mess.split())

def text_process(mess: str):
    """
    English stopword removal
    :param mess:
    :return:
    """
    nostop = ' '.join([word for word in mess.split() if word not in stopwords.words('english')])
    return nostop



