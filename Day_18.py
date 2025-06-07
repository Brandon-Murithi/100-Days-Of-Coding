#create a series
import pandas as pd
numbers = pd.Series([10,20,30,40,50])
print("Series is:", numbers) #Series will output as a single column

#creating  a DataFrame
data = {
    "Name": ["Alice","Bob", "Charlie"],
    "Age": [22, 30, 34],
    "Salary": [50000,60000,65000]
}

df = pd.DataFrame(data)
print("DataFrame is: \n", df)#DataDrame is both column and rows

#DataFrame manipulation
print("Age column is:\n", df["Age"])
print("Salary column is:\n", df["Salary"])

#Adding new column to DataFrame 
df["Department"]= ["HR","Analysis","IT"]
print("DataFrame after adding Department column:\n", df)   

older_than_23 = df[df["Age"]> 23]
print("People older than 23:\n", older_than_23)


#Let's create a new Series
points = pd.Series([100,200,300])
print("New Series is:", points)


#Creating a new DataFrame
players = {
    "Player": ["Brandon", "Norman", "Eliane"],
    "Score":[250, 200, 240]
}

df_players = pd.DataFrame(players)
print(df_players)