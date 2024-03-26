# Program that calculates carpet stuff

# Global decleration # Depricated Function
# global fitting

# fitting = 3.75


# Validate inputs Function
def areaOfRectangle():
    while True:
        try:
            num1 = float(input("What is the length of your room? "))
            assert num1 > 0
            num2 = float(input("What is the width of your room? "))
            assert num2 > 0
        except ValueError:
            print("Please input a valid number.")
            continue
        except AssertionError:
            print("Please enter a valid number.")
        else:
            global area
            area = num1 * num2
            return area
            break


# Calculates the basic cost
def calculateBasicCost():
    areaOfRectangle()
    basic = 10.25 # 6.50
    total = basic
    
    # area = areaOfRectangle()

    cost = total * area

    print(f"Your total cost for your area of {area} is: {cost}")


# Calculates the standard cost
def calculateStandardCost():
    areaOfRectangle()
    standard = 22.50 # 18.75
    total = standard

    # area = areaOfRectangle()

    cost = total * area

    print(f"Your total cost for your area of {area} is: {cost}")


# Calculates the luxury cost
def calculateLuxuryCost():
    areaOfRectangle()
    luxury = 32.25 # 29.50
    total = luxury

    # area = areaOfRectangle()

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
        if option == "2":
            calculateStandardCost()
        if option == "3":
            calculateLuxuryCost()
        if option == "4":
            exit()
        else:
            print("Please select a correct option")


# Initalise the Main Function
if __name__ == "__main__":
    main()
