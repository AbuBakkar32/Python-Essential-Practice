import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

df = pd.read_csv('home_prices.csv')
# plt.scatter(df['area'], df['price'], marker='*', color='red', label='Data Area')
# plt.legend()
# plt.xlabel('Area measure')
# plt.ylabel('Price of Area')
# plt.title('Home Price and Area')
# plt.show()

x = df[['area']]
y = df['price']

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=.3)
print(xtrain)
print(xtest)

