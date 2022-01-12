class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        pd = dict()
        visited = set()
        
        # Convert prerequisites to dict
        for n in range(0, numCourses):
            pd[n] = []
        for req in prerequisites:
            pd[req[0]].append(req[1])
            
        for n in range(0, numCourses):
            if (n in visited):
                continue
            search_value = self.dfs(n, visited, [], pd)
            if (search_value == True):
                # Cycle found
                return False
            else:
                # No cycle
                pass
        return True
    
    def dfs(self, n, visited, stack, pd):
        if (n in visited): 
            return False
        stack.append(n)
        for m in pd[n]:
            if (m in stack):
                return True
            elif (self.dfs(m, visited, stack, pd)):
                return True
            if (len(stack) > 0): 
                stack.pop()
        visited.add(n)
        return False
