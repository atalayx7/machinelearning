# Atalay Samet Ergen
import numpy as np

with open("TrainingDat1.txt") as x:
    A = []
    B = []
    x = x.readlines()
    s = []
    for i in x:
        A.append(" ".join(i.split()))
    for i in A:
        i = i.split(" ")
        B.append(i)
    for i in B:
        s.append(i[3])
        i.insert(0, str(1))
        i.pop()

    x = np.array(B)
    y = x.astype(np.float)  # y= B in float type
    c = np.array(y)

    j = np.array(s)
    l = j.astype(np.float)  # y= B in float type
    m = np.array(l)

    # print(np.matmul(c.transpose(),y))   #transpose of X multiple by x vector

    # print(np.matmul(c.transpose(),m)) #transpose of X nultiple by y vector

    inverse = np.linalg.inv(np.matmul(c.transpose(), y))

    result = (np.matmul(inverse, np.matmul(c.transpose(), m)))

    finalResult = result[0] + result[1] * 6 + result[2] * 5 + result[3] * 8
    print(finalResult)
