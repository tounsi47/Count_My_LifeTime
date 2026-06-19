print("Count my Lifetime version 2.0")
print("First, we need to calculate your age")
print("Please type your birth date : ")
from date_time_retrieving import input_age_reformulation
from time_unites import TimeUnites 

restart = True
while restart  :
    try : 
        day = int(input("your birth day :"))
        month = int(input("your birth month : "))
        year = int(input("your birth year :"))
        
        
        input_age = input_age_reformulation(year, month, day).retrieve_input_age()
        
        
        if input_age[0] < 0 :
            print("seems like you were born in the future :0")
        elif input_age[0] == 0 :
            print("New Born !!!!!")
        print(f"Great, you have {input_age[0]} year and {input_age[1]} days. Now please select the unite  you want to convert your age")
        print("1 : seconds")
        print("2 : minutes")
        print("3 : hours")
        print("4 : days")
        print("5 : weeks")
        print("6 : months")
        option = int(input(">>>"))
        if option == 1 : 
            age_in_seconds = TimeUnites(input_age).convert_to_seconds()
            print(f"{round(age_in_seconds)} secondes")
        elif option == 2 : 
            age_in_minutes = TimeUnites(input_age).convert_to_minutes()
            print(f"{round(age_in_minutes)} minutes")
        elif option == 3 : 
            age_in_hours = TimeUnites(input_age).convert_to_hours()
            print(f"{round(age_in_hours)} hours")

        elif option == 4 : 
            age_in_days = TimeUnites(input_age).convert_to_days(year)
            print(f"{round(age_in_days)} days")

        elif option == 5 : 
            age_in_weeks = TimeUnites(input_age).convert_to_weeks()
            print(f"{round(age_in_weeks)} weeks")

        elif option == 6 : 
            age_in_months = TimeUnites(input_age).convert_to_months()
            print(f"{round(age_in_months)} months")
        else : 
            print("Invalid choice .")
        retry  = input("Do you want to restart ?   ")
        if retry.lower() ==  "yes" :
            restart = True
        else :
            break
    except ValueError :
        print("Error ! you don't have to type a non-integer value. Please try again:")
   
    
