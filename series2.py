import pandas as pd

data = pd.Series([10,20,30,40,50], index = ["A", "B", "C", "D", "E"])

# index 안에 있는 B의 값을 바꾸기
data["B"] = 60

print(data, "\n", data["B"])