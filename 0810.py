import pandas as pd
import numpy as np

def main():
    data = pd.read_csv("歷史數據.csv")
    l = 6
    games = 0
    win = 0
    lose = 0
    for idx, rows in data.iterrows():
        if idx < l:
            continue
        balls = []
        for i in rows:
            balls.append(int(i))
        
        three = []
        list = []
        for c in range(1, l + 1):
            t = []
            for i in range(5):
                t.append(int(data.iloc[idx - c][i]))

            for i in range(5):
                for j in range(i + 1, 5):
                    for k in range(j + 1, 5):
                        if [t[i],t[j], t[k]] not in three:
                            three.append([t[i], t[j], t[k]])

            list.append(t)

        # print(list)
        two_check = [0 for i in range(len(three))]
        two = []
        max = -1
        for i in range(len(three)):
            for b in list:
                for j in range(3):
                    for k in range(j + 1, 3):
                        if three[i][j] in b and three[i][k] in b:
                            two_check[i] += 1
                            if two_check[i] > max:
                                two = [three[i]]
                                max = two_check[i]
                            elif two_check[i] == max:
                                two.append(three[i])
        one = []
        one_check = [0 for i in range(len(two))]
        max = -1
        # print(two)
        # for i in range(len(two)):
        #     for b in list:
        #         for k in two[i]:
        #             if k in b:
        #                 one_check[i] += 1
        #                 if one_check[i] > max:
        #                     max = one_check[i]
        #                     one = [two[i]]
        #                 elif one_check == max:
        #                     one.append(two[i])
        count = 0
        num = 0
        test = two[0]
        if len(two) < 5:
            games += 1
            for i in test:
                if i in balls:
                    num += 1
            if num == 1 or num == 2:
                print("win", two, balls)
                win += 1
            else:
                print("lose", two, balls)
                lose += 1
                # print(len(one))
    print(round(win/games, 3), games, win)

main()
        
            
        


            

                    

            

                                     

                

