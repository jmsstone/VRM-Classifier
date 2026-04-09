# Utterance length feature
from tokenizer import *

def UtteranceLength(tokens:list[str]) -> int:
    return len(removePunctuation(tokens))

