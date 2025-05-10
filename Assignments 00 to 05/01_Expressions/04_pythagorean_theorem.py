import math

def main():
    print("\nwrite the values of Adjacent and Opposite to know the value of Hypotenuse!")
    adjacent : float = float(input("write the Adjacent side of the triangle: "))
    opposite : float = float(input("Write the Opposite side of the triangle: "))
    hypotenuse : float = math.sqrt(adjacent **2 + opposite **2 )
    hypotenuse = round(hypotenuse, 3)
    print(f"\nThe Hypotenuse side of the right angle triangle is \033[1;3m{hypotenuse}\033[0m .\n")

if __name__ == '__main__':
    main()