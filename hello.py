print("Hello World") #FirstLine of Python code

#Str tasks
f_name = 'Moe'
l_name = 'Jalili'
message1 = 'Hello {} {}'.format(f_name,l_name)
message2 = f'Hello {f_name} {l_name}'
message3 = 'Hello %s %s' % (f_name,l_name)
print(message1)
print(message2)
print(message3)

#List
my_list1 = ['Moe', 35, 3.1415, None, 'Brisbane']
print(my_list1)
my_list2 = my_list1[1:4]
print(my_list2)

#Tuple
#my_tuple = ('Moe', 35, 3.1415, None, 'Brisbane')
address = ('http','moejalili.com', 80)
protocol, domain, port = address
print(domain)
print(len(address))

#Dict   'Key' : value
my_dict = {
    'one':1,
    'two':2,
    'three':3,
    'four':4
}
number_one = my_dict['one']    #read the value of a key
print(number_one)      
my_dict['ten'] = 10            #assign a Key/Value to the my_dict
print(my_dict)

#Operators  **, /, //, ++, --, not, and, or,
# not a == 1 is equal to a!=1
#in operator to check membership in collection
my_list3 =['a','b','c','d','e','f','g']
found_f = 'f' in my_list3 
print(found_f)

#PEP-8   (Suggestion Box)  ---> Identation 4 spaces recommended, error if identation is mot consistent
#PEP-8   (Suggestion Box)  ---> snake case for variable and function name my_list (Not myList)

#Conditionals             elif(else if)
a = 45
if a == 42:
    print('You discovered meaning of life!')
if a == 43:
    print('close but no Cigar!')
else:
    print('Better luck next time!')

evening = 1
message4 = 'Turn the light {}'.format('on' if evening == True else 'off')
print(message4)

#there is no switch in Python 

#exapme of FOR and IF
lower_names = ['moe','bahar','tim','ava','leo']
upper_names = []

""" for name in lower_names:
    name2 = name.capitalize()
    upper_names.append(name2)
print(upper_names) """ 

""" upper_names = [name.capitalize() for name in lower_names]
print(upper_names) """ 

""" upper_names = [name.capitalize() for name in lower_names if len(name) < 4]
print(upper_names) """

#This example uses tuple destructuring and a conditional inside of a list comprehension
boy_names = [
    name.capitalize() for (idx, name)
        in enumerate(lower_names)           #enumerate() function it will return a list of tuple with the (index,element) -->[(0,'moe),(1,'bahar'),...]
            if idx % 2 == 0
            ]
print(boy_names)    


#Functions
""" def say_hello(first_name):
    message5 = f'Hello {first_name}'
    return message5

greeting = say_hello('Bahar')
print(greeting) """


def parse_address(address):
    protocol_stop = address.find(':')
    protocol_start = address.rfind(':')
    protocol = address[:protocol_stop]
    port = address[protocol_start+1:]
    domain = address[protocol_stop + 3:protocol_start]
    return (protocol, domain, port)

(protocol, domain, port) = parse_address('http://example.com:80')
print(protocol,domain,port)

#Modular Python Application
#A module is simply a container for a chunk of code that can be reused in an application.
#The Python Standard Library contains many modules that are useful in everyday tasks. Let's consider the random module.
suits = ['hearts','clubs','spades','diamonds']
ranks = [str(r) for r in range(2,11)]   #The range function will generate integers from the start index up to the stop index, so 2 through 10 in this example. And the str initializer will cast the integers to strings. Finally, the list initializer will split the string into a list.
ranks.extend(list('AKQJ'))             

#Now import the random module and use the choice function to select a suit and rank.

import random
suit = random.choice(suits)
rank = random.choice(ranks)
card = f'{rank} of {suit}'
print(card)


from random import choice 
suit = choice(suits)
rank = choice(ranks)
card = f'{rank} of {suit}'
print(card)

#Both work the same. Which one should you use? That depends. To avoid naming conflicts, it is best to import the module and refer to the individual members. 

""" from random import * #This will import everything from the random module.
# This is common in data analysis with Python. You will often see these two modules aliased.
import numpy as np   
import pandas as pd
import matplotlib.pyplot as plt
 """
#Creating a module
import random as rnd

suit = random.choice(suits)
rank = random.choice(ranks)
card = f'{rank} of {suit}'

def draw_card():
    suit = rnd.choice(suits)
    rank = rnd.choice(ranks)
    card = f'{rank} of {suit}'
    return card
#in cards.py file
""" from cards import draw_card

def draw_hand(num_cards):
    hand = [draw_card() for _ in range(num_cards)]
    return hand

if __name__ == '__main__':
    poker_hand = draw_hand(5)
print(poker_hand) """


import time, sys 

for i in range(5):
    print(i)
    time.sleep(1)

for i in range(100):
	print(5**i)

