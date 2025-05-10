# ASSIGNMENT 01

def main():
    print("🔢 Simple Addition Program")

    first_input = input("Enter the first number: ")
    first_number = int(first_input)
    second_input = input("Enter the second number: ")
    second_number = int(second_input)
    total = first_number + second_number

    print(f"✅ The sum of {first_number} and {second_number} is {total}.")

if __name__ == "__main__":
    main()

# ASSIGNMENT 02

def main():
    animal = input("What's your favorite animal? ")
    print(f"My favorite animal is also {animal}!")

if __name__ == '__main__':
    main()


# ASSIGNMENT 03

def main():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    print(f"Temperature: {fahrenheit}F = {celsius}C")

if __name__ == '__main__':
    main()


# ASSIGNMENT  04

def main():
    anton : int = 21
    beth : int = 6 + anton
    chen : int = 20 + beth
    drew  : int = chen + anton
    ethan : int = chen

    print("Anton is " + str(anton))
    print("Beth is " + str(beth))
    print("Chen is " + str(chen))
    print("Drew is " + str(drew))
    print("Ethan is " + str(ethan))


if __name__ == '__main__':
    main()


# ASSIGNMET 05

def main():
    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))
    
    perimeter = side1 + side2 + side3
    
    print(f"The perimeter of the triangle is {perimeter}")

if __name__ == '__main__':
    main()


# ASSIGNMENT 06

def main():
    number = float(input("Type a number to see its square: "))
    square = number ** 2
    print(f"{number} squared is {square}")

if __name__ == '__main__':
    main()
