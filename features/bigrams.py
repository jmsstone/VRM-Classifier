from tokenizer import *

def getBigrams(tokens:list[str]) -> list[list[str]]:
    bigrams = []
    for index in range(len(tokens)-1):
        bigrams.append([tokens[index],tokens[index+1]])
    return bigrams

if __name__ == "__main__":
    sent = "I like to walk my dog but, he isn't here."
    tokens = tokenizeSent(sent)
    bigrams = getBigrams(tokens)
    print(bigrams)

