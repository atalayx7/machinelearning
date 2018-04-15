# Atalay Samet Ergen 130201014
import numpy as np

with open("TrainingDat2.txt") as x:
    A = []
    B = []
    x = x.readlines()
    s = []
    riskFactor = []
    for i in x:

        i = i.strip()
        i = i.split(",")

        if i[1] == "honda":
            i[1] = 1
        elif i[1] == "peugot":
            i[1] = 2
        elif i[1] == "renault":
            i[1] = 3
        elif i[1] == "toyota":
            i[1] = 4
        elif i[1] == "volkswagen":
            i[1] = 5
        elif i[1] == "volvo":
            i[1] = 6

        B.append(i)
    for i in B:
        if i[2] == "hatchback":
            i[2] = 1
        elif i[2] == "sedan":
            i[2] = 2
        elif i[2] == "wagon":
            i[2] = 3
        elif i[2] == "hardtop":
            i[2] = 4
        elif i[2] == "convertible":
            i[2] = 5
        i.insert(0, 1)
        i[1] = int(i[1])
        i[4] = int(i[4])

    for i in B:
        riskFactor.append(i[1])
        i.pop(1)

    x = np.array(B)
    inverse = np.linalg.inv(np.matmul(x.transpose(), B))

    result = (np.matmul(inverse, np.matmul(x.transpose(), riskFactor)))

    print(result)
