import pandas as pd
import numpy as np

def main():
    data = pd.read_csv("歷史數據.csv")
    count = 0
    balls = []
    l = 6
    win = 0
    games = 0
    lose = 0
    prev = 'win'
    for idx, rows in data.iterrows():
        if idx < 6:
            continue
        temp = []
        for i in rows:
            temp.append(int(i))
        balls = []
        rec = np.zeros((40, 40, 40))
        maxx = -1
        for m in range(1, l + 1):
            to_check = []
            for i in range(5):
                to_check.append(int(data.iloc[idx - m][i]))
            for i in range(0, 5):
                for j in range(i + 1, 5):
                    for k in range(j + 1, 5):
                        a = to_check[i]
                        b = to_check[j]
                        c = to_check[k]
                        rec[a][b][c] += 1
                        if maxx < rec[a][b][c]:
                            maxx = rec[a][b][c]
        for i in range(1, 40):
            for j in range(i + 1, 40):
                for k in range(j + 1, 40):
                    if rec[i][j][k] == maxx:
                        balls.append([i, j, k])

                    
        last = np.zeros((len(balls)))
        present = []
        maxx = -1
        for m in range(1, l + 1):
            to_check = []
            for i in range(5):
                to_check.append(int(data.iloc[idx - m][i]))
            for p in range(len(balls)):
                i = balls[p]
                for k in range(0, 2):
                    for j in range(1 + k, 3):
                        if i[k] in to_check and i[j] in to_check:
                            last[p] += 1
                if last[p] > maxx:
                    maxx = last[p]
                    present = []
                    present.append(i)
                elif last[p] == last[p]:
                    present.append(i)
            
                        
        t = []
        for j in rows:
            t.append(int(j))
        
        num = 0
        for i in present[0]:
            if i in t:
                num += 1
        count += num
        # if prev == 'lose':
        #     games += 1
        #     if num == 1 or num == 2:
        #         win += 1
        #         prev = "win"
        #     else:
        #         lose += 1
        #         prev = 'lose'
        if num == 1 or num == 2:
            print("win", present[0], t)
            prev = 'win'
            win += 1
        else :
            print("lose", present[0], t)
            prev = 'lose'
            lose += 1
        games += 1
                

    print(win/ games)
    print(win, lose, games)
    print(count)

main()
        
