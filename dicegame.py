import random
import time
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print ("Rolling the dices...")
    print ("The values are....")

    print (random.randint(min, max))
    time.sleep(3)
    print (random.randint(min, max))

    roll_again = ("Roll the dices again?")


