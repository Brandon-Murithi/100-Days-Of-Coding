import pandas as pd
data = {

    "Name": ["Alice", "Bob", None,  "Eve"],
    "Age": [25, 30, 7,-22],
    "Salary": [50000, 60000, 70000, None]
    }
df =pd.DataFrame(data)
print("Original DataFrame",df)

print("\nOriginal DataFrame missing values",df.isnull().sum())

df.loc[df['Age']<0, "Age"]= None
mean_age = df['Age'].mean()
print("Mean age is:", mean_age)
mean_age = df['Age'].mean(skipna=True)

print("Mean age without missing values is:",mean_age)

df["Name"] = df["Name"].fillna("Unknown")
print("Name column after filling missing values:", df["Name"])
print("DataFrame after filling missing values:\n", df)

df["Age"]=df["Age"].fillna(mean_age)
print("DataFrame after filling missing values in Age column:\n", df["Age"])

df["Salary"] = df["Salary"].fillna(0)
print("DataFrame after filling missing values in Salary column:\n", df["Salary"])

print("Dataframe after filling all missing values:\n", df)
print("DataFrame missing values:",df.isnull())