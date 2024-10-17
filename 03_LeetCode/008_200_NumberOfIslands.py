
# 문제 링크: https://leetcode.com/problems/number-of-islands/description/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        cnt = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    que = deque()
                    que.append([i, j])
                    visited[i][j] = True

                    while que:
                        cur_i, cur_j = que.popleft()
                        for dx, dy in direction:
                            next_i = cur_i + dx
                            next_j = cur_j + dy
                            if 0 <= next_i < m and 0 <= next_j < n:
                                if grid[next_i][next_j] == "1" and not visited[next_i][next_j]:
                                    que.append([next_i, next_j])
                                    visited[next_i][next_j] = True
                    cnt += 1
        return cnt