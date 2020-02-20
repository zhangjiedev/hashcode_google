from pp import getTest
from backpack_problem import backpack, output


def inputs():
    M, N, S = getTest("e_also_big.in")
    f = open("e_also_big.out", "w")
    num, ans_arr = method2combine(M, S)
    f.write(str(len(ans_arr)))
    f.write("\n")
    for a in ans_arr:
        f.write(str(a))
        f.write(" ")
    f.close()


def method2combine(M, S):
    S2 = []
    for i in reversed(range(len(S))):
        if S[i] < M:
            S2 = S[:i+1]
            break
    if len(S2) > 30:
        sm, ans_arr = method2(M, S2)
    else:
        sm, ans_arr = backpack(M, S2)
    return sm, ans_arr

def method2(M, S):
    exc, tps = adding(M, S)
    pin = tps[0]
    # pin is the index of first number so that it and every number behind it add to just exceed M
    max_reduce = sum(S[:pin])
    # max_reduce is the maximum number for which we need to select up to
    upper_bound = len(S)
    # this is the upper bound we need to select
    if S[-1] > max_reduce:
        for i in range(pin, len(S)):
            if S[i] > max_reduce:
                upper_bound = i
    # find the least error:
    maxM = exc - S[pin]
    fin_arr = []
    for j in range(pin, upper_bound):
        sm, ans_arr = method2combine(M - exc + S[j], S[:pin])
        curr_err = exc - S[j] + sm
        if curr_err > maxM:
            maxM = curr_err
            fin_arr = ans_arr + list(range(pin, j)) + list(range(j+1, len(S)))
        if maxM == M:
            break
    print(maxM)
    return maxM, fin_arr


def adding(M, S):
    count = 0
    tps = []
    for a in reversed(range(len(S))):
        count += S[a]
        tps.append(a)
        if count >= M:
            # print(count)
            return count, list(reversed(tps))
    return count, list(reversed(tps))

inputs()
