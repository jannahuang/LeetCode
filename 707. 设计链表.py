# 707. 设计链表
# 20190402

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(-1)

    def size(self):
        head = self.head
        length = 0
        while head is not None:
            length += 1
            head = head.next
        return length

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        head = self.head
        l = self.size()
        if (index < 0) or (index > l-1): return -1
        i = 0
        while i <= index:
            if i == index:
                return head.value
            i += 1
            head = head.next
        return -1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        head = self.head
        new_node = Node(val)
        new_node.next = head
        self.head = new_node

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        head = self.head
        new_node = Node(val)
        new_node.next = None
        while head is not None:
            prev = head
            head = head.next
        prev.next = new_node

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        head = self.head
        l = self.size()
        i = 0
        while head is not None and i <= index:
            if i == index:
                new_node = Node(val)
                if index == 0:
                    new_node.next = head
                    self.head = new_node
                else:
                    new_node.next = head
                    prev.next = new_node
                return None
            prev = head
            head = head.next
            i += 1

        if head is None and i == index:
            new_node = Node(val)
            prev.next = new_node

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        head = self.head
        i = 0
        while head is not None and i <= index:
            if i == index:
                if index == 0:
                    head = head.next
                    self.head = head
                else:
                    prev.next = head.next
                return None
            prev = head
            head = head.next
            i += 1
