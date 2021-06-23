def soln(res, curr, steps, stairs):
    if curr == stairs:
        res += 1
        return res
    for i in range(1, steps + 1):
        if i + curr <= stairs:
            res = soln(res, curr + i, steps, stairs)
        else:
            break
    return res
    
def calculateWays(stairs, steps):
    return soln(0, 0, steps, stairs)

if __name__ == "__main__":
    stairs, steps = map(int,input().split())
    res = calculateWays(stairs, steps)
    print(res)
