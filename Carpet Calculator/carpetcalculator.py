# Program that calculates carpet stuff

# Global decleration 
global fitting

fitting = 3.75


# Validate inputs Function
def areaOfRectangle():
    while True:
        try:
            num1 = float(input("What is the length of your room? "))
            num2 = float(input("What is the width of your room? "))
            if (num1 and num2) < 0:
                raise ValueError
        except ValueError:
            print("Please input a valid number.")
            continue
        else:
            global area

            area = num1 * num2
            return area


# Calculates the basic cost
def calculateBasicCost():
    basic = 6.50
    total = basic + fitting
    global cost

    cost = total * area

    print(f"Your total cost for your area of {area} is: {cost}")


# Calculates the standard cost
def calculateStandardCost():
    areaOfRectangle()
    standard = 18.75
    total = standard + fitting
    global cost

    cost = total * area

    print(f"Your total cost for your area of {area} is: {cost}")


# Calculates the luxury cost
def calculateLuxuryCost():
    areaOfRectangle()
    luxury = 29.50
    total = luxury + fitting
    global cost

    cost = total * area

    print(f"Your total cost for your area of {area} is: {cost}")


# Main Function
def main():
    while True:
        print("=-=-=-=-=- Main Menu -=-=-=-=-=")
        print("1.) Basic\n2.) Standard\n3.) Luxury\n4.) Exit\n")
        option = input("What option of carpet would you like? ")

        if option == "1":
            calculateBasicCost()
        elif option == "2":
            calculateStandardCost()
        elif option == "3":
            calculateLuxuryCost()
        elif option == "4":
            exit()
        else:
            print("Please select a correct option")


# Initalise the Main Function
if __name__ == "__main__":
    main()