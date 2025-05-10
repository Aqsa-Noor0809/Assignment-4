C : int = 299792458  # Speed of light in m/s

def main():
    M : int =  float(input("Enter mass in kg: "))
    result : int = M * C**2
    print(" e = m * C^2")
    print(f" e = {M} kg  * {C}^2 m/s")
    print(f"Energy equivalent of \033[1;3m {M} \033[0m kg is \033[1;3m{result}\033[0m Jouls.")

if __name__ == '__main__':
    main()