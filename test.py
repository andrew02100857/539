import pandas as pd
import numpy as np


def main():
    data = pd.read_csv("history.csv")
    # data = data.iloc[::-1]
    # data = data.reset_index()
    data = data.astype(int)
    
    
    rec = np.zeros((10, 10, 10))
    max = 0
    ans = []
    balls = [1, 2, 6]
    st = len(data) - 200
    for idx, rows in data.iterrows():
        if idx < st:
            continue
        test = []
        for i in rows:
            test.append(int(i))
        num = 0
        # for i in balls:
        #     if i in test:
        #         num += 1
        # if num == 2 or num == 1:
        #     max += 1
        for i in range(1, 10):
            for j in range(i + 1, 10):
                for k in range(j + 1, 10):
                    # for l in range(k + 1, 10):
                        # for m in range(l + 1, 10):
                            num = 0
                            if i in test:
                                num += 1
                            if j in test:
                                num += 1
                            if k in test:
                                num += 1
                            # if l in test:
                            #     num += 1
                            # if m in test:
                            #     num += 1
                            # print(num)
                            if num == 1 or num == 2:
                                rec[i][j][k] += 1
                                
                            if rec[i][j][k] > max:
                                max = rec[i][j][k]
                                ans = [i, j, k]
                                # print(ans, max)
    


    print(ans)
    print(max)

main()