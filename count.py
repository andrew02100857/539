import pandas as pd
import numpy as np



def main():
    data = pd.read_csv("new.csv")
    rec = np.zeros((40, 40, 40))
    balls = []
    n = 0
    for idx, rows in data.iterrows():
        temp = []
        for i in rows:
            temp.append(int(i))
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
                    balls.append([i, j, k])
    present = []
    last = np.zeros((len(balls)))
    for idx, rows in data.iterrows():
        t = []
        for j in rows:
            t.append(int(j))

        maxx = -1
        for b in range(len(balls)):
            select = balls[b]
            for j in range(3):
                for k in range(j + 1, 3):
                    if select[j] in t and select[k] in t:
                        last[b] += 1
            if maxx < last[b]:
                maxx = last[b]
                present = [select]
            elif maxx == last[b]:
                present.append(select)
    print(present)
main()
        