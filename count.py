import pandas as pd
import numpy as np

def main():
    data = pd.read_csv("new.csv")
    for idx, rows in data.iterrows():
        balls = []
        for i in rows:
            balls.append(int(i))
        
        three = []
        list = []
        t = []
        for i in range(5):
            t.append(int(rows[i]))

        for i in range(5):
            for j in range(i + 1, 5):
                for k in range(j + 1, 5):
                    if [t[i],t[j], t[k]] not in three:
                        three.append([t[i], t[j], t[k]])

        list.append(t)

    two_check = [0 for i in range(len(three))]
    two = []
    max = -1
    for i in range(len(three)):
        for b in list:
            for j in range(3):
                for k in range(j + 1, 3):
                    if three[i][j] in b or three[i][k] in b:
                        two_check[i] += 1
                        if two_check[i] > max:
                            two = [three[i]]
                            max = two_check[i]
                        elif two_check[i] == max:
                            two.append(three[i])

    count = 0
    num = 0
    test = two[0]
    for i in two:
        print(i)
    print(len(two))

main()