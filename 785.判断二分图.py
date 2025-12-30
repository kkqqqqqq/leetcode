#
# @lc app=leetcode.cn id=785 lang=python3
# @lcpr version=30305
#
# [785] 判断二分图
#

# @lc code=start
class Solution:
    
        
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        self.visited = [False]*n
        self.color = [False]*n
        # 因为图不一定是联通的，可能存在多个子图
        # 所以要把每个节点都作为起点进行一次遍历
        # 如果发现任何一个子图不是二分图，整幅图都不算二分图
        for v in range(n):
            if not self.visited[v]:
                self.traverse(graph, v)
        return self.ok
        
 
        
    def traverse(self,graph:List[bool],v:int):
        if not self.ok :
            return 
        self.visited[v] = True
        for w in graph[v]:
            if not self.visited[w]:
                # 相邻节点 w 没有被访问过
                # 那么应该给节点 w 涂上和节点 v 不同的颜色
                self.color[w] = not self.color[v]
                # 继续遍历 w
                self.traverse(graph, w)
            else:
                # 相邻节点 w 已经被访问过
                # 根据 v 和 w 的颜色判断是否是二分图
                if self.color[w] == self.color[v]:
                    # 若相同，则此图不是二分图
                    self.ok = False
                
        
        
    
    def __init__(self):
        self.visited=[]
        self.color=[]
        self.ok=True 
        
    
        
            
        
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[0,2],[0,1,3],[0,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,3],[0,2],[1,3],[0,2]]\n
# @lcpr case=end

#

