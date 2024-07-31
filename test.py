import pandas as pd
import numpy as np


def main():
    data = pd.read_csv("歷史數據.csv")
    # data = data.iloc[::-1]
    # data = data.reset_index()
    data = data.astype(int)
    balls = [8,19,30]
    windows = 30
    fin = 495
    st = fin - windows - 1
    rec = [0, 0, 0, 0]
    for idx, rows in data.iterrows():
        times = 0
        if idx >= fin or idx < st:
            continue
        temp = []
        for i in rows:
            temp.append((int(i)))
        num = 0
        for i in balls:
            if i in temp:
                num += 1
        rec[num] += 1
        
    print(rec)
    print(rec[0] * 6129 - rec[1] * 15071 + rec[2] * 6129 + rec[3] * 240729)

main()