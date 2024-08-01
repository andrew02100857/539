import pandas as pd
import numpy as np



def main():
    data = pd.read_csv("歷史數據.csv")
    rec = np.zeros((40, 40, 40))
    l = 6

    windows = 0
    little = 6
    balls = []
    win = 0
    games = 0
    n = 0
    present = []
    dbc = np.zeros((40, 40, 40))
    st = 500 - little * 20 - l
    for idx, rows in data.iterrows():
        if idx < st:
            continue
        test = []
        for i in range(5):
            test.append(int(rows[i]))

        if idx > st + l:
            if windows == 0:
                n = 0
                for i in range(1, 40):
                    for j in range(i + 1, 40):
                        for k in range(j + 1, 40):
                            if rec[i][j][k] > n:
                                n = rec[i][j][k]
                                balls = [[i, j, k]]
                            elif rec[i][j][k] == n:
                                balls.append([i, j, k])
                present = []
                last = np.zeros((len(balls)))
                for i in range(l):
                    t = []
                    for j in range(5):
                        a = int(data.iloc[idx - i][j])
                        t.append(a)
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
                    
                                
                                
                windows = little

            if windows > 0:
                
                nums = 0
                for i in present[0]:
                    for j in range(5):
                        if i == test[j]:
                            nums += 1

                if nums != 0:
                    win += 1
                    print("win")
                    print(present[0], test)
                # elif nums == 3:
                #     print("lose")
                #     print(present[0], test)
                else:
                    print("lose")
                    print(present[0], test)
                games += 1
                windows -= 1

            for i in range(0, 5):
                for j in range(i + 1, 5):
                    for k in range(j + 1, 5):
                        a = data.iloc[idx - l][i]
                        b = data.iloc[idx - l][j]
                        c = data.iloc[idx - l][k]
                        rec[a][b][c] -= 1

        for i in range(0, 5):
            for j in range(i + 1, 5):
                for k in range(j + 1, 5):

                    a = int(rows[i])
                    b = int(rows[j])
                    c = int(rows[k])

                    rec[a][b][c] += 1

                    if rec[a][b][c] > n:
                        n = rec[a][b][c]
                        balls = [a, b, c]
        
        


    
    
    print(win/games)
    print(win, games)
    print(342000 * win - games * 119070)
                

main()