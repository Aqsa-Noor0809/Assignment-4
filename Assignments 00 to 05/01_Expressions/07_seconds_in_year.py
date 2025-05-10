days_in_a_year : int = 365;
hours_in_a_day : int = 24;
minutes_in_an_hour : int = 60;
seconds_in_a_minute : int = 60;
seconds_in_a_year : int = days_in_a_year * hours_in_a_day * minutes_in_an_hour * seconds_in_a_minute ;

def main():
    print("\n let's calculate the number of seconds in a year!")
    print("\nPROCESSING...")
    print(f"\nThe number of seconds in a year is \033[1;3m{seconds_in_a_year}\033[0m \n.")
    

if __name__ == '__main__':
    main()