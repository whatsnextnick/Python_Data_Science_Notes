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

#Variable, and numbypy
# Alice, Bob and Carol have agreed to pool their Halloween candy and split it evenly 
# among themselves. For the sake of their friendship, any candies left over will be smashed. 
# For example, if they collectively bring home 91 candies, they'll take 30 each and smash 1.
# Write an arithmetic expression below to calculate how many candies they must smash for a given haul.
#_______________________________________

# Variables representing the number of candies collected by alice, bob, and carol
alice_candies = 121
bob_candies = 77
carol_candies = 109

# An expression involving alice_candies, bob_candies, and carol_candies
(alice_candies + bob_candies + carol_candies) % 3


#Complete the following block of code based on the doctstring

#any method is key to solving this with list comprehension
def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    return any(meals[meal] == meals[meal + 1] for meal in range(len(meals)-1))

#Kaggle's solution:
def menu_is_boring(meals):
    # Iterate over all indices of the list, except the last one
    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            return True
    return False

 
# In simplest terms, list comprehension is a concise way to create lists in Python. 
# It's like a compact loop that generates items for a list, all in one line.

#**Toygh one**
#A researcher has gathered thousands of news articles. But she wants to focus her attention on articles including a specific word. Complete the function below to help her filter her list of articles.

# The function should meet the following criteria:

# Do not include documents where the keyword string shows up only as a part of a larger word. For example, if she were looking for the keyword “closed”, you would not include the string “enclosed.”
# She does not want you to distinguish upper case from lower case letters. So the phrase “Closed the case.” would be included when the keyword is “closed”
# Do not let periods or commas affect what is matched. “It is closed.” would be included when the keyword is “closed”. But you can assume there are no other types of punctuation.
def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
#     stringified_lst = ' '.join(doc_list)
#     index_values = [doc_list.index(keyword.lower()) for word in doc_list if keyword.lower() in stringified_lst]
#     return index_values
#     lowcased_lst = [str_item.lower() for str_item in doc_list]
#     index_value = [i for i, lstr_items in enumerate(lowcased_lst) if keyword.lower() in lowcased_lst]
#     return index_value
    
    keyword = keyword.lower()  # Convert keyword to lowercase
    # Convert each document in doc_list to lowercase and remove periods and commas
    lowcased_lst = [str_item.lower().replace('.', '').replace(',', '') for str_item in doc_list]
    index_values = [i for i, str_item in enumerate(lowcased_lst) if keyword in str_item.split()]
    return index_values


