def main():
    number = input("\nEnter a number to see it's square: ")
    rNum : int = int(number)
    result = rNum ** 2
    print(f"\nThe square of number {number} is \033[1;3m{result}\033[0m .\n")

if __name__ == '__main__':
    main()