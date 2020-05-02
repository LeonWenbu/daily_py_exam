def reversWrods(sentence):
    # sentence = "i have a dog"
    # print(sentence)
    words = sentence.split(' ')
    # print(words)

    words.reverse()
    # print(words)
    return " ".join(words)

# main
sentence = "i have a dog, and a cat"
print(reversWrods(sentence))
