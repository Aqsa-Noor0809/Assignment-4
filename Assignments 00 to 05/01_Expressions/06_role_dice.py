import random

dicesides : int = 6

def main():
    print("\n let's roll some dice!")
    die1 : int = random.randint(1, dicesides)
    die2 : int = random.randint(1, dicesides)
    total : int = die1 + die2
    print(f"die 1 is {die1}.")
    print(f"die 2 is {die2}.")
    print(f"the total is {total}.")
    print(f"\nThe results of dice rolls are \033[1;3m{die1}\033[0m and \033[1;3m{die2}\033[0m with a total of \033[1;3m{total}\033[0m .")

if __name__ == '__main__':
    main()