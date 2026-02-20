# Utterance length feature
from tokenizer import *

def UtteranceLength(utterance: str, punctuationIncluded = False) -> int:
    tokens = tokenizeSent(utterance, PunctuationRemoved=not punctuationIncluded)
    return len(tokens)

