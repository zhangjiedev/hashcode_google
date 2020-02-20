from pp import getTest
from collections import Counter
filestring = "e_also_big.in"


def ZeroOnePack(f, c, w, N):
    for i in range(N, c, -1):    # might need to change +1 or -1
        f[i] = max(f[i], f[i-c] + w)


def AddNumber(cter, i, S, start=0):
    cre = cter.copy()
    for a in cter:
        cre[a + S[i]] = cter[a] + [i + start]
        cre[a] = cter[a]
    cre[S[i]] = [i + start]
    # print(len(cre))
    return cre


def backpack(M, S, start=0):
    # M = 17
    # N = 4
    # S = [2, 5, 6, 8]
    # M, N, S = getTest("d_quite_big.in") # d_quite_big c_medium
    fcounter = {}
    for i in range(len(S)):
        fcounter = AddNumber(fcounter, i, S, start)
        # print(i)
    t = sorted(list(fcounter.keys()), reverse=True)
    for k in t:
        if k <= M:
            # print(k)
            return k, fcounter[k]
    return 0, []

def adding(M, S):
    count = 0
    tps = []
    for a in range(len(S)):
        count += S[a]
        if count >= M:
            # print(count - S[a])
            return count - S[a], tps
        tps.append(a)
    return count, tps


def combine():
    M, N, S = getTest(filestring)
    a = 50
    if N > a:
        m_temp, add_arr = adding(M, S[a:])
        ans, ans_arr = backpack(M-m_temp, S[:a])
        # print(ans + m_temp)
        return ans + m_temp, add_arr + ans_arr
    return backpack(M, S)
# adding()
# backpack()


def re_combine():
    M, N, S = getTest(filestring)
    a = 40
    if N > a:
        m_temp, add_arr = adding(M, S[:N-a+1])
        ans, ans_arr = backpack(M-m_temp, S[N-a+1:], N-a+1)
        # print(ans + m_temp)
        return ans + m_temp, add_arr + ans_arr
    return backpack(M, S)


def shelladding():
    M, N, S = getTest(filestring)
    adding(M, S)

def output(filename):
    f = open(filename, "w")
    num, ans_arr = re_combine()
    f.write(str(len(ans_arr)))
    f.write("\n")
    for a in ans_arr:
        f.write(str(a))
        f.write(" ")
    f.close()


output("e_also_big.out")
# combine()
# shelladding()
