import pandas as pd
data = {'이름': ['Alice', 'Bob', '홍길동'], '나이': [25, 30, 26], '성별': ['여', '남', '남']}

df = pd.DataFrame(data, index=['A', 'B', 'C'])
print(df)

# df.to_csv("./data.csv")
# 7줄 to_csv = 내가 가지고 있는 파일을 CSV로 만들겠다.

