# RohanRenganathan
import sys
from os import system


def screenClear():
    _ = system("clear")


#######################################################
# This function will check if the input of the Roman Characters is either M, D, C, L, X, V, I
def validRomanChars(inputRomanNumber):
    val = True
    lettersToCheck = ["M", "D", "C", "L", "X", "V", "I"]
    if any(char not in lettersToCheck for char in inputRomanNumber):
        print("Invalid Roman Characters ~ The valid Roman Characters are M, D, C, L, X, V, I")
        val = False
    return val

    ####################################################


# This function checks that the order of the numbers are in the correct order
def validateOrder(inputRomanNumber):
    val = True
    for i in range(len(inputRomanNumber)):
        firstChar = inputRomanNumber[i]
        remainingStr = inputRomanNumber[i + 1:]

        if firstChar == "D" and "M" in remainingStr:
            print("The letters are not in descending order ~ D cannot be followed by M")
            val = False

        if firstChar == "C" and any(i in remainingStr for i in "MD"):
            print("The letters are not in descending order ~ C cannot be followed by M D")
            val = False

        if firstChar == "L" and any(i in remainingStr for i in "MDC"):
            print("The letters are not in descending order ~ L cannot be followed by M D C")
            val = False

        if firstChar == "X" and any(i in remainingStr for i in "MDCL"):
            print("The letters are not in descending order ~ X cannot be followed by M D C L")
            val = False

        if firstChar == "V" and any(i in remainingStr for i in "MDCLX"):
            print("The letters are not in descending order ~ V cannot be followed by M D C L X")
            val = False

        if firstChar == "I" and any(i in remainingStr for i in "MDCXV"):
            print("The letters are not in descending order ~ I cannot be followed by M D C X V")
            val = False
    return val


####################################################
# This function checks that the number entered is not greater than 4000
def maxValue(arabicNumber):
    val = True
    if (arabicNumber) > 4000:
        print("The number has to be less than 4000")
        val = False

    return val


######################################################
# This function checks that a letter is not repeated if it can be replaced with another letter
def checkRepeatLetters(inputRomanNumber):
    val = True
    if "DD" in inputRomanNumber:
        print("DD should be replaced with M")
        val = False

    elif "CCCCC" in inputRomanNumber:
        print("CCCCC should be replaced with D")
        val = False

    elif "LL" in inputRomanNumber:
        print("LL should be replaced with C")
        val = False

    elif "XXXXX" in inputRomanNumber:
        print("XXXXX should be replaced with L")
        val = False

    elif "VV" in inputRomanNumber:
        print("VV should be replaced with X")
        val = False

    elif "IIIII" in inputRomanNumber:
        print("IIIII should be replaced with V")
        val = False

    return val


#######################################################
# This function takes in Roman Characters and converts it into Arabic Numbers
def convertRomanToArabic(inputRomanNumber):
    sumInputNum = 0
    for i in inputRomanNumber:
        if i == "M":
            sumInputNum = sumInputNum + 1000
        elif i == "D":
            sumInputNum = sumInputNum + 500
        elif i == "C":
            sumInputNum = sumInputNum + 100
        elif i == "L":
            sumInputNum = sumInputNum + 50
        elif i == "X":
            sumInputNum = sumInputNum + 10
        elif i == "V":
            sumInputNum = sumInputNum + 5
        elif i == "I":
            sumInputNum = sumInputNum + 1
    return (sumInputNum)


#######################################################
# This function converst an Arabic number into Roman Numerals
def convertArabicToRoman(inputNumber):
    totalThousand = 0
    totalFiveHundred = 0
    totalHundred = 0
    totalFifty = 0
    totalTen = 0
    totalFive = 0

    romanAnswer1 = ""
    romanAnswer2 = ""
    romanAnswer3 = ""
    romanAnswer4 = ""
    romanAnswer5 = ""
    romanAnswer6 = ""
    romanAnswer7 = ""

    firstNumber = int(inputNumber / 1000)
    for i in range(0, firstNumber):
        romanAnswer1 = (romanAnswer1 + "M")
        totalThousand = (totalThousand + 1000)

    secondNumber = int((inputNumber - totalThousand) / 500)
    if secondNumber > 0:
        romanAnswer2 = "D"
        totalFiveHundred = 500

    thirdNumber = int((inputNumber - (totalThousand + totalFiveHundred)) / 100)
    for i in range(0, thirdNumber):
        romanAnswer3 = (romanAnswer3 + "C")
        totalHundred = (totalHundred + 100)

    fourthNumber = int((inputNumber - (totalThousand + totalFiveHundred + totalHundred)) / 50)
    if fourthNumber > 0:
        romanAnswer4 = "L"
        totalFifty = 50

    fifthNumber = int((inputNumber - (totalThousand + totalFiveHundred + totalHundred + totalFifty)) / 10)
    for i in range(0, fifthNumber):
        romanAnswer5 = (romanAnswer5 + "X")
        totalTen = (totalTen + 10)

    sixthNumber = int((inputNumber - (totalThousand + totalFiveHundred + totalHundred + totalFifty + totalTen)) / 5)
    if sixthNumber > 0:
        romanAnswer6 = "V"
        totalFive = 5

    seventhNumber = int(
        inputNumber - (totalThousand + totalFiveHundred + totalHundred + totalFifty + totalTen + totalFive))
    for i in range(0, seventhNumber):
        romanAnswer7 = (romanAnswer7 + "I")

    finalRomanAns = (
                romanAnswer1 + romanAnswer2 + romanAnswer3 + romanAnswer4 + romanAnswer5 + romanAnswer6 + romanAnswer7)

    return (finalRomanAns)


#######################################################
# .                MAIN PROGRAM                        #
#######################################################
romanNumber1 = input("Enter your first number ")
if romanNumber1.lower() == "clear":
    screenClear()
    exit()

if type(romanNumber1) == str and validRomanChars(romanNumber1) and validateOrder(romanNumber1) and checkRepeatLetters(
        romanNumber1):
    arabicNumber1 = convertRomanToArabic(romanNumber1)
else:
    exit()

if maxValue(arabicNumber1):
    print(arabicNumber1)
else:
    exit()

romanNumber2 = input("Enter your second number ")
if romanNumber2.lower() == "clear":
    screenClear()
    exit()

if type(romanNumber2) == str and validRomanChars(romanNumber2) and validateOrder(romanNumber2) and checkRepeatLetters(
        romanNumber2):
    arabicNumber2 = convertRomanToArabic(romanNumber2)
else:
    exit()

if maxValue(arabicNumber2):
    print(arabicNumber2)
else:
    exit()

if romanNumber1 == romanNumber2:
    print("Both numbers cannot be the same")
    exit()

if arabicNumber2 > arabicNumber1:
    print("The first number has to be bigger than the second number")
    exit()

myOperation = input("What operation do you want to do? + - ")
if myOperation.lower() == "clear":
    screenClear()
    exit()

if myOperation == "+":
    arabicAnswer = (arabicNumber1 + arabicNumber2)

elif myOperation == "-":
    arabicAnswer = (arabicNumber1 - arabicNumber2)

else:
    print("This is not a valid operation ~ + - x / ")

romanAnswer = convertArabicToRoman(arabicAnswer)
print("Arabic Answer = " + str(arabicAnswer))
print("Roman Answer = " + str(romanAnswer))

#######################################################
