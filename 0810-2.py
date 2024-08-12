import pandas as pd
import numpy as np

def main():
    data = pd.read_csv("歷史數據.csv")

    l = 100
    balls = []
    rec = np.zeros((40, 40))
    times = np.zeros((40))
    win = 0
    games = 0
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
            sec = -1
            thi = -1
            rank = [0, 0, 0]
            cc  = [0, 0, 0]
            for i in range(5):
                p = prev[i]
                for j in range(40):
                    chance = rec[p][j] / times[p]
                    if chance > max:
                        thi = sec
                        sec = max 
                        max = chance
                        
                        rank[2] = rank[1]
                        cc[2] = cc[1]
                        rank[1] = rank[0]
                        cc[1] = cc[0]
                        rank[0] = j
                        cc[0] = times[p]
                        
                    elif chance > sec:
                        thi = sec
                        rank[2] = rank[1]
                        sec = chance
                        rank[1] = j
                        cc[2] == cc[1]
                        cc[1] = times[p]
            
                    
                    elif chance > thi:
                        thi = chance
                        rank[2] = j
                        cc[2] = times[p]
            
            if cc[0] > 12:
                games += 1
                num = 0
                for i in rank:
                    if i in now:
                        num += 1
                for i in range(3):
                    cc[i] = round(int(cc[i]), 2)
                # print(cc)
                if num == 1 or num == 2:
                    win += 1
                    print("win", rank, now)
                    print(cc)
                else:
                    print("lose", rank, now)
                    print(cc)
                        

        for i in range(5):
            p = prev[i]
            times[p] += 1
            for j in range(5):
                n = now[j]
                rec[p][n] += 1
        if idx > l:
            prev = []
            now = []
            for i in range(5):
                prev.append(int(data.iloc[idx - l][i]))
                now.append(data.iloc[idx - l + 1][i])
            for i in prev:
                for j in now:
                    rec[i][j] -= 1
                times[i] -= 1

    print(round(win/games, 2), win, games)
                







main()