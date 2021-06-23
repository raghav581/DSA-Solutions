# Solution:{
    # soln function will calculate getProductSum for 'special' array 'arr' recursively.
def soln(arr, depth):
    res = 0
    for a in arr:
# checking if the given element is list or not
        if isinstance(a, list):
            res += soln(a, depth + 1)
        else:
            res += a
    return depth * res

    # This getProductSum function will return the final ProductSum of 'Special' Array "arr" passed to it.
def getProductSum(arr):
    return soln(arr, 1);
# }

# Input Function{
# In getSpecialArray, we take two inputs, i.e. x and y, for every element considering only INTEGER or list datatypes are present.
# 1. For x = 1, it means the y value will be considered as INTEGER.
# 2. For x = 2, it means the y value will be consideres as length of the list and it will generate a list of next y element for which we call getSpecialArray function recursively.
def getSpecialArray(N):
    res = list()
    for i in range(N):
        x, n = map(int, input().split())
        if x == 1:
            res.append(n)
        else:
            res.append(getSpecialArray(n))
    return res
# }


# Driver code starts.{
if __name__ == "__main__":

# Number of elements in parent array
    N = int(input()) 

# Take 'special' array input
    arr = getSpecialArray(N)

# generate getProductSum for 'special' array 'arr'
    res = getProductSum(arr)
    print(res)
# }
# Driver code ends.