def main():
    print("\n Convert Feet to inches!")
    required : int = int(input("Give here the feet you want to convert into inches: "))
    result : int = required * 12
    print(f"\n Here are your inches: {result} .")

if __name__ == '__main__':
    main()