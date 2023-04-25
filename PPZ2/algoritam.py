#algorythm that constructs a number using an inputed positive number and an inputed negative number
#if the number is not possible to construct, it returns 1
#only a certain ammount of numbers can be used
ammount = int(input())
positive = int(input())
negative = int(input())
def construct(number):
    #constructs a number using the positive and negative numbers
    #if the number is not possible to construct, it returns 1
    #only a certain ammount of numbers can be used
    #if the number is possible to construct, it returns nothing
    #if the number is 0, it returns nothing
    if number == 0:
        return
    if number < 0:
        return 1
    if number > 0:
        if number % positive == 0:
            if number // positive <= ammount:
                return
            else:
                return 1
        if number % negative == 0:
            if number // negative <= ammount:
                return
            else:
                return 1
        if number % positive == 0 and number % negative == 0:
            if number // positive <= ammount and number // negative <= ammount:
                return
            else:
                return 1
        if number % positive != 0 and number % negative != 0:
            return 1
        if number % positive != 0:
            if number // negative <= ammount:
                return
            else:
                return 1
        if number % negative != 0:
            if number // positive <= ammount:
                return
            else:
                return 1
    return 1

print(construct(5))