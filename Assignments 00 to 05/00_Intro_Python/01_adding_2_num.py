def main():
    print("Give me Two values to add.")
    num1 : str = input("Enter First Number: ")
    num1 : int = int(num1)
    num2 : str = input("Enter Second Number: ")
    num2 : int = int(num2)
    total : int = num1 + num2 
    print("Your Answer is " + str(total) + ".")

if __name__ == '__main__':
    main()