def main():
    print("Write the length of thrice sides below!")
    len1 = input("Enter the length of First side: ")
    length1 : int = int(len1)
    len2 = input("Enter the length of Second side: ")
    length2 : int = int(len2)
    len3 = input("Enter the length of Third side: ")
    length3 : int = int(len3)
    result : int = length1 + length2 + length3
    print("\nThe perimeter of the Triangle is " + str(result) + " . \n")

if __name__ == '__main__':
    main()
