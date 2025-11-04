# Exercise 1
word1 = ("Coding")
word2 = (" is")
word3 = (" Cool")
Python = (word1 + word2 + word3)
print (Python)

#Exercise 2
C = 8, 10
total = sum(C)
print (f"The sum is {total}")

#exercise 4
user_input = input ("What is the Capital of France?")
if user_input.lower() == 'paris':
    print ("!CORRECT!")
else:
    print ("!WRONG!")

user_input = input ("What is the Capital of Germany?")
if user_input.lower() == 'berlin':
    print ("!CORRECT!")
else:
    print ("!WRONG!")

user_input = input ("What is the Capital of Spain?")
if user_input.lower() == 'madrid':
    print ("!CORRECT!")
else:
    print ("!WRONG!")

user_input = input ("What is the Capital of Italy?")
if user_input.lower() == 'rome':
    print ("!CORRECT!")
else:
    print ("!WRONG!")

user_input = input ("What is the Capital of UK?")
if user_input.lower() == 'london':
    print ("!CORRECT!")
else:
    print ("!WRONG!")

user_input = input ("What is the Capital of Greece?")
if user_input.lower() == 'athens':
    print ("!CORRECT!")
else:
    print ("!WRONG!")

user_input = input ("What is the Capital of Austria?")
if user_input.lower() == 'vienna':
    print ("!CORRECT!")
else:
    print ("!WRONG!")

user_input = input ("What is the Capital of Portugal?")
if user_input.lower() == 'lisbon':
    print ("!CORRECT!")
else:
    print ("!WRONG!")

user_input = input ("What is the Capital of Sweden?")
if user_input.lower() == 'stockholm':
    print ("!CORRECT!")
else:
    print ("!WRONG!")

user_input = input ("What is the Capital of Poland?")
if user_input.lower() == 'warsaw':
    print ("!CORRECT!")
else:
    print ("!WRONG!")

#Exercise 5
days_in_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

month = int(input("Enter the month number (1-12): "))

if month in days_in_month:
    if month == 2:
        leap = input("Is it a leap year? (yes/no): ").lower()
        if leap == "yes":
            print("February has 29 days in a leap year.")
        else:
            print("February has 28 days.")
    else:
        print(f"Month {month} has {days_in_month[month]} days.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")

#Exercise 6
password = 'python123'
max_attempts = 5

for attempt in range(1, max_attempts + 1):
    user_input = input("Please enter Password: ")

    if user_input == password:
        print("!CORRECT!")
        break
    else:
        if attempt < max_attempts:
            print("!WRONG! Try Again")
        else:
            print("!ACCESS DENIED! Maximum attempts reached")

#Exercise 7
for i in range(0, 51):
    print(i)

for i in range(50, -1, -1):
    print(i)

for i in range(30, 51):
    print(i)

for i in range(50, 9, -2):
    print(i)

for i in range(100, 201, 5):
    print(i)

#Exercise 8
names = ["jake", "zac", "ian", "ron", "sam", "dave"]

search_name = input("Enter the name to search for: ").lower()

if search_name in names:
    print(f"{search_name} was found in the list.")
else:
    print(f"{search_name} was not found in the list.")

#Exercise 9
def hello():
    print ("Hello")

def main():
   hello()

if __name__ == "__main__":
    main()

#Exercie 10
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")



