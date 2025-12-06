import pandas as pd


df = pd.read_csv("input_06_1.txt", header=None, delimiter=r"\s+")

sum=0

for col_num, _ in enumerate(df.columns):
    col = df[col_num]
    
    op = col.iloc[-1]

    if op == "+":
        sum += col.drop(col.index[-1]).astype(int).sum()
    elif op == "*":
      sum += col.drop(col.index[-1]).astype(int).prod()


print     (sum)
    