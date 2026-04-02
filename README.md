# COP4533_Programming_Assignment_3

Christopher Bowers

UFID: 19272960

Dylan Esperto

UFID: 53118184

## Instructions to Run

Run this command from the repository root to run the algorithm:
```
python ./src/main.py
```

To test with example data `ex1.in`, run this command:
```
cat data/ex1.in | python ./src/main.py
```
This command should reproduce the output in `data/ex1.out`.

## Question 1: Runtime Graph

As the size of both input strings grow, a clear polynomial runtime pattern shows for larger n. 

![Runtime graph](img/graph.png "Runtime graph")

## Question 2: Recurrence Equation

OPT(i, j) represents the maximum value of a common subsequence of the first i 
characters of A and the first j characters of B, where v(c) represents the value 
of a given character c.

Base case: OPT(i, j) = 0 if i = 0 or j = 0

Match case: OPT(i, j) = OPT(i-1, j-1) + v(A[i]) if A[i] = B[j]

No match case: OPT(i, j) = max(OPT(i-1, j), OPT(i, j-1)) if A[i] != B[j]

The answer is OPT(m, n) where m and n are the lengths of A and B respectively.

Base cases: When either string is empty there are no characters to match, 
so the maximum value is 0.

Match case: When A[i] = B[j] we take the match and add its value v(A[i]) 
to the best solution on the remaining prefixes OPT(i-1, j-1).

No match case: When A[i] != B[j] we cannot take both characters, so we take 
the best of skipping i in A or skipping j in B.

# Question 3: Big O

```
A = a_1 ... a_m
B = b_1 b_2 ... b_n
v(i) = value of character i
Calc-OPT:
    M = 2d array of size n x m initialized to zeros
    for i = 1 to m + 1
        for j = 1 to n + 1
            if a_(i-1) == b_(j-1)
                M[i][j] = M[i-1][j-1] + v(a_(i-1))
            else
                M[i][j] = max(M[i-1][j], M[i][j-1])
    return M[m][n]
```

The algorithm is O(mn).