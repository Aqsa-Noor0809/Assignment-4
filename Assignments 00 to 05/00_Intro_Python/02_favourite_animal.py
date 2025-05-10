def main():
    print("Let's see if our favourite animals are the same!")
    animal = input("Enter your favourite animal: ")
    print(f"\n Oh Wow! \nMy fvourite animal is also \033[1;3m{animal}\033[0m !")

if __name__ == "__main__":
    main()