import pandas as pd
import numpy as np



def main():
    data = pd.read_csv("new.csv")
    rec = np.zeros((40, 40, 40))

    n = 0
    for idx, rows in data.iterrows():
        temp = []
        for i in range(5):
            temp.append(rows[i])
        for i in range(0, 5):
            for j in range(i + 1, 5):
                for k in range(j + 1, 5):
                    a = temp[i]
                    b = temp[j]
                    c = temp[k]
                    rec[a][b][c] += 1
                    if n < rec[a][b][c]:
                        n = rec[a][b][c]
    for i in range(1, 40):
        for j in range(i + 1, 40):
            for k in range(j + 1, 40):
                if rec[i][j][k] == n:
                    print(i, j, k)
    print(n)
main()
        