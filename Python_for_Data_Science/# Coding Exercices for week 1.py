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

# Control Flow / User Input:

"""A function which will allow user to travel to any year in the past or future as long as
 their age at that time is a prime number"""

def time_traveller():
    #Get the current year
    import datetime
    current_year = datetime.date.today().year

    #Get user's info
    past_or_pres = input("Would you like to travel to the past or present? ")
    age = input("How old are you? ")
    
    #function for determining the 
    def is_it_prime(n):
        if n <= 1:
           return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


    for i in range(int(age)):
          if is_it_prime(i) == True:
                print("You can travel to year " + str(int(current_year) - (i+1)))
                      


                             # print("you can travel to " + current_year - i)


time_traveller()






