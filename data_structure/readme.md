# 每周算法练习
很多时候不知道有啥用，所以不重视，但是不熟很吃亏啊。并且光看还不够，必须亲自动手，再简单的算法都很可能会出现问题，除此之外，还需要反复练习，否则容易遗忘

## 算法的作用其实很强大
- 帮助熟悉各种语言的用法及细节，快速练习，提高自己编码能力和速度
- 在参考如力扣上别人的解法时候，往往有新的发现能提高自己的代码性能
- 微观结构和宏观结构很多时候具有很强的相似性，单机运行和多机运行，很多时候原理相似，基础算法更容易让人理解和设计如分布式系统（比如区块链）或者没有现成库解决的问题
- 算法是基本功，本身其实在程序底层有非常多的实现和应用，比如数据库，了解其原理，更能方便理解底层应用的作用机制，以及找到优化方法
- 算法和数据结构，能够更清晰的了解程序的内在运行逻辑，即使是高度封装的python代码，了解其时间和空间复杂度，潜意识里能写出相对更高性能的代码
- 算法题往往已经成为面试中初步检验写代码能力的通用方式，因为有的题目特别是基础算法就几个关键字，方便描述，不需要解释一堆场景
- 解决实际问题时，有些问题通常就是基本算法的内容，如果提前有了解，就能更快的想到最佳的解决方案，有时候绞尽脑汁想出来的方式，实际上前人遇到过，而自己不懂借鉴，卡半天搞出来还感觉很得意，或者根本找不到解法
- 大厂面试基本上都会在多轮面试中考算法题，这个是更直接的经济效益，且入职后也非常重视算法题，也许还有一些其他的原因
- 不止在计算机科学方面，数学在生活中都会有很多应用，比如一些科学的工作方法或者决策方法等

## Finished
- 选择排序
- 快速排序
- 二分查找
- 括号合法性（栈）
- 数组去重
- 链表反转
- 深度优先搜索
- 广度优先搜索
- 动态规划（fib爬楼梯）
- 二叉树遍历（前中后递归）


## TODO
- 有序数组变平衡二叉树（log(n)）
- LRU（146）
- 冒泡排序
- 二叉树共同祖先
- 3数之和
- 快慢指针

- 位运算
- 堆排序
- 归并排序
- 红黑树

- 图
- ...


## 解题思路笔记

### 递归
eg. fib 三角路径和
```python

def recursion(level, param1, param2, *args, **kwargs):
    # 终止条件
    if level>param1:
        return 1
    # 处理当前节点
    process()
    # 分解下探
    ret1 = recursion(level+1, param1, *args, **kwargs)
    ret2 = recursion(level+1, param2, *args, **kwargs)
    # 组合处理
    return ret1 + ret2 
```
### 二分法
eg. power(x,n)

```python

def binary_search(items, n):
    high = len(items) - 1
    low = 0
    mid = low + (high -low) / 2
    while low<=high:
        if items[mid] == n:
            return mid
        elif items[mid] >= n:
            low = mid +1
        else:
            high = mid -1
    return -1

```


### BFS广度优先搜索（图和树）

```python
visited = set()
def bfs(root):
    queue = root
    visited.add(root)
    while queue:
        node = queue.pop()
        process_node(node)
        visited.add(queue)
        nodes = get_not_visited_children(node)
        queue.push(nodes)
```
### DFS深度优先搜索（图和树）
递归，复杂度O(n)
```python
visited = set()
def dfs(node, visited):
    if not node:
        return 
    process_node(node)
    visited.add(node)
    for child in node.children():
        if child not in visited:
            dfs(child, visited)
```
### 二叉搜索树前中后序遍历(递归)
```python
array = []
def dfs(node, array):
    if not node:
        return
    # array.append(node.val)  # 前序遍历 
    dfs(node.left, array)
    # array.append(node.val)  # 中序遍历 左根右
    dfs(node.right, array)
    # array.append(node.val)  # 后续遍历 左右根
    return array
```


### Dynamic Programing
- 递归，记忆化   
- 状态定义（问题转化）  dp[i,j]   
- 状态转移方程  dp[i] = best_of(dp[i-1], dp[i-2] ...)   
- 最优子结构  减少重复计算   

```python
import numpy as np
def dynamic(row,col):
    # row,col = 10, 10
    dp = np.zeros((row,col))
    dp[0,0] = 0
    dp[0,1] = 1
    
    for r in range(1,row):
        for c in range(1, col):
            dp[r,c]  = max(dp[r-1,c], dp[r,c-1])
    return dp[row-1,col-1]  # 反向dp或者正向dp
```


### 位运算
odd（奇数） x & 1 == 1 
even（偶数） x & 1 == 0
清除最低位的1(???) x = x & (x-1)
 
