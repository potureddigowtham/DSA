from lib2to3.pgen2.pgen import generate_grammar
from sys import displayhook


class GenericTreeNode:
    def __init__(self, data=0):
        self.data = data
        self.children = []

    def tree_list(self, arr):
        root = GenericTreeNode(None)
        stack = []
        for i in range(len(arr)):
            if arr[i] == -1:
                stack.pop()
            else:
                t = GenericTreeNode(arr[i])

                if len(stack) > 0:
                    stack[-1].children.append(t)
                else:
                    root = t

                stack.append(t)
        return root

    def display_tree(self, root):
        val = str(root.data) + " --> "
        for i in root.children:
            val += str(i.data) + " "
        val += "."
        print(val)

        for i in root.children:
            self.display_tree(i)
        return

    def size_tree(self, root):
        count = 0
        for i in root.children:
            val = self.size_tree(i)
            count += val
        count += 1
        return count

    def max_in_tree(self, root):
        maxi = root.data
        for i in root.children:
            maxi = max(maxi, i.data)
        for i in root.children:
            val = self.max_in_tree(i)
            maxi = max(maxi, val)
        return maxi

    def height_of_tree(self, root):
        height = 0
        for i in root.children:
            val = self.height_of_tree(i)
            height = max(height, val)
        height += 1
        return height

    def traversal_tree(self, root):
        print("Node pre " + str(root.data))
        for i in root.children:
            print("Edge pre " + str(root.data) + " " + str(i.data))
            self.traversal_tree(i)
            print("Edge post " + str(root.data) + " " + str(i.data))
        print("Node post " + str(root.data))

    def preorder_tree(self, root):
        print(root.data)
        for i in root.children:
            self.preorder_tree(i)

    def postorder_tree(self, root):
        for i in root.children:
            self.postorder_tree(i)
        print(root.data)

    def levelorder_tree(self, root):
        queue = []
        queue.append(root)
        while len(queue) > 0:
            temp = queue.pop(0)
            print(temp.data, end =" ")
            for i in temp.children:
                queue.append(i)

    def levelorder_linewise_tree(self, root):
        queue1 = []
        queue2 = []
        queue1.append(root)
        while len(queue1) > 0 or len(queue2) > 0 :
            temp = queue1.pop(0)
            print(temp.data, end =" ")
            for i in temp.children:
                queue2.append(i)
            if len(queue1) < 1:
                queue1 = queue2
                queue2 = []
                print(" ")

    def levelorder_linewise_zigzag_tree(self, root):
        stack1 = []
        stack2 = []
        stack1.append(root)
        level = 1
        while len(stack1) > 0 or len(stack2) > 0 :
            temp = stack1.pop()
            print(temp.data, end =" ")
            temp_list = temp.children
            if level % 2 == 0:
                for i in range(len(temp_list)-1,-1,-1):
                    stack2.append(temp_list[i])
                    # print(temp_list[i].data)
            else:
                for i in temp.children:
                    stack2.append(i)
                    # print(i.data)
            if len(stack1) < 1:
                stack1 = stack2
                stack2 = []
                print(" ")
                level += 1

    def levelorder_single_queue_tree_linewise(self, root):
        queue = [] 
        queue.append(root)
        queue.append(None)
        while len(queue) > 0:
            if queue[0] == None:
                queue.pop(0)
                print(" ")
                if len(queue) > 0:
                    queue.append(None)
            else:
                temp = queue.pop(0)
                print(temp.data, end=" ")
                for i in temp.children:
                    queue.append(i)

    def arrange(self, data):
        i = 0
        j = len(data)-1
        while i < j and i != j:
            data[i], data[j] = data[j], data[i]
            i += 1
            j -= 1
        return data

    def mirror_tree(self, root):
        for i in root.children:
            self.mirror_tree(i)
        self.arrange(root.children)

    def remove_leaf_nodes_tree(self, root):
        for i in range(len(root.children) - 1, -1, -1):
            child = root.children[i]
            if len(child.children) == 0:
                del root.children[i]
            
        for child in root.children:
            self.remove_leaf_nodes_tree(child)

# form a linear tree in preorder fashion
    def linearize_tree(self, root, root1):
        if root1.data == 0:
            root1.data = root.data
        else:
            temp = GenericTreeNode()
            temp.data = root.data
            root1.children.append(temp)
        for i in root.children:
            self.linearize_tree(i, root1)
        return root1

# find for an element in generic tree
    def find_in_tree(self, root, k):
        if k == root.data:
            print("True")
            return True
        for i in root.children:
            ans = self.find_in_tree(i, k)
            if ans:
                return True
        return False

# Find not to root path, find a element where it is and return the root nodes of that element.
    def root_to_node_path(self, root, k):
        if k == root.data:
            path = []
            path.append(root.data)
            return path
        for i in root.children:
            path1 = self.root_to_node_path(i, k)
            if len(path1) > 0:
                path1.append(root.data)
                return path1
        return []

# find lowest common ancestor
    def lowest_common_ancestor(self, root, a, b):
        path1 = self.root_to_node_path(root, a)
        path2 = self.root_to_node_path(root, b)
        for i in path1:
            for j in path2:
                if i == j:
                    return i
        return None

# Distance btw 2 nodes
    def diff_btw_2_nodes(self, root, a, b):
        path1 = self.root_to_node_path(root, a)
        path2 = self.root_to_node_path(root, b)
        i = len(path1) - 1
        j = len(path2) - 1
        while (i >= 0 and j >= 0 and path1[i] == path2[j]):
            i -= 1
            j -= 1
        return i+j+2

