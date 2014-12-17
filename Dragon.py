from turtle import *

print "HERE THERE BE DRAGONS!"

def makeDirections(n):
    directions = [0]
    if n == 0:
        return
    for iteration in range(n):
        otherA = []
        for i in directions:
            otherA.append(i)
        otherA.reverse()
        directions.append(0)
        for i in range(0 ,len(directions) - 1):
            if otherA[i] == 0:
                directions.append(1)
            if otherA[i] == 1:
                directions.append(0)
    for direction in directions:
        forward(4)
        if direction == 1:
            left(90)
        if direction == 0:
            right(90) 
            

makeDirections(10)
raw_input()