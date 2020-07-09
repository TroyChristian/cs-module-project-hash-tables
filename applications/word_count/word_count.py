
    
def word_count(words):
    word_occurence = {} #dictionary word:number of times word appears
    ignored_character_set = [" : ; , . - + = / \ | [ ] { } ( ) * ^ & } " ]
    word_list = words.split() #Create list of words from argument input
    #["I" "am," "Groot"]
    for i in ignored_character_set:
        for word in word_list:
            for char in word:
                try:
                    word_list.remove(i)
                except ValueError:
                    continue
    print(word_list)

word_count("I am, Groot :::")

    






if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))

""" def word_count(s):
        words.join(" ")
    tally = {}

    for letter in words:
        if letter not in tally:
            tally[letter] = 1

        else:
            tally[letter] +=1
     """
