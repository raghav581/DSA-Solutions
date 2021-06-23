def soln(res, i, tmp, arr):
    if i == len(arr):
        res.append(tmp)
        return res;
    res = soln(res, i + 1, tmp, arr)
    res = soln(res, i + 1, tmp + [arr[i]], arr)
    return res;

def powerSet(arr):
    res = list()
    return soln(res, 0, [], arr)

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    res = powerSet(arr)
    print(res) 