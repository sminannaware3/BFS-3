# Time O(n ^ n)
# Space O(n ^ n)
from collections import deque
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        n = len(s)
        dq = deque()
        dq.append(s)
        visited = set()
        result = set()
        if self.isValid(s): result.add(s)
        while len(dq) > 0 and len(result) == 0:
            length = len(dq)
            for i in range(length):
                curr = dq.popleft()
                for j in range(len(curr)):
                    if curr[j] not in ['(', ')']: continue
                    newS = curr[:j] + curr[j+1:]
                    if newS in visited: continue
                    if self.isValid(newS):
                        result.add(newS)
                    else: dq.append(newS)
                    visited.add(newS)
        return list(result)
    
    def isValid(self, s: str) -> bool:
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                if count == 0: return False
                count -= 1
        return True if count == 0 else False
    
# using DFS finding levels similar to BFS
# Time O(n ^ n)
# Space O(n ^ n)
class Solution:
    def __init__(self):
        self.result = set()
        self.visited = set()
        self.level = 0
        self.resultLevel = -1

    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.dfs(s)
        return list(self.result)
    
    def isValid(self, s: str) -> bool:
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                if count == 0: return False
                count -= 1
        return True if count == 0 else False
    
    def dfs(self, curr: str):
        # base
        if curr in self.visited: return
        if self.isValid(curr):
            if (self.result and self.resultLevel > self.level) or self.resultLevel == -1:
                self.resultLevel = self.level
                self.result = set()
                self.result.add(curr)
            elif self.resultLevel == self.level:
                self.result.add(curr)
            else: return
        
        # logic
        self.level += 1
        for j in range(len(curr)):
            if curr[j] not in ['(', ')']: continue
            newS = curr[:j] + curr[j+1:]
            self.dfs(newS)
        self.level -= 1    
        self.visited.add(curr)

# OPtimized DFS
# Time O(n ^ n)
# Space O(n ^ n)
class Solution:
    def __init__(self):
        self.result = set()
        self.visited = set()
        self.max = 0

    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.dfs(s)
        return list(self.result)
    
    def isValid(self, s: str) -> bool:
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                if count == 0: return False
                count -= 1
        return True if count == 0 else False
    
    def dfs(self, curr: str):
        # base
        if len(curr) < self.max: return
        if self.isValid(curr):
            if len(curr) > self.max:
                self.max = len(curr)
                self.result = set()
            self.result.add(curr)
        
        # logic
        for j in range(len(curr)):
            if curr[j] not in ['(', ')']: continue
            newS = curr[:j] + curr[j+1:]
            if newS not in self.visited:
                self.visited.add(newS)
                self.dfs(newS)
        