import pandas as pd
import matplotlib.pyplot as plt

content = pd.read_csv('/Users/CnuipMac/Documents/NLP/titanic.csv')
content = content.dropna()
age_with_fares = content[
    (content['Age'] > 22) & (content['Fare'] < 400) & (content['Age'] < 60)
]
sub_fare = age_with_fares['Fare'].tolist()
sub_age = age_with_fares['Age'].tolist()

plt.scatter(sub_age, sub_fare)
plt.show()
