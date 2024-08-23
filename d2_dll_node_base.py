class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        val = "%d: %d" % (self.key, self.value)
        return val

    def __repr__(self):
        val = "%d: %d" % (self.key, self.value)
        return val


class DoubleLinkedList:
    def __init__(self, capacity=0xffff):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.size = 0

    # insert a node before head
    def push(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            self.head.next = None
            self.head.prev = None
        else:
            node.next = self.head
            self.head.prev = node
            node.prev = None
            self.head = node
        self.size += 1
        return node

    # insert a node after tail
    def append(self, node):
        if not self.head:
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
        self.size += 1
        return node

    # special use for delete head node
    def __del_head(self):
        if not self.head:
            return
        node = self.head
        if node.next:
            self.head = node.next
            self.head.prev = None
        else:
            self.tail = self.head = None
        self.size -= 1
        return node

    # special use for delete tail node
    def __del_tail(self):
        if not self.tail:
            return
        node = self.tail
        if self.tail.prev:
            self.tail = node.prev
            self.tail.next = None
        else:
            self.tail = self.head = None
        self.size -= 1
        return node

    # delete a node
    def __remove(self, node):
        # for node=None, default to remove the tail node
        if not node:
            node = self.tail
        if node == self.tail:
            self.__del_tail()
        elif node == self.head:
            self.__del_head()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.size -= 1
        return node

    # pop head node
    def pop(self):
        return self.__del_head()

    def remove(self, node=None):
        return self.__remove(node)

    def print(self):
        p = self.head
        line = ''
        while p:
            line += '%s' % p
            p = p.next
            if p:
                line += ' => '
            else:
                line += 'None'
        print(line)


if __name__ == '__main__':
    dll = DoubleLinkedList(10)
    nodes = []
    for i in range(10):
        node = Node(i, i + 1)
        nodes.append(node)
        dll.append(node)
    dll.print()
    dll.push(Node(100, 101))
    dll.print()
    print(dll.pop())
    dll.print()
    dll.remove(Node(1, 2))
    dll.print()
