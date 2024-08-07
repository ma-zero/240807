import pandas as pd
import matplotlib.pyplot as plt

col_names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pd.read_csv('./data/pima-indians-diabetes.data.csv', names=col_names)

# print(data)
# print(data['preg'])
# print(data.head(5))
# print(data['preg'].head(5))
# print(data.describe())

plt.clf()
plt.hist(data['preg'])
plt.show()
plt.savefig("./age.png")

# data.describe().to_csv("./result/describe.csv")