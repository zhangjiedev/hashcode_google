
def calculate(file_name):
    with open(file_name, 'r') as f:
        M, N = map(int, f.readline().strip('\n').split(' '))
        slices = list(map(int, f.readline().strip('\n').split(' ')))

    # print(M, N)
    # print(slices)

    result = []
    i = 0
    total = 0
    while total < M:
        result.append(i)
        total += slices[i]
        i += 1
    result.pop(-1)
    i -= 1
    total -= slices[i]

    while i < N:
        result_index = len(result) - 1
        j = result[result_index]
        if total + (slices[i] - slices[j]) > M:
            return total, result

        while total + (slices[i] - slices[j]) <= M and result_index >= 0:
            result_index -= 1
            j = result[result_index]

        # if result_index == len(result) - 1:    # if can't change the last one
        #     return total, result

        if total + (slices[i] - slices[j]) > M:
            total += (slices[i] - slices[result[result_index + 1]])
            result.pop(result_index + 1)
        else:
            total += (slices[i] - slices[j])
            result.pop(result_index)

        result.append(i)

        i += 1

    return total, result


if __name__ == '__main__':
    total, result = calculate('data/e_also_big.in')
    assert len(result) == len(set(result))
    print(total)
    print(result)