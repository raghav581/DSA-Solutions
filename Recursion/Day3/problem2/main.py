def solve(Str, Str1, Str2, i, j, k):
    if len(Str) != len(Str1) + len(Str2):
        print("hi")
        return False
    if i == len(Str1) and j == len(Str2):
        return True
    if i < len(Str1) and j < len(Str2) and Str1[i] == Str2[j] and Str[k] == Str1[i]:
        x = solve(Str, Str1, Str2, i + 1, j, k + 1)
        if x:
            return x
        return solve(Str, Str1, Str2, i, j + 1, k + 1)
    elif i < len(Str1) and Str1[i] == Str[k]:
        return solve(Str, Str1, Str2, i + 1, j, k + 1)
    elif j < len(Str2) and Str2[j] == Str[k]:
        return solve(Str, Str1, Str2, i, j + 1, k + 1)
    else:
        return False

def check(S, S1, S2):
    return solve(S, S1, S2, 0, 0, 0)

if __name__ == "__main__":
    one = input()
    two = input()
    three = input()
    res = check(three, one, two)
    print(res)