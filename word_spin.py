# function that takes in a string of one or more words and returns
# same string but all words longer than 4 words reversed.

sentence = "Welcome"

def spin_words(sentence):
    # function to reverse strings in place
    def reverse_string(instring):
        return instring[::-1]
    # convert string into list by splitting words into elements
    as_list = sentence.split()
    # check words that are >= 5 chars and reverse
    for i in range(len(as_list)):
        if len(as_list[i]) >= 5:
            as_list[i] = reverse_string(as_list[i])
    # convert list of words back into string
    return " ".join(as_list)


if __name__ == "__main__":
    answer = spin_words(sentence)
    print(answer)

