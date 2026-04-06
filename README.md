# Highest Value Longest Common Subsequence - Programming Assignment 3

- **Name:** Carlos Felipe
- **UFID:** 70583368

## Description
Given two strings A and B and an alphabet where each character has a value, this program finds the common subsequence that maximizes total character value using dynamic programming.

## How to Run

### Run the solver
```
python3 src/hvlcs.py <input_file>
```

Example:
```
python3 src/hvlcs.py tests/example.in
```

### Generate test files
```
python3 src/generate_tests.py
```
This creates 10 test files in `data/` with string lengths ranging from 25 to 2000.


## Project Structure
```
├── README.md
├── src/
│   ├── hvlcs.py               # Main solver
│   ├── generate_tests.py      # Test file generator
│   └── benchmark.py           # Runtime benchmarking and graphing
├── data/                      # Generated test input files
└── tests/
    ├── example.in             # Worked example from assignment
    └── example.out            # Expected output for example
```

## Input Format
```
K
x1 v1
x2 v2
...
xK vK
A
B
```
- K is the number of characters in the alphabet
- Each of the next K lines contains a character and its integer value
- A is the first string
- B is the second string

## Output Format
```
<max_value>
<optimal_subsequence>
```

## Question 1: Empirical Comparison
![Runtime Graph](data/runtime_graph.png)

The graph shows that runtime grows quadratically as string length increases,
which is consistent with the O(m * n) time complexity of the DP algorithm.

## Question 2: Recurrence Equation
```
Let OPT(i, j) represent the maximum value of a common subsequence of A[1..i] and B[1..j], and let v(c) be the value of character c.
```
 
**Base cases:**
```
OPT(i, 0) = 0    for all i
OPT(0, j) = 0    for all j
```
 
**Recurrence:**
```
OPT(i, j) = 0                                  if i = 0 or j = 0
          = v(A[i]) + OPT(i-1, j-1)            if A[i] = B[j]
          = max( OPT(i-1, j), OPT(i, j-1) )    if A[i] != B[j]
```
 
**Why this is correct:**
When A[i] == B[j], we have a matching character. Including it in our
subsequence is always optimal because character values are nonnegative,
so adding v(A[i]) can never decrease the total value. We then solve
the remaining subproblem on A[1..i-1] and B[1..j-1].
 
When A[i] != B[j], these two characters cannot both end a common
subsequence. We must skip at least one, so we take the better of
skipping the last character of A or the last character of B.
 
The base cases hold because a common subsequence with an empty
string has no characters and therefore a value of 0.
 
**Answer = OPT(m, n)**

## Question 3: Big-Oh
**Pseudocode:**
```
Input: strings A, B, value function v
for i = 0 to m:    OPT[i][0] = 0
for j = 0 to n:    OPT[0][j] = 0
 
for i = 1 to m:
    for j = 1 to n:
        if A[i] == B[j]:
            OPT[i][j] = v(A[i]) + OPT[i-1][j-1]
        else:
            OPT[i][j] = max(OPT[i-1][j], OPT[i][j-1])
 
return OPT[m][n]
```
 
**Runtime: O(mn)** — The algorithm fills an (m+1) x (n+1) table. Each cell requires O(1) work since it only compares characters and looks up at most three previously computed values. The two nested loops iterate m x n times total, giving O(mn) time and O(mn) space for the table.