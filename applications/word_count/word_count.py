""" def word_count(s):
        words.join(" ")
    tally = {}

    for letter in words:
        if letter not in tally:
            tally[letter] = 1

        else:
            tally[letter] +=1
     """



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))


