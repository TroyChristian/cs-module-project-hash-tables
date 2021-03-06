import string
ascii_letters = set(map(ord, string.ascii_letters))
non_letters = ''.join(chr(i) for i in range(256) if i not in ascii_letters)




def word_count(words):
 
    word_list = words.split()
    word_map = {}

    for i in word_list:
        clean_word = i.strip(non_letters).lower() 
        if clean_word in word_map:
                word_map[clean_word] += 1 # increment value of wordKey if it already exists in word map
        elif clean_word not in word_map:
                word_map[clean_word] = 1 # create key:value in list {I:1}
                

        

    return word_map

 
        

    return word_map

    






if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))


