import pandas as pd
import seaborn as sns #both pandas and seaborn are libraries

df=sns.load_dataset('titanic')#.load_dataset is a function in seaborn that loads the titanic dataset
df.head() #is a method, it belongs to df object
print(df.shape)# returns the dimensions of the dataframe
print(df.columns)# returns the columns of the dataframe
print(df.info('age'))# returns the information of the dataframe
print(df.describe())# returns the description of the dataframe
print(df.isnull().sum())

