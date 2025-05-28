numbers = [1,2,3,4,5]
squares = map(lambda x: x**2, numbers)

print(list(squares))

evens= list(filter(lambda x: x % 2==0 ,  numbers))
print(evens)

odds = list(filter(lambda x: x % 2 == 1,  numbers))
print(odds)

import seaborn as sns
import pandas as pd
df = sns.load_dataset('titanic')

older_than_30 = df[ df['age'].apply(lambda x: x > 30 if pd.notnull(x) else False)]
print(older_than_30[['age','sex', 'survived']])

pairs= [(1, 'b'), (2, 'c'), (3, 'a')]
sorted_pairs = sorted( pairs, key=lambda x: x[0])
print(sorted_pairs)
pairs= [(1, 'b'), (2, 'c'), (3, 'a')]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)

words = ['hello','world']
upper_words = list(map(lambda w: w.upper(), words))
print((upper_words))
lower_words= list(map(lambda w:w.lower(),upper_words))
print(lower_words)

pairs= [('zello', 2), ('world', 1)]
sorted_pairs = sorted(pairs, key=lambda x: x[0])
print(sorted_pairs)

# Filter out negative numbers
nums = [-2, -1, 0, 1, 2]
positives = list(filter(lambda x: x > 0, nums))
print(positives)  # Output: [1, 2]

# Filter out positive numbers
nums = [-2, -1, 0, 1, 2]
negatives = list(filter(lambda x: x <0, nums))
print(negatives)  # Output: [-2,-1 ]

words = ['hello','WORLD', 'PYTHON']
upper_words = list(filter(lambda w: w.isupper(), words))
print(upper_words)

words = ['hello','WORLD', 'PYTHON']
lower_words = list(filter(lambda w: w.islower(), words))
print(lower_words)