# Are generic tress similar in shape
    def are_trees_similar_in_shape(root1, root2):
        print(root1.data, root2.data)
        if len(root1.children) != len(root2.children):
            return False
        
        for i in range(len(root1.children)):
            temp1 = root1.children[i]
            temp2 = root2.children[i]
            if not GenericTreeNode.are_trees_similar_in_shape(temp1, temp2):
                return False
        
        return True

# Are generic trees mirror in shape
    def are_trees_mirror_in_shape(a, b):
        if len(a.children) != len(b.children):
            return False

        for i, j in zip(a.children, b.children[::-1]):
            if not GenericTreeNode.are_trees_mirror_in_shape(i, j):
                return False
        return True

    def is_generic_tree_symmetric(a):
        return GenericTreeNode.are_trees_mirror_in_shape(a,a)

    predecessor = 0
    successor = 0
    state = 0
    def predecessor_and_successor(root, k):
        if GenericTreeNode.state == 0:
            if root.data == k:
                GenericTreeNode.state += 1
                return True
            else:
                GenericTreeNode.predecessor = root.data
        elif GenericTreeNode.state == 1:
            GenericTreeNode.successor = root.data
            GenericTreeNode.state += 1
        for i in root.children:
            GenericTreeNode.predecessor_and_successor(i, k)
            

    ciel = 0
    floor = 0
    def ceil_and_floor_in_generic_tree(root, k):
        if root.data > k:
            GenericTreeNode.ciel = root.data if GenericTreeNode.ciel == 0 else min(GenericTreeNode.ciel, root.data)
        if root.data < k:
            GenericTreeNode.floor = root.data if GenericTreeNode.floor == 0 else max(GenericTreeNode.floor, root.data)
        for i in root.children:
            GenericTreeNode.ceil_and_floor_in_generic_tree(i, k)

    def kth_largest_element_in_tree(root, k):
        for i in range(k):
            if i == 0:
                GenericTreeNode.ceil_and_floor_in_generic_tree(root, 1000000)
            else:
                data = GenericTreeNode.floor
                GenericTreeNode.floor = 0
                GenericTreeNode.ceil_and_floor_in_generic_tree(root, data)
            print(GenericTreeNode.floor)

        
if __name__ == "__main__":
    arr = [10,20,50,-1,60,-1,-1,30,70,-1,80,110,-1,
        120,-1,-1,90,-1,-1,40,100,-1,-1,-1]
    # arr = [10,20,50,-1,60,-1,-1,30,70,-1,80,110,-1,\
    #     120,-1,-1,90,-1,-1,40,100,-1,-1,-1]
    # arr = [1,2,-1,3,-1,-1]
    obj = GenericTreeNode()
    tree = obj.tree_list(arr)
    # obj.display_tree(tree)
    # print(obj.size_tree(tree))
    # print(obj.max_in_tree(tree))
    # print(obj.height_of_tree(tree))
    # obj.traversal_tree(tree)
    # obj.preorder_tree(tree)
    # obj.postorder_tree(tree)
    # obj.levelorder_tree(tree)
    # obj.levelorder_linewise_tree(tree)
    # obj.levelorder_linewise_zigzag_tree(tree)
    # obj.levelorder_single_queue_tree_linewise(tree)
    # obj.mirror_tree(tree)
    # obj.remove_leaf_nodes_tree(tree)
    # tree1 = GenericTreeNode()
    # tree1 = obj.linearize_tree(tree, tree1)
    # obj.display_tree(tree1)
    # print(obj.find_in_tree(tree, 50))
    # print(obj.root_to_node_path(tree, 20))
    # print(obj.lowest_common_ancestor(tree, 90, 80))
    # print(obj.diff_btw_2_nodes(tree, 50, 120))
    # arr1 = [10,20,50,-1,-1,30,70,-1,80,110,-1,\
    #     120,-1,-1,90,-1,-1,40,100,-1,-1,-1]
    # obj1 = GenericTreeNode()
    # tree1 = obj1.tree_list(arr1)
    # print(GenericTreeNode.are_trees_similar_in_shape(tree, tree1))
    # a_arr = [1, 2, -1, 3, 4, -1, 5, -1, -1]
    # b_arr = [1, 2, 3, -1, 4, -1, -1, 5, -1]
    # b_arr = [1, 2, -1, 3, 4, -1, 5, -1, -1]
    # a = obj.tree_list(a_arr)
    # b = obj1.tree_list(b_arr)
    # print(GenericTreeNode.are_trees_mirror_in_shape(a, b))
    # a_arr = [1, 2, 4, -1, 5, -1, -1, 3, 6, -1, 7, -1, -1]
    # a_arr = [1, 2, 4, -1, 5, -1, -1, 3, 6, -1, -1]
    # a = obj.tree_list(a_arr)
    # print(GenericTreeNode.is_generic_tree_symmetric(a))
    # GenericTreeNode.predecessor_and_successor(tree, 110)
    # print(GenericTreeNode.predecessor)
    # print(GenericTreeNode.successor)
    # GenericTreeNode.ceil_and_floor_in_generic_tree(tree, 120)
    # print(GenericTreeNode.ciel)
    # print(GenericTreeNode.floor)
    # GenericTreeNode.floor = 1000000000000
    GenericTreeNode.kth_largest_element_in_tree(tree, 3)





