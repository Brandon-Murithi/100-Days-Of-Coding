import pandas as pd
df = pd.read_csv('train.csv')
df[['col1','col2']]
print(df.columns)
df[['PassengerId','Survived']]

df.loc[0:4,['PassengerId']]
df.iloc[0:3, [5]] #the 0:3 shows the first 3 rows, and [5] shows the 6th column

df[df['Age']>25]
filtered_df = df[df['Age'] > 25]
print(filtered_df['Cabin'])

df['new_col']=df['Fare'].apply(lambda x:x*2)
print(df['new_col'].head)

df.rename(columns = {'PassengerId': 'ID'})

df.drop_duplicates(inplace = True)
print(df)

