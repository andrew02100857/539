import pandas as pd
import numpy as np


def main():
    data = pd.read_csv("歷史數據.csv")
    # data = data.iloc[::-1]
    # data = data.reset_index()
    data = data.astype(int)
    rec = [[[0 for _ in range(40)] for _ in range(40)] for _ in range(40)]
    balls = []
    max = 0
    st = 394
    fin = 495
    for idx, rows in data.iterrows():
        if idx > fin or idx < st:
            continue
        temp = []
        for i in rows:
            temp.append((int(i)))
        for i in range(1, 38):
            for j in range(i + 1, 39):
                for k in range(j + 1, 40):
                    num = 0
                    if i in temp:
                        num += 1
                    if j in temp:
                        num += 1
                    if k in temp:
                        num += 1
                    if num == 0:
                        rec[i][j][k] += 1
                    if rec[i][j][k] > max:
                        max = rec[i][j][k]
                        balls = [(i, j, k)]
                    elif rec[i][j][k] == max:
                        balls.append((i, j, k))
    print(balls, rec[balls[0][0]][balls[0][1]][balls[0][2]])

main()