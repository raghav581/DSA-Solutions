def soln(res, arr1, arr2):
    if(len(arr2) == 0):
        if arr1 not in res:
            res.append(arr1)
        return res
    for i in range(len(arr2)):
        val = arr2[i]
        tmp = arr2[:]
        del tmp[i]
        res = soln(res, arr1 + [val], tmp)
    return res

def comb(arr):
    res = list()
    return soln(res, [], arr)

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    res = comb(arr)
    print(res)