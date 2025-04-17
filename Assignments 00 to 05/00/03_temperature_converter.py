def main():
    print("Need to convert fahrenheit to celsius?")
    fahrenheit = float(input("Enter the fahrenheit temperature: "))
    celcius = (fahrenheit - 32) * 5.0 / 9.0
    print(f"\n The temperature is \033[1;3m{celcius}\033[0m degrees celsius!\n")

if __name__ == '__main__':
    main()