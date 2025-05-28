#Day 2: **PERSONALISED MESSAGE PROGRAM
name="Brandon".upper()
age="20"
hobby="drawing"
message="{} is {} years old".format(name,age)
print(message)
message= f"{name} is {age} years old"
print(message)



#Day 3: **LISTS
tasks=["Talk with Florence","Assistance from friends","Apply more"]
print(tasks)
tasks.insert(1,"call dad")
tasks.remove("call dad")
tasks[0]="buy groceries"
if "buy groceries" in tasks:
    print("Healthy eating tonight!")



#Day 4: **DICTIONARIES
house = {}
house = {
 "tables":4,
 "chairs": 10
}
print(house)
print(
 f"{house["chairs"]}\n"
 f"{house["tables"]}\n"
)
house["rooms"] =9
print(house)
house.get("chairs")
house.keys()
house.values()



#Day 5: **CONDITIONALS
is_coding= True #bool type

if is_coding == True: print(" You a G!")
else: print("You're not doing your best!?!")

rooms = int(input ("Enter your input:  "))#int type
if rooms == 9: print("You got that right!")
elif rooms > 9: print("Mans house bigg!")
else: print("Thas a bedsitter!")



#Day 6: **LOOPS
numbers=[ 10,20,30,40,50]

total=0
for num in numbers:
    total+=num 

average = total / len(numbers)
maximum = numbers [0]
minimum = numbers [0]
for num in numbers:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

print(f"sum is {total}\n"
      f"average is {average}\n"
      f"max is {maximum}\n"
      f"min is {minimum}\n"
      
      
      )



#Day 7: **FUNCTIONS
def add_numbers(num1,num2):
    return num1 + num2
def subtract_numbers(num1,num2):
    return num1 - num2
def multiply_numbers(num1,num2):
    return num1 * num2



#Day 8: ERROR HANDLING
def divide_by_two(number):
    try:
        return number / 2
    except TypeError:
        return "Give me a number!"

print(divide_by_two(10))      # Output: 5.0
print(divide_by_two("test"))  # Output: Give me a number!



#Day 9: 
def add_ten(number):  
    try:  
        return number + 10  
    except TypeError:  
        return "Error: Give me a number, not nonsense."  

print(add_ten("hello"))  # Output: Error message  



#Day 10: **PANDAS
import pandas as pd
import seaborn as sns

df= sns.load_dataset('titanic')

survived_count = df['survived'].sum()#how many survived
print(f"Number of passengers who survived: {survived_count}")

survival_by_gender= df.groupby('sex')['survived'].mean()#survival rate by  gender
print(f"Survival rate by gender: {survival_by_gender}")

avg_age = df.groupby('survived')['age'].mean()
print(f"Average age of passengers: {avg_age}")

print(f"Missing values in each column/n")
print(df.isnull().sum())

words = ['hello','WORLD', 'PYTHON']
upper_words = list(filter(lambda w: w.isupper(), words))
print(upper_words)

words = ['hello','WORLD', 'PYTHON']
lower_words = list(filter(lambda w: w.islower(), words))
print(lower_words)