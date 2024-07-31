import pandas as pd
import numpy as np



def main():
    data = pd.read_csv("歷史數據.csv")
    rec = np.zeros((40, 40, 40))
    len = 12

    windows = 0
    little = 6
    balls = []
    win = 0
    games = 0
    n = 0
    present = []
    dbc = np.zeros((40, 40, 40))
    st = 493 - little * 20 - len
    for idx, rows in data.iterrows():
        if idx < st:
            continue
        test = []
        for i in range(5):
            test.append(int(rows[i]))

        if idx > st + len:
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
                for i in balls:
                    nums = 0
                    for j in i:
                        if j in test:
                            nums += 1
                    if num
                windows = little

            if windows > 0:
                
                nums = 0
                for i in present:
                    for j in range(5):
                        if i == test[j]:
                            nums += 1

                if nums != 0:
                    win += 1
                    print("win")
                    print(present, test)
                elif nums == 3:
                    print("lose")
                    print(present, test)
                else:
                    print("lose")
                    print(present, test)
                games += 1
                windows -= 1

            for i in range(0, 5):
                for j in range(i + 1, 5):
                    for k in range(j + 1, 5):
                        a = data.iloc[idx - len][i]
                        b = data.iloc[idx - len][j]
                        c = data.iloc[idx - len][k]
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