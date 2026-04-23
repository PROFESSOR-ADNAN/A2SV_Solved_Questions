class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)

        for a, b in prerequisites:
            adj_list[a].append(b)

        white = 1
        gray = 2
        black = 3

        color = {k: white for k in range(numCourses)}

        def dfs(node):

            color[node] = gray

            if node in adj_list:
                for nei in adj_list[node]:
                    if color[nei] == white:
                        if dfs(nei):
                            return True
                    elif color[nei] == gray:
                        return True

            color[node] = black

        for i in range(numCourses):
            if color[i] == white:
                if dfs(i):
                    return False

        return True

