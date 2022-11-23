#Version 3
import random
class RandomNumberGenerator():

    def RandomNumber(amount, minRange, maxRange):
# PRECONDITION: minRange < maxRange
# PRECONDITION: amount > 0

# POSTCONDITION: a RandNumber has am "amount" times been generated between the minRange and Maxrange 
# POSTCONDITION: a lsit with all the RandNumbers has been returned to the output      
        RandNumberList = []
        for n in range(amount):
            RandNumber = random.randrange(minRange, maxRange)
            RandNumberList.append(RandNumber)
        return RandNumberList


print(RandomNumberGenerator.RandomNumber(4,50,100))