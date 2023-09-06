# Coding Exercices for week 1

# String Manipulation:
str1 = "hello"
str2 = "world"

statement = str1 + " " + str2
print(statement)
print(statement.upper())
print(statement.lower())
print(statement.title())

statement2 = " how are you?"
statement += statement2
print(statement.split(" ")[1])
print(statement)
print("____________________________")
# Control Flow / User Input:

"""A function which will allow user to travel to any year in the past or future as long as
 their age at that time is a prime number"""

import datetime

def is_it_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def time_traveller():
    # Get the current year
    current_year = datetime.date.today().year
    print(f"Current Year: {current_year}")

    # Get user's info
    while True:
        past_or_pres = input("Would you like to travel to the past or future? ").lower()
        if past_or_pres in ["past", "future"]:
            break
        print("Please enter either 'past' or 'future'.")

    while True:
        try:
            age = int(input("How old are you? "))
            break
        except ValueError:
            print("Please enter a valid age.")

    # Loop for 'past' selection from user (show the past years they can travel to)
    if past_or_pres == "past":
        for i in range(age):
            if is_it_prime(i):
                year = current_year - (age - i)
                print(f"You can travel in the past, to year {year} | Age: {i}")

    # Loop for 'future' selection from the user (shows future years they can travel to)
    elif past_or_pres == "future":
        for i in range(age, age + 20):  # Assuming a max of 20 years into the future for simplicity
            if is_it_prime(i):
                year = current_year + (i - age + 1)
                print(f"You can travel to the future, to year {year} | Age: {i}")

time_traveller()







