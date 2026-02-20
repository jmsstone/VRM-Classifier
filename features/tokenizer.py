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


def tokenizeSents(sents:str) -> list[str]:
    detector = PunktTokenizer()
    tokens = detector.tokenize(sents.strip())
    return tokens

def tokenizeSent(sent:str, PunctuationRemoved=False) -> list[str]:
    tokenizer = StanfordTokenizer()
    tokens = tokenizer.tokenize(sent)
    
    if PunctuationRemoved:
        punctuation = [".",",",":","?",";","!"]
        for punc in punctuation:
            tokens = [x for x in tokens if x != punc]
    return tokens

