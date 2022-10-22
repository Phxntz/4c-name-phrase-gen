import string
import random 
from random import Random, randint


def random_string(letter_count, digit_count):  
    str1 = ''.join((random.choice(string.ascii_lowercase) for x in range(letter_count)))  
    str1 += ''.join((random.choice(string.digits) for x in range(digit_count)))  
    f = 0
    while f < 1:
        sam_list = list(str1) # it converts the string to list.  
        random.shuffle(sam_list) # It uses a random.shuffle() function to shuffle the string.  
        final_string = ''.join(sam_list)
        f = f + 1     
        open('gened.txt','a+').write("{}\n".format(final_string))
    return final_string
v = 0
while v < 1000:
    print(random_string(3, 1))
    print(random_string(2, 2))  
    v = v + 1


  