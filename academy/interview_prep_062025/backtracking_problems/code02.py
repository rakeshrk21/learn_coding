# check if all the words in the sentence belong to in the dictionary

def sentence_in_dictionary(sentence, dictionary):
    lower_case_dictionary = [word.lower() for word in dictionary]
    lower_case_sentence = sentence.lower().replace(" ","")


    def back_track(index):
        size = len(lower_case_sentence)
        # base case - sentence was completely parsed
        if index == size:
            return True

        for i in range(index, size+1):
            # create the word
            word = lower_case_sentence[index:i]

            # compare it with each dictionary word
            # if match found, then  backtrack
            if word in lower_case_dictionary:
                print(f'the word: {word} was found in the dictionary')
                if back_track(i):
                    return True

        return False

    return back_track(0)

if __name__ == "__main__":
    # print(sentence_in_dictionary("applepiecelebration"))
    # print(sentence_in_dictionary("applep1celebration"))
    print(sentence_in_dictionary("it love apple celebration", ['it', 'i', 'love', 'Apple', 'Pie', 'Celebration']))
    # print(sentence_in_dictionary("applepieapple")) # multiple words ==> gives false positive