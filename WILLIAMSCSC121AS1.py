#Aaron Williams
#01/25/18
#CSC-121
#This program will allow the user to convert Celsius to Fahrenheit and Fahrenheit to Celsius

def main():
    userTempChoice = mainMenu()
    print(userTempChoice)
    if userTempChoice == 1:
        toFahrenheit()
    elif userTempChoice == 2:
        toCelsius()
    else:
        print("Please input 1 or 2, other answers are invalid.")
        print("")
        main()

def mainMenu():
    print("=" * 55)
    print("Would you like to convert to Fahrenheit or Celsius?")
    print("1.\tFahrenheit")
    print("2.\tCelsius")
    userTempChoice = int(input("Please input an answer: "))
    print("=" * 55)
    return userTempChoice

def toFahrenheit():
    userTemp = getInput()
    userTempConverted = userTemp * 1.8 + 32
    print("Your temperature in Celsius was: ",userTemp)
    print("Your new Fahrenheit temperature is: ",userTempConverted)
    print("")
    print("Would you like to run the program again?")
    print("1. \t YES")
    print("2. \t NO")
    rerunProgram = int(input("Please input an answer: "))
    if rerunProgram == 1:
        main()
    else:
        print("Thank you for using this program, see you next time.")

def toCelsius():
    userTemp = getInput()
    userTempConverted = (userTemp - 32) * (5/9)
    print("Your temperature in Fahrenheit was: ",userTemp)
    print("Your new Celsius temperature is: ",userTempConverted)
    print("")
    print("Would you like to run the program again?")
    print("1. \t YES")
    print("2. \t NO")
    rerunProgram = int(input("Please input an answer: "))
    if rerunProgram == 1:
        main()
    else:
        print("Thank you for using this program, see you next time.")
    
def getInput():
    #User will input a temperature based on their choice from the main menu
    #Both toCelsius and toFahrenheit share this function to get a temperature from the user
    print("What is the temperature you're trying to convert?")
    userTemp = float(input("Please input a temperature: "))
    return userTemp

main()
