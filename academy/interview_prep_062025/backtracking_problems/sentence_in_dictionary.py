def sentence_in_dictionary(sentence, dictionary):
    print(f"sentence : {sentence} , dictionary : {dictionary}")

    # lower case the sentence and strip any spaces
    newSentence =sentence.replace(' ','').lower()
    print(f"lower case sentence : {newSentence}")

    def bt(index):
        size = len(newSentence)
        #base case
        if index == size:
            return True

        for i in range(index, size+1):
            word = newSentence[index:i]
            if word in dictionary:
                print(f"match found in dictionary for {word}")
                if bt(i):
                    return True
        return False

    return bt(0)




    return False

if __name__ == "__main__":
    print(sentence_in_dictionary("it love apple celebration", ['it', 'i', 'love', 'Apple', 'Pie', 'Celebration']))

