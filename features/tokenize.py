"""
Author: James Stone
Date: 2/19/2026
File: tokenize.py
Purpose: The purpose of this file is to implement a simple tokenization feature using
        NLTK's built-in punkt tokenizer. It will also have a no-punctuation tokenization
        feature and a feature that tokenizes an utterance into its constituent tokens.
"""
from nltk.tokenize import PunktTokenizer


def tokenizeSents(sents:str) -> list[str]:
    detector = PunktTokenizer()
    tokens = detector.tokenize(sents.strip())
    return tokens
