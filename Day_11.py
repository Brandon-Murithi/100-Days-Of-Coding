#DAY 11: LIST COMPREHENSIONS
#creating lists using list comprehensions
numbers = [1, 2, 3, 4, 5]
print(numbers)
squares = [n**2 for n in numbers]#the 'for' represents a for loop
print(squares)

import seaborn as sns
df= sns.load_dataset('titanic')
print(df['age'])
avg_age = df['age'].mean()
print(avg_age)

import pandas as pd
# Create a list of ages, replacing missing values with the average
ages = [age if not pd.isnull(age) else avg_age for age in df['age']]
print(ages[:10])# Display the first 10 ages


	
print(ages[:10])# Display the first 10 ages
