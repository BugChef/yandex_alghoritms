import sys


def find_max_length(A, B, n, m):
    dp = {}
    maxm = 0

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):

            if A[i] == B[j]:
                if i + 1 in dp and j + 1 in dp[i + 1]:
                    dp[i] = {j: dp[i + 1][j + 1] + 1}
                else:
                    dp[i] = {j: 1}

                if dp[i][j] > maxm:
                    maxm = dp[i][j]

    return maxm


n = int(sys.stdin.readline().strip())
n_matches = sys.stdin.readline().strip().split()
m = int(sys.stdin.readline().strip())
m_matches = sys.stdin.readline().strip().split()
print(find_max_length(n_matches, m_matches, n, m))
