import pandas as pd
import random
import seaborn as sns
import matplotlib.pyplot as plt

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
#print(pd.get_dummies(data['whoAmI']))
data.loc[data['whoAmI'] == 'human', 'human'] = "1"
data.loc[data['whoAmI'] == 'robot', 'robot'] = "1"
data = data.fillna("0")
print(data)