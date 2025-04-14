def main():
    print("Need to convert fahrenheit to celsius?")
    fahrenheit = float(input("Enter the fahrenheit temperature: "))
    celcius = (fahrenheit - 32) * 5.0 / 9.0
    print("\n The temperature is " + str(celcius) + " degrees celsius!\n")

if __name__ == '__main__':
    main()