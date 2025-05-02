from collections import defaultdict


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if len(prerequisites) == 0:
            return True

        pre_map = defaultdict(list)

        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False

            if pre_map[crs] == []:
                return True

            visited.add(crs)

            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False

            visited.remove(crs)
            pre_map[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True
