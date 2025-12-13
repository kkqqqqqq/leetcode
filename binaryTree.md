# 二叉树

先在开头总结一下，二叉树解题的思维模式分两类：

1、是否可以通过遍历一遍二叉树得到答案？如果可以，用一个 traverse 函数配合外部变量来实现，这叫「遍历」的思维模式。

2、是否可以定义一个递归函数，通过子问题（子树）的答案推导出原问题的答案？如果可以，写出这个递归函数的定义，并充分利用这个函数的返回值，这叫「分解问题」的思维模式。

无论使用哪种思维模式，你都需要思考：

如果单独抽出一个二叉树节点，它需要做什么事情？需要在什么时候（前/中/后序位置）做？



## 遍历
前中后序是遍历二叉树过程中处理每一个节点的三个特殊时间点

前中后序位置的代码，能力依次增强。

前序位置的代码只能从函数参数中获取父节点传递来的数据。

中序位置的代码不仅可以获取参数数据，还可以获取到左子树通过函数返回值传递回来的数据。

后序位置的代码最强，不仅可以获取参数数据，还可以同时获取到左右子树通过函数返回值传递回来的数据。

所以，某些情况下把代码移到后序位置效率最高；有些事情，只有后序位置的代码能做。

### 代码框架
```python

# 二叉树的遍历框架
def traverse(root):
    if root is None:
        return
    # 前序位置
    traverse(root.left)
    # 中序位置
    traverse(root.right)
    # 后序位置

```

```python
# 层序遍历
# 输入一棵二叉树的根节点，层序遍历这棵二叉树
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return
        q = collections.deque()
        q.append(root)
        depth = 0
        # 从上到下遍历二叉树的每一层
        while q:
            sz = len(q)   ------可以用来求最大宽度
            # 从左到右遍历每一层的每个节点。   
            for i in range(sz):    -----可以用来每一层的max/min
                cur = q.popleft()

                # 将下一层节点放入队列
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            depth += 1   --------可以用来求最大深度
```