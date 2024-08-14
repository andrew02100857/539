import pandas as pd
import numpy as np

def main():
    data = pd.read_csv("history.csv")
    games = 0
    win = 0
    lose = 0
    balls = [1, 37]
    a = 1
    b = 37
    rec = np.zeros((40, 40))
    for idx, rows in data.iterrows():
        games += 1
        temp = []
        for i in rows:
            temp.append(int(i))
        if a in temp and b in temp:
            win += 1
        # for i in range(5):
        #     for j in range(i + 1, 5):
        #         rec[temp[i]][temp[j]] += 1
        
    max = -1
    num = []
    # for i in range(1, 40):
    #     for j in range(i + 1, 40):
    #         if max < rec[i][j]:
    #             max = rec[i][j]
    #             num = [i, j]
        

    print(win, games)

main()
