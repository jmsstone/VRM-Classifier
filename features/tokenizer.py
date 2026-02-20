"""
Author: James Stone
Date: 2/19/2026
File: tokenize.py
Purpose: The purpose of this file is to implement a simple tokenization feature using
    NLTK's built-in punkt tokenizer. It will also have a no-punctuation tokenization
    feature and a feature that tokenizes an utterance into its constituent tokens.
"""
from nltk.tokenize import PunktTokenizer
from nltk.tokenize.stanford import StanfordTokenizer


"""
    TokenizeSents() - The purpose of this function is to return a list of utterances. 
        It uses the standard PunktTokenizer but I plan on reworking this to be trained
        off our original dataset to allow for more apt sentence tokenization.
"""
def tokenizeSents(sents:str) -> list[str]:
    # initializing the Punkt Tokenizer
    detector = PunktTokenizer()

    # stripping sentences of extra white space and tokenizing
    tokens = detector.tokenize(sents.strip())
    return tokens

"""
    removePunctuation() - This functions purpose is to take in a list of tokens and remove
        punctuation from them. This is needed when we are counting only the words in an
        utterance and also when were making bigrams.
"""
def removePunctuation(tokens: list[str]) -> list[str]:
    # punctuation list
    punctuation = [".",",",":","?",";","!"]

    for punc in punctuation:
        # list comprehension: if your not a punctuation mark you get added
        tokens = [x for x in tokens if x != punc]
    return tokens

"""
    tokenizeSent() - The purpose of this function is to provide a standard tokenizer
        that is used through out the model. It also has functionality to return a
        no punctuation version automatically.
"""
def tokenizeSent(sent:str, PunctuationRemoved=False) -> list[str]:
    # initalizing stanford tokenizer
    # make sure you have a JDK here and that you have the stanford POST tagger downloaded
    # also make sure that it has been added to your CLASS_PATH environment variable
    tokenizer = StanfordTokenizer()
    tokens = tokenizer.tokenize(sent)
    
    if PunctuationRemoved:
        tokens = removePunctuation(tokens)
    return tokens
