# COP4533_Programming_Assignment_3





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