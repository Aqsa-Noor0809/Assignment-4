def main():
    number = input("\nEnter a number to see it's square: ")
    rNum : int = int(number)
    result = rNum ** 2
    print(f"\nThe square of number {number} is {result} .\n")

if __name__ == '__main__':
    main()