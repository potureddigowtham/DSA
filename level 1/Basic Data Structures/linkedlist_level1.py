class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_list(self, data):
        node = Node(data[0])
        self.head = node
        current = node
        for i in range(1, len(data)):
            node = Node(data[i])
            current.next = node
            current = node
        return self.head

    def print_ll(self):
        current = self.head
        print(current.data)
        while current.next != None:
            current = current.next
            print(current.data)

    def add_last(self, data):
        current = self.head
        if current == None:
            self.add_first(data)
            return
        while current.next != None:
            current = current.next
        node = Node(data)
        current.next = node
        self.tail = node

    def add_first(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def add_index(self, data, index):
        node = Node(data)
        current = self.head
        position = 1
        while position < index and current.next != None:
            current = current.next
            position += 1
        if index <= position:
            node.next = current.next
            current.next = node
        else:
            print("list out of index")

    def remove_last(self):
        current = self.head
        prev = None
        while current.next != None:
            prev = current
            current = current.next
        prev.next = None

    def remove_last_single_pointer(self):
        current = self.head
        if current.next == None:
            self.head = None
        while current.next.next != None:
            current = current.next
        current.next = None

    def remove_first(self):
        current = self.head
        self.head = current.next
        current.next = None

    def remove_first_without_self(ll):
        current = ll.head
        ll.head = current.next
        current.next = None

    def remove_index(self, index):
        current = self.head
        position = 1
        while position+1 < index:
            position += 1
            current = current.next
        current.next = current.next.next

    def remove_by_value(ll, val):
        curr = ll.head
        curr1 = curr.next
        while curr1 != 0:
            if val == curr.data:
                curr.next = curr1.next
                curr1.next = None
                return curr
            else:
                curr = curr1
                curr1 = curr1.next
        return ll

    def data_at_index(self, idx):
        counter = 0
        curr = self.head
        while curr.next != 0:
            counter += 1
            if idx == counter:
                print(curr.data)
                return curr.data
            curr = curr.next
        
    def node_at_index(self, idx):
        counter = 0
        curr = self.head
        while curr.next != 0:
            counter += 1
            if idx == counter:
                return curr
            curr = curr.next

    def size_of_ll(self):
        current = self.head
        counter = 1
        while current.next != None:
            counter += 1
            current = current.next
        return counter

    def size_of_ll_without_self(ll):
        current = ll.head
        counter = 1
        while current.next != None:
            counter += 1
            current = current.next
        return counter

    def reverse_data_iteratively_1(self):
        current = self.head
        store = []
        while current.next != None:
            store.append(current.data)
            current = current.next
        store.append(current.data)
        store = store[::-1]

        current = self.head
        for i in store:
            current.data = i
            current = current.next

    def reverse_data_iteratively_2(self):
        l = 1
        h = self.size_of_ll()
        while l < h:
            ldata = self.node_at_index(l)
            hdata = self.node_at_index(h)
            ldata.data, hdata.data = hdata.data, ldata.data
            l += 1
            h -= 1

    def reverse_linkedlist(self):
        prev = None
        curr = self.head
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev 

    def kth_node_from_end(self, k):
        curr = self.head
        data = []
        while curr != None:
            data.append(curr.data)
            curr = curr.next
        print(data[-k])
        return data[-k]

# Kth Node from End of Linked List
    def kth_node_from_end_optimized(self, k):
        slow = self.head
        fast = self.head
        for i in range(k):
            fast = fast.next
        while fast != None:
            slow = slow.next
            fast = fast.next
        print(slow.data)

# Mid Of Linked List
    def mid_of_linked_list(self):
        slow = self.head
        fast = self.head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        print(slow.data)

# Merge Two Sorted Linked Lists
    def mergeTwoSortedLists(l1, l2):
        obj3 = LinkedList()
        curr1 = l1
        curr2 = l2
        while curr1 != None and curr2 != None:
            if curr1.data > curr2.data:
                obj3.add_last(curr2.data)
                curr2 = curr2.next
            else:
                obj3.add_last(curr1.data)
                curr1 = curr1.next
        while curr1 != None:
            obj3.add_last(curr1.data)
            curr1 = curr1.next
        while curr2 != None:
            obj3.add_last(curr2.data)
            curr2 = curr2.next
        # obj3.print_ll()
        return obj3


    def split_ll(first, last, ll):
        obj5 = LinkedList()
        curr = ll.head
        counter = 1
        while counter < first:
            curr = curr.next
            counter += 1
        while counter >= first and counter <= last:
            obj5.add_last(curr.data)
            curr = curr.next
            counter += 1
        return obj5

# Merge Sort A Linked List
    def merge_sort_ll(ll):
        curr = ll
        l = 1
        h = LinkedList.size_of_ll_without_self(curr)
        m = (h)//2
        left_ll = LinkedList.split_ll(l, m, curr)
        right_ll = LinkedList.split_ll(m+1, h, curr)
        sorted_left_ll = LinkedList.merge_sort_ll(left_ll)
        sorted_right_ll = LinkedList.merge_sort_ll(right_ll)
        return LinkedList.mergeTwoSortedLists(sorted_left_ll.head, sorted_right_ll.head)

# Remove Duplicates In A Sorted Linked List
    def remove_duplicates(ll):
        cur = ll.head
        while cur:
            while cur.next and cur.next.data == cur.data:
                cur.next = cur.next.next     # skip duplicated node
            cur = cur.next     # not duplicate of current node, move to next node
        return ll

    def evenodd_ll(self, head):
        odds = LinkedList()
        evens = LinkedList()
        oddshead = odds
        evenhead = evens
        curr = head
        isOdd = True
        while curr:
            if isOdd:
                odds.next = curr
                odds = odds.next
            else:
                evens.next = curr
                evens = evens.next
            isOdd = not isOdd
            curr = curr.next
        evens.next = None
        odds.next = evenhead.next
        odds.print_ll()
        print('done')

    def reverse_ll(self):
        c = self.head
        p = None
        while c:
            temp = c.next
            c.next = p
            p = c
            c = temp
        self.head = p


# Display Reverse (recursive) - Linked List
    def print_reverse_ll(ll):
        if ll.next:
            curr = ll
            LinkedList.print_reverse_ll(curr.next)
            print(curr.data)
        else:
            print(ll.data)

# Reverse Linked List Recursive
    def reverse_ll_recursive(node):
        if (node == None):
            return node
          
        if (node.next == None):
            return node
            
        node1 = LinkedList.reverse_ll_recursive(node.next)
        node.next.next = node
        node.next = None
        return node1


# obj = LinkedList()
# obj1 = LinkedList()
# l1 = obj.add_list([7, 12, 56, 78, 100])
# l2 = obj1.add_list([1, 8, 9, 24, 58, 91, 99])
# # obj.add_last(4)
# # obj.add_first(0)
# # obj.add_index(5, 5)
# # obj.remove_last()
# # obj.remove_last_single_pointer()
# # obj.remove_first()
# # obj.remove_index(2)
# obj.print_ll()
# obj.reverse_data_iteratively()
# obj.data_at_index(3)
# obj.size_of_ll()
# obj.reverse_data_iteratively_2()
# obj.reverse_linkedlist()
# obj.print_ll()
# obj.kth_node_from_end(2)
# obj.kth_node_from_end_optimized(3)
# obj.mid_of_linked_list()
# obj3 = LinkedList.mergeTwoSortedLists(obj.head, obj1.head)
# obj3.print_ll()
# obj4 = LinkedList()
# obj4.add_list([10, 2, 19, 22, 3, 7])
# print(obj4)
# LinkedList.merge_sort_ll(obj4)
# obj4.print_ll()
# obj5 = LinkedList()
# obj5.add_list([2,2,4,2,23,3,33,4,2,4])
# ll = LinkedList.remove_duplicates(obj5)
# ll.print_ll()
evenodd = LinkedList()
evenodd.add_list([1,2,3,4])
# LinkedList.print_reverse_ll(evenodd.head)
ll = LinkedList.reverse_ll_recursive(evenodd.head)
# evenodd.reverse_ll()
# evenodd.print_ll()
# print(evenodd.evenodd_ll(evenodd.head))






