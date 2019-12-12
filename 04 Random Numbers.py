#Random Number Data Type

import random

#To call the random library and see what methods are available, use a '.'
#The random function  is a part of the random library and will produce random numbers between 0 and 1
#Run the script multiple times to generate random numbers

randomnumber = random.random()

print randomnumber

#To provide a random integer in the range of a and b use the command 'randint'
#To provide the range, follow the method displayed in the command box and type in 
#the lowest and highest number separated by a colon e.g. (5,25). 
#This will generate a whole number with no decimal points

randomnumber = random.randint(5,25)

print randomnumber