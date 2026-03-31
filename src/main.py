if __name__ == '__main__':
    with open('../data/ex1.in', 'r') as file:
        lines = [lines.strip() for lines in file.readlines()]

    n = int(lines[0])

    values = {}

    for i in range(n):
        char, value = lines[i+1].split()
        values[char] = int(value)

    str1 = lines[n + 1]
    str2 = lines[n + 2]



#we are going to use a 2D array and the general format of find longest subsequence to track the total weight of a subsequence
#OPT = {

arr = [[0]*len(str2)] * len(str1)


