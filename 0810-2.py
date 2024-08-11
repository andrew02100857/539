import pandas as pd
import numpy as np

def main():
    data = pd.read_csv("歷史數據.csv")

    l = 100
    balls = []
    rec = np.zeros((40, 40))
    times = np.zeros((40))
    for idx, rows in data.iterrows():
        if idx < 1:
            continue

        now = []
        prev = []
        for i in range(5):
            now.append(int(rows[i]))
            prev.append(int(data.iloc[idx - 1][i]))
        
        if idx > l:
            max = -1
            test = []
            prev = []
            for i in range(5):
                prev.append(int(data.iloc[idx - 1]))
            for i in range(40):
                if rec[i] / times[i] > max:
                    max = rec[i]

        for i in range(5):
            p = prev[i]
            times[p] += 1
            for j in range(5):
                now = int(rows[j])
                rec[prev][now] += 1
        
                






    games = 0
    win = 0

main()