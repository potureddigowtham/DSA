class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def printll(self):
        if self.head is None:
            print("Linkedlist is empty")
            return
        itr = self.head
        llist = " "
        while itr:
            llist += str(itr.data) + " --> "
            itr = itr.next
        print(llist)

    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    # Create a Linkedlist with a list if data
    def insert_values(self, data_list):
        self.head = None
        for i in data_list:
            self.insert_at_end(i)

    def lengthll(self):
        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count += 1
        return count
    
    def remove_at_begining(self):
        if self.head == None:
            print("Linkedlist is Empty")
            return
        
        self.head = self.head.next

    def remove_at_ending(self):
        if self.head == None:
            print("Linkedlist is Empty")
            return
        
        lllength = self.lengthll()
        itr = self.head
        count = 1
        while itr.next:
            if count == lllength-1:
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next

    def remove_at_index(self, index):
        if self.head == None:
            print("Linkedlist is Empty")
            return

        lllength = self.lengthll()

        if index < 0 or index > lllength:
            raise Exception("Invalid Index") 

        if index == 1:
            self.remove_at_begining()
            return

        if index == lllength:
            self.remove_at_ending()
            return

        itr = self.head
        count = 1
        while itr.next:
            if count == index-1:
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next

    def insert_at_index(self, data, index):
        if self.head == None:
            raise Exception("Linkedlist is empty")

        lllength = self.lengthll()

        if index < 0 or index > lllength+1:
            raise Exception("Invalid Index") 
    
        if index == lllength+1:
            self.insert_at_end(data)
            return

        if index == 1:
            self.insert_at_begining(data)
            return

        itr = self.head
        count = 1
        while itr.next:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count+=1

    def insert_after_value(self, data, value):
        itr = self.head
        while itr:
            if itr.data == value:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next

    def remove_by_value(self, value):
        itr = self.head
        while itr:
            if itr.next.data == value:
                itr.next = itr.next.next
                break
            itr = itr.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values([1,4,5,6,7])
    ll.printll()
    ll.insert_after_value(10, 1)
    ll.printll()
    ll.remove_by_value(4)

    # ll.remove_at_begining()
    # ll.printll()
    # ll.remove_at_ending()
    # ll.printll()
    # ll.remove_at_index(100)
    # ll.printll()
    # ll.insert_at_index(8, 2)
    # ll.printll()
    # print(ll.lengthll())
    # ll.insert_at_index(10, 7)
    # ll.printll()
