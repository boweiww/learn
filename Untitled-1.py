print("Hello world")
# FizzBuzz: Write a loop that prints numbers from 1 to 100, with the following caveat:
# If the number is divisible by 3 you print “Fizz”, if it’s divisible by 5 you print “Buzz”, and if it’s divisible by both 3 and 5 you print “FizzBuzz”

for i in range(1,100):
    if(i%3 == 0  and  i%5 == 0):
        print("FizzBuzz")
    else if (i%3 == 0 ):
        print("Fizz")
    else if (i%5 == 0):
        print("Buzz")      
    else:
            print(i)
  
# CustomLoop: FizzBuzz is a popular thing, but now clients want to be able to write their own versions. Unfortunately clients don’t know how to code very well.
#  Refactor FizzBuzz into a function customLoop(config) that accepts a parameter specifying strings to print for given numbers.
# e.g. if the spec says: 2 -> “Beep”, 3 -> “Bop”, 5 -> “Boop”, the output should start with:
# 1, Beep, Bop, Beep, Boop, BeepBop ...

[[2,"Beep"],[3,"Bop"]]

def customLoop(configList, length):
    for i in range(1,length):
        char = ""
        for j in range(len(configList)):
            if (i%configList[j][0] == 0):
                char = char + configList[j][1]
        if (char == ""):
            print(i)
        else:
            print(char)
# Write a function frequencyPrinter(text, n) that prints the nth most frequent character in a string
# (e.g. if the string is “abbccc”, the 1st most frequent is ‘c’, the 2nd is ‘b’, and 3rd is ‘a’)
bbaccc
abbccc2
def frequencyPrinter(text, n):
    text = sort(text)
    j = 0
    current = text[0]
    numlist = []
    for i in range (len(text)):
        if (current != text[i]):
            numlist.append([j,current])
            current =  text[i]
            j = 0
        else:
            j = j+1
    numlist.sort()
    print(numlist[n][1])    


# Identify the intent of the code (below) and fix any existing and potential errors
# (‘print’ is a generic console output function, ‘data.char’ is a character, characters and
# strings are concatenatable)
    function mysteryFn(data) {
        if data == null:
        return data
        var lResult = mysteryFn(data.left); 
        var rResult = mysteryFn(data.right); 
        return lResult + data.char + rResult;
        }
        print(mysteryFn(data));


                 10
                / \
                5  5
               /\  /\
               2 3 2 3
               
               10