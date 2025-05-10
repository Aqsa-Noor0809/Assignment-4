def main():
    print("Write the length of thrice sides below!")
    len1 = float(input("Enter the length of First side: "))
    len2 = float(input("Enter the length of Second side: "))
    len3 = float(input("Enter the length of Third side: "))
    result : int = len1 + len2 + len3
    print(f"\nThe perimeter of the Triangle is \033[1;3m{result}\033[0m . \n")

if __name__ == '__main__':
    main()
