
# Using BFS
# Time O(v+e)
# Space O(v+e)
from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None 
        oldToNewMap = {}
        dq = deque()
        newNode = Node(node.val)
        oldToNewMap[node] = newNode
        dq.append(node)
        while len(dq) > 0:
            curr = dq.popleft()
            for ne in curr.neighbors:
                if ne not in oldToNewMap:
                    newNode = Node(ne.val)
                    oldToNewMap[ne] = newNode
                    dq.append(ne)
                oldToNewMap[curr].neighbors.append(oldToNewMap[ne])
        return oldToNewMap[node]
                
# Using DFS
# Time O(v+e)
# Space O(v+e)
from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None 
        oldToNewMap = {}
        self.dfs(node, oldToNewMap)
        return oldToNewMap[node]
    
    def dfs(self, node: Optional['Node'], oldToNewMap: dict) -> None:
        # Base
        if node in oldToNewMap: return
        #logic
        newNode = Node(node.val)
        oldToNewMap[node] = newNode
        for ne in node.neighbors:
            self.dfs(ne, oldToNewMap)
            oldToNewMap[node].neighbors.append(oldToNewMap[ne])
        