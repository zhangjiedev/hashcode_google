import numpy as np
def getTest(filename: str):
    f = open('data/'+ filename, 'r')
    first = f.readline()
    second = f.readline()
    f.close()
    M, N = first.split()
    M, N = int(M), int(N)
    S = np.array([int(i) for i in second.split()])
    return M, N, S

# print(getTest('a_example.in'))