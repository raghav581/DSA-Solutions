def solve(res, S, i, s, keys):
    if(i == len(S)):
        res.append(s)
        return res
    for k in keys[S[i]]:
        res = solve(res, S, i + 1, s + k, keys)
    return res

def numbers(S, keys):
    return solve([], S,0,"", keys)

def Print(arr):
    for a in arr:
        print(a)

if __name__ == "__main__":
    keypad = {"0" : "0", "1" : "1", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
    N = input()
    res = numbers(N, keypad)
    Print(res)