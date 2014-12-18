from termcolor import colored

print "=============================="
print "|                            |"
print "|     Binary and Decimal     |"
print "|         Converter          |"
print "|                            |"
print "==============================\n"


def toBinary(n):
    return 1

def toDecimal(n):
    return 2

def convert():
    number = raw_input("What number whould you like to convert? ")

    try:
        number = int(number)
    except:
        print colored("That's not a number silly!\n", 'red')
        convert()

    convertType = raw_input("1. Decimal to Binary\n2. Binary to Decimal ")

    if convertType == "1":
        return toBinary(number)
    elif convertType == "2":
        return toDecimal(number)
    else:
        print "I don't understand your answer, please choose 1 or 2!\n"
        convert()

print convert()