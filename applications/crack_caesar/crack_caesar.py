# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
#https://en.wikipedia.org/wiki/Frequency_analysis
#Ceaser Uper:
#Understand: All English texts display an occurence of letter frequency, which I have a chart of
#Plan: Count all letters in ceaser cipher, see % of that letter occurence, map to known frequency of eng.letters
#Execute: 
#Reflect

def count_letters(cipher):
    # Count the letters in the cipher text by mapping them to a dictionary based on frequency of occurence
    #{X:31}
    pass 

def determine_percent(counted_cipher):
#determine percentage based occurence of values in the counted_cipher dictionary
#total values = 100, {X:10} X = 10%

def map_counted_cipher_to_english(percented_cipher):
    #Chart provided in read me here, map dictionary to chart
    # if chart says a is 10%, x occurrs 10% {x:a}
    #return key


def apply_key(key, cipher):
    #Pass in key returned from map_counted_cipher_to_english,
    #pass in the cipher itself
    # Determine logic to pass each letter of cipher through key to create a message
    #Return decoded message 




