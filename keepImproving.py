"""
MUSTAFA MURAT COSKUN: UDEMY  COURSE
SECTION 3: HOMEWORKS
TAKE PARAMETERS AS MINIMUM AMOUNT OF WORDS TO DECREASE THE SIZE OF FILE.

HOMEWORK 1:
a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("ThirdNumber: "))

result = a * b * c
print("The multiplication of taken  numbers whose are {}, {}, and {}: {}".format(a,b,c,result))

HOMEWORK 2:
height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

bodyEvaluater = (weight / (height ** 2))
print("Height: {}; Weight: {}; BMI: {}".format(height,weight,bodyEvaluater))

HOMEWORK 3:
money = float(input("How much fuel is used: "))
kilometers = float(input("How much road will be gone: "))

operation = money * kilometers
print("You have to pay {} per {}: {} cost.".format(money,kilometers,operation))

HOMEWORK 4:

name = str(input("Enter your name: "))
surname= str(input("Enter your surname: "))
idNumber=int(input("Enter your id number: "))

print("Name:      {}\nSurname:  {}\nID:            {} ".format(name,surname,idNumber))

HOMEWORK 5:

a = int(input("Enter a number: "))
b  = int(input("Enter another number: "))

print("First values of parameters: a-- {} ; b-- {}".format(a,b))

constantVar = a
a = b
b = constantVar

print("Last values of parameters: a--{} ; b--{}".format(a,b))

HOMEWORK 6:

first = int(input("Enter the first number: "))
second = int(input("Enter the second: "))

third = (((first ** 2) + (second ** 2)) ** (1/2))
print("The variables of perpendicular: {}, {}\nThe hypotenuses: {}".format(first,second,third))

SECTION 4: HOMEWORKS:

HOMEWORK 1:

height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

operation = (weight / (height ** 2))
message = ("Your measurements: height: {}, weight: {}, Body Mass Index: {}".format(height,weight,operation))

if (operation < 18.5):
    print(message, ": Zayıf")
elif (operation >= 18.5 and operation < 25):
    print(message, ": Normal")
elif (operation >= 25 and operation < 30):
    print(message, ": Fazla kilolu")
#elif (operation >=30):
else:
    print(message, ": Obez")

HOMEWORK 2:
a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))

if (a < b and a < c):
    print("Minimum: {}".format(a))
    if (b > c ):
        print("Medium: {}\nMaksimum: {}".format(c,b))
    elif(b < c):
        print("Medium: {}\nMaksimum: {}".format(b,c))
    else:
        print("Maksimum: {}".format(b))

elif (b < a and b < c):
    print("Minimum: {}".format(b))
    if (a > c):
        print("Medium: {}\nMaksimum: {}".format(c,a))
    elif (a < c):
        print("Medium: {}\nMaksimum: {}".format(a,c))
    else:
        print("Maksimum: {}".format(c))

elif(c < a and c < b):
    print("Minimum: {}".format(c))
    if(a > b):
        print("Medium: {}\nMaksimum: {}".format(b,a))
    elif (a < b):
        print("Medium: {}\nMaksimum: {}".format(a,b))
    else:
        print("Maksimum: {}".format(a))

HOMEWORK 3:
fmidterm = float(input("Enter the first midterm: "))
smidterm = float(input("Enter the second midterm: "))
final = float(input("Enter the final: "))

result = (fmidterm*30 + smidterm*30 + final*40)/100

if (result >= 90):
    print("Result: {} -- AA".format(result))
elif (result >= 85):
    print("Result: {} -- BA".format(result))
elif (result >= 80):
    print("Result: {} -- BB".format(result))
elif (result >= 75):
    print("Result: {} -- CB".format(result))
elif (result >= 70):
    print("Result: {} -- CC".format(result))
elif (result >= 65):
    print("Result: {} -- DC".format(result))
elif (result >= 60):
    print("Result: {} -- DD".format(result))
elif (result <= 55) :
    print("Result: {} -- FF".format(result))

HOMEWORK 4:
type = str(input("What will you select Triangle or Quadrangle? (T/Q)  "))

if (type == "T"):

    first = int(input("First side: "))
    second = int(input("Second side: "))
    third = int(input("Third side: "))

    #conditions for defining a triangle
    fcondition =  ((first < (second + third)) and (first > abs(second - third)))
    scondition = ((second < (first + third)) and (second > abs(first - third)))
    tcondition = ((third < (first + second)) and (third > abs(first - second)))

    if ((fcondition and scondition) and tcondition):
        if ((first == second and first != third) or (first == third and first != second) or (second == third and second != first)):
            print("{}, {}, {} sides define a ISOSCALE triangle.".format(first,second,third))
        elif (first == second == third):
            print("{}, {},{} sides define a EQUILATERAL triangle.".format(first,second,third))
        else:
            print("{}, {}, {} sides define a NORMAL triangle".format(first,second,third))
    else:
        print("{}, {}, {} sides DO NOT define a triangle.".format(first,second,third))

elif(type == "Q"):

    one = int(input("First side: "))
    two = int(input("Second side: "))
    three = int(input("Third side: "))
    four = int(input("Fourth side: "))

    if (one == two == three == four):
        print("{}, {}, {}, {} sides define a SQUARE.".format(one,two,three,four))

    elif ((one == two and three == four) or (one == three and two == four) or (one == four and two == three) ):
        print("{}, {}, {}, {} sides define a RECTANGLE.".format(one,two,three,four))

    else:
        print("{}, {}, {}, {} sides define a NORMAL quadrangle.".format(one,two,three,four))

SECTION 5: HOMEWORKS:
HOMEWORK 1:

number = int(input("Enter a number: "))
divisionList = list()

for divider in range(1, number):
    if (number % divider == 0):
        divisionList.append(divider)

summation = 0
for element in divisionList:
    summation = summation + element

if (summation == number):
    print("{} is an amazing number.".format(number))
else:
    print("{} is NOT an amazing number since their dividers' summation equals to {}".format(number,summation))

HOMEWORK 2:

first = (input("enter a number: "))
indexOfFirst = list()
thirdpowerofFirst = list()

for character in first :
    indexOfFirst.append(int(character))
print("STEP 1: Division of given number {}  in list form: {}".format(first,indexOfFirst))

for element in indexOfFirst:
    thirdpowerofFirst.append(element ** len(indexOfFirst))
print("STEP 2: Forms of given numbers {} in power of a number that equals order number {}: {}".format(first,len(indexOfFirst),thirdpowerofFirst))

summation = 0
for index in thirdpowerofFirst:
    summation += index
print("STEP 3: Summations of the numbers that are found in ordered forms in step 2 {}: {}".format(thirdpowerofFirst, summation))

if ((first) == str(summation)):
    print("{} is an ARMSTRONG number".format(first))
elif ((first) != str(summation)):
    print("Given number: {}\nSummation of characters: {}\n{} is NOT an armstrong number.".format(first,summation,first))

HOMEWORK 3:

for first in range(1,11):
    for second in range(1,11):
        print(first*second)

HOMEWORK 4:

dividerList = list()
notdividerlist = list()

for number in range(1,101):
    if (number % 3 == 0):
        dividerList.append(number)
    else:
        notdividerlist.append(number)

print("Numbers divisible without reminder to 3: {}".format(dividerList))
print("Numbers NOT divisible without reminder to 3: {}".format(notdividerlist))

HOMEWORK 5:

even = list()
odd = list()

for number in range (1,101):
    if (number % 2 == 0):
        even.append(number)
    else:
        odd.append(number)

print("EVEN NUMBER LIST: {}".format(even))
print("ODD NUMBERS LIST: {}".format(odd))

HOMEWORK 6:

result = 0
while (True):
    option = input("Enter a number: ")

    if (option == "Q"):
        print("Loop is finishing...")
        break
    else:
        result += int(option)
        print("Summation: {}".format(result))

SECTION 6: HOMEWORKS: YOU HAVE TO TRANSFORM THEM INTO FUNCTION MODE.
HOMEWORK 1:

first = int(input("Enter a number: "))
second = int(input("Enter another number: "))

firstList = list()
secondList = list()
commonList = list()

for character in range(1,first+1):
    if (first % character == 0):
        firstList.append(character)
print("{} divider list: {}".format(first,firstList))

for element in range(1, second+1):
    if (second % element == 0):
        secondList.append(element)
print("{} divider list: {}".format(second,secondList))

for firstIndex in firstList:
    for secondIndex in secondList:
        if (firstIndex == secondIndex):
            commonList.append(firstIndex)
print("Common diviser list of {} and {}: {}".format(first,second,commonList))
print("Maximum common diviser of {} and {}: {}".format(first,second,commonList[len(commonList)-1]))

HOMEWORK 2: CONTINUE TO OBTAIN EKOK WITH  USING WHILE LOOP.

first = int(input("Enter a number: "))
second = int(input("Enter another number: "))

multiplicationOfNumbers = first*second
firstList = list()
secondList = list()
commonList = list()

for character in range(1,first+1):
    if (first % character == 0):
        firstList.append(character)
print("{} divider list: {}".format(first,firstList))

for element in range(1, second+1):
    if (second % element == 0):
        secondList.append(element)
print("{} divider list: {}".format(second,secondList))

for firstIndex in firstList:
    for secondIndex in secondList:
        if (firstIndex == secondIndex):
            commonList.append(firstIndex)
print("Common diviser list of {} and {}: {}".format(first,second,commonList))
print("Maximum common diviser of {} and {}: {}".format(first,second,commonList[len(commonList)-1]))

ekokOperation = multiplicationOfNumbers/(commonList[len(commonList)-1])
print("Minimum common multiple of {} and {}: {}".format(first,second,ekokOperation))


HOMEWORK 3: NICE EXAMPLE

number=  (input("Enter a number: "))
indexList = list()
printedList = list()

numberAlphabet = {0: "sıfır", 1: "bir" , 2: "iki", 3: "üç", 4: "dört", 5: "bes", 6 : "altı", 7: "yedi", 8: "sekiz", 9: "dokuz" }
decimalResponse = {1: "on", 2: "yirmi", 3: "30", 4: "kırk", 5: "elli", 6: "atmıs", 7: "yetmis", 8: "seksen", 9: "doksan"}

if (len(number) == 2):

    for character in number:
        indexList.append(int(character))

    firstIndex = indexList[0]
    secondIndex = indexList[1]

    for key in decimalResponse.keys():
        if (key == firstIndex):
            printedList.append(decimalResponse.get(key))
    for keys in numberAlphabet.keys():
        if (keys == secondIndex):
            printedList.append(numberAlphabet.get(keys))
    print("{}: {} {}".format(number,printedList[0],printedList[1]))

else:
    print("Please enter a number whose order equals to 2")

HOMEWORK 4:

pisagorList = list()

for a in range(1,101):
    for b in range(1,101):
        for c in range(1,101):

            operation = (a**2 + b**2 == c**2)
            if (operation):
                #pisagorList.append("(")
                pisagorList.append((a,b,c,))
                #pisagorList.append(b)
                #pisagorList.append(c)
                #pisagorList.append(") ; ")

for numbers in pisagorList:
    print(numbers, end= " ")

PROJECT EULER PROBLEMS:
PROBLEM 1:
multipleList = list()

for element in range(1,1000):
    if (element % 3 == 0 or element % 5 == 0):
        multipleList.append(element)

summation = 0

for number in multipleList:
    summation += number
print(summation)

PROBLEM 2:
squareList = list()
summation = 0
secondSum = 0

for number in range(1,101):
    squareList.append(number**2)
for value in squareList:
    summation += value

for element in range(1,101):
    secondSum += element

finalOperation = (secondSum**2 - summation)
print("Differences: {}".format(finalOperation))

PROBLEM 3:
operation = (2**1000)
result = str(operation)
summation = 0
operationList = list()
for number in result:
    operationList.append(number)
for character in operationList:
    summation += int(character)
print(summation)

PROBLEM 4:
summation = 0
multiple= 1
factorial = int(input("Enter a number: "))
for number in range(1, factorial+1):
    multiple *= number
for character in str(multiple):
    summation += int(character)
print(summation)

denemeForProblem5:
productList = list()
multiple = 1
for a in range(1,400):
    for b in range(1,400):
        for c in range(1,400):
            if (a < b <  c):
                if ((a**2 + b**2 == c**2) and (a + b + c == 1000)):
                    productList.append(a)
                    productList.append(b)
                    productList.append(c)
print(productList)
for element in productList:
    multiple *= element
print(multiple)

deneme for problem6:

toplam = 0
secondToplam = 0
characterList = list()
fifthpowerList = list()
for number in range(10000,100000):
    for character in str(number):
        characterList.append(int(character))
    for element in characterList:
        toplam = toplam + pow(element,5)
    if (toplam == number):
        fifthpowerList.append(number)
for value in fifthpowerList:
    secondToplam += value
print(secondToplam)

deneme for problem 7:
import sys
i = 3
sum = 0
summation = 0
multipleList = list()
equationList = list()
multiple = 1
while (i < sys.maxsize):
    for character in str(i):
        for element in range(1,int(character)+1):
            multiple *= element
        multipleList.append(multiple)
        for value in multipleList:
            summation += value
            if (summation == i):
                equationList.append(summation)
            for number in equationList:
                sum += number
        print(sum)
        i += 1

PROBLEM 5:

summation = 0
powerList = list()
for number in range(1,1001):
    powerList.append(number**number)
for element in powerList:
    summation += element
indexing = (str(summation)[::-1])
secondIndexing = indexing[0:10]
finalIndexing  = secondIndexing[::-1]
print(finalIndexing)

UDEMY BASIC PROBLEM1:

def takePower(taban,power):
    operation = taban ** power
    return ("{}^{} = {}".format(taban,power,operation))

print(takePower(2,3))

UDEMY BASIC PROBLEM2:
number = int(input("Enter a number:"))
dividerList = list()
notDividerList = list()

for divider in range(1,number+1):
    if (number % divider == 0):
        dividerList.append(divider)
    else:
        notDividerList.append(divider)

print("Dividers of {}: {}\nNot dividers of {}: {}".format(number,dividerList,number,notDividerList))

UDEMY BASIC PROBLEM3:
tavuk = int(input("Enter chickens': "))
inek = int(input("Enter cows': "))
koyun = int(input("Enter sheeps': "))

operationT = 2*tavuk
operationI = 4*inek
operationK = 4*koyun

print("Total foot numbers are: {}".format(operationT+operationI+operationK))

UDEMY BASIC PROBLEM4:
x = [-2,4,10,7,-9]
multipleList = list()
toplam = 0
if (len(x) == 0):
    print(0)
else:
    for number in x:
        multipleList.append(number*(x.index(number)))
    for element in multipleList:
        toplam += element
    print(toplam)

UDEMY INTERMEDIATE PROBLEM1:
maaliyet = float(input("Enter cost of items: "))
satis = float(input("Enter sale price: "))
envanter = int(input("Items sold: "))
information = {"maaliyet": maaliyet, "satis": satis, "envanter": envanter}
profit = (information.get("envanter")*information.get("satis"))  - (information.get("envanter")*information.get("maaliyet"))
print("Recordings related to product:\nReduced cost: {}\nSale price: {}\nTotal items sold: {}\nProfit: {}".format(information.get("maaliyet"),information.get("satis"),information.get("envanter"),int(profit)))

UDEMY  INTERMEDIATE PROBLEM2:
first = int(input("First: "))
second = int(input("Second: "))
third = int(input("Third: "))
operation = (first**2 + second**2 == third**2) or (third**2 + first**2 == second**2) or (third**2 + second**2 == first**2)
conditionF = first > abs(second - third) and first < second + third
conditionS = second > abs(first - second) and second < first + third
conditionT = third > abs(first - second) and third < first + second
if (conditionT and conditionS and conditionF):
    if (operation):
        print(True)
    else:
        print(False)

PRIME NUMBER OR NOT
x = int(input("Enter a number: "))
dividerList = list()

for divider in range(1, x+1):
    if (x % divider == 0):
        dividerList.append(divider)
if (len(dividerList) <= 2):
    print("{} PRIME NUMBER".format(x))
elif (len(dividerList) >= 2):
    print("{} NOT PRIME NUMBER BECAUSE ITS DIVIDERS ARE: {}".format(x,dividerList))

UDEMY BASIC PROBLEM 5:
#base = int(input("Enter the base: "))
#result = int(input("Enter the result: "))

def hesapla(base,result):
    for number in range(1,result+1):
        operation = base ** number
        if(operation == result):
            print("{}^{}:{} Power must be: {}".format(base,number,result,number))
hesapla(3,81)
"""















