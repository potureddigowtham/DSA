class binarytree:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        

    def btree_list(self, data):
        root = binarytree(data[0], None, None)
        stack = [[root, 1]]
        data.pop(0)
        for i in data:
            if stack[-1][1] == 3:
                stack.pop()
            if i != None and stack[-1][1] == 1:
                node = binarytree(i, None, None)
                stack[-1][0].left = node
                stack[-1][1] += 1
                stack.append([node, 1])
            elif i != None and stack[-1][1] == 2:
                node = binarytree(i, None, None)
                stack[-1][0].right = node
                stack[-1][1] += 1
                stack.append([node, 1])
            elif i == None and stack[-1][1] == 1 or stack[-1][1] == 2:
                stack[-1][1] += 1
            if stack[-1][1] == 3:
                stack.pop()
        return root

    def display_btree(self, root):
        ans = ""
        ans += str(root.left.data)+" --> " if root.left != None else " . -->"
        ans += str(root.data)
        ans += " <-- " + str(root.right.data) if root.right != None else "<-- . "
        print(ans)

        if root.left: self.display_btree(root.left)
        if root.right: self.display_btree(root.right)

    def size_btree(self, root):
        if root == None:
            return 0
        size = 1
        size += self.size_btree(root.left)
        size += self.size_btree(root.right)
        return size

    def sum_btree(self, root):
        if root == None:
            return 0
        total = root.data
        total += self.sum_btree(root.left)
        total += self.sum_btree(root.right)
        return total

    def height_btree(self, root):
        if root == None:
            return -1
        lt = self.height_btree(root.left)
        rt = self.height_btree(root.right)
        height = max(lt, rt)+1
        return height


    def min_btree(self, root):
        mini = root.data
        if root.left:
            mini = min(mini, self.min_btree(root.left))
        if root.right:
            mini = min(mini, self.min_btree(root.right))
        return mini

    def max_btree(self, root):
        maxi = root.data
        if root.left:
            maxi = max(maxi, self.max_btree(root.left))
        if root.right:
            maxi = max(maxi, self.max_btree(root.right))
        return maxi
    
    def preorder_btree(self, root):
        if root == None:
            return
        
        print(root.data)
        self.preorder_btree(root.left)
        self.preorder_btree(root.right)

    def postorder_btree(self, root):
        if root == None:
            return
        
        self.postorder_btree(root.left)
        self.postorder_btree(root.right)
        print(root.data)

    def inorder_btree(self, root):
        if root == None:
            return

        self.inorder_btree(root.left)
        print(root.data)
        self.inorder_btree(root.right)
        

obj = binarytree()
tree = obj.btree_list([50,25,12,None,None,37,30,None,None,None,75,62,None,70,None,None,87,None])
# obj.display_btree(tree) 
# print(obj.size_btree(tree))
# print(obj.sum_btree(tree))
# print(obj.height_btree(tree))
# print(obj.min_btree(tree))
# print(obj.max_btree(tree))
# obj.preorder_btree(tree)
# obj.postorder_btree(tree)
obj.inorder_btree(tree)