import pandas as pd
import numpy as np
import math


def main():
    data = pd.read_csv("歷史數據.csv")
    data = data.astype(int)
    balls = []
    win = [0 for i in range(40)]
    rec = [0 for i in range(40)]
    windows = 0
    times = 0
    for idx, rows in data.iterrows():
        if windows == 6:
            windows = 0
            times += 1
            for i in range(39):
                if win[i + 1] > 1:
                    rec[i + 1] += 1
            win = [0 for i in range(40)]
        for i in range(5):
            temp = rows.iloc[i]
            win[temp] += 1
        windows += 1
    
    for i in range(1,40):
        print(f"數字:{i}一周內連出率:{round(rec[i] / times * 100, 2)}%")

main()