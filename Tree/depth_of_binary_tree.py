from collections import deque
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    @staticmethod
    def height_recursive(root):
        if root is None:
            return -1
        lheight = Node.height_recursive(root.left)
        rheight = Node.height_recursive(root.right)

        return max(lheight , rheight) +1
    @staticmethod
    def height(root):
        if root is None:
            return 0
        q = deque([root])
        depth = 0
        while q:
            levelsize = len(q)
            for i in range(levelsize):
                curr = q.popleft()

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
            depth +=1

        return depth - 1

    
    @staticmethod
    def level_traversal_rec(root, level, res):
        if root is None:
            return
        if len(res) <= level:
            res.append([])

        res[level].append(root.val)

        Node.level_traversal_rec(root.left, level+1, res)
        Node.level_traversal_rec(root.right, level+1, res)


    @staticmethod
    def level_traversal(root):
        q = []
        res = []

        if q is not None:
            q.append(root)
        current_level = 0
        while q:

            level = len(q)
            res.append([])
            for _ in range(level):
                
                node = q.pop(0)
                res[current_level].append(node.val)

                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)

            current_level +=1
        return res



root = Node(12)
root.left = Node(8)
root.right = Node(18)
root.left.left = Node(5)
root.left.right = Node(11)


# print(root.height_recursive(root))
# print(root.height(root))
# res = []
# root.level_traversal_rec(root, 0, res)
# print(res)
print(root.level_traversal(root))