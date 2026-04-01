def parse_input():
    n = int(input())

    values = {}

    for i in range(n):
        char, value = input().split()
        values[char] = int(value)

    str1 = input()
    str2 = input()

    return (n, values, str1, str2)


def opt(n, values, str1, str2):
    #we are going to use a 2D array and the general format of find longest subsequence to track the total weight of a subsequence
    #OPT = {
    m = len(str1)
    n = len(str2)
    arr = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                arr[i][j] = arr[i-1][j-1] + values[str1[i-1]]
            else:
                arr[i][j] = max(arr[i-1][j], arr[i][j-1])

    print(arr)


#backtracking


if __name__ == '__main__':
    input_tuple = parse_input()
    opt(*input_tuple)