def main():
    print("\n let's do some division and see its remainders!")
    devide = int(input("Please enter a number to be divided: "))
    devidedBy = int(input("Please enter a number to divide by: "))
    result1 : int = devide // devidedBy
    result2 : int = devide % devidedBy
    print(f"\nThe result of this division is \033[1;3m{result1}\033[0m quotient with a remainder of \033[1;3m{result2}\033[0m .")

if __name__ == '__main__':
    main()