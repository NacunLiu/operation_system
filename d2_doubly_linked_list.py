class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        val = '%s: %d' % (self.key, self.value)
        return val

    def __repr__(self):
        val = '%s: %d' % (self.key, self.value)
        return val


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, key, value):
        new_node = Node(key, value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.head
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def append(self, key, value):
        new_node = Node(key, value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            # 让当前节点的next属性指向新建的节点
            self.tail.next = new_node
            # 将新建节点置为tail
            self.tail = new_node

    def insert_at_position(self, position, key, value):
        new_node = Node(key, value)
        if position == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            pass

    def print_dll(self):
        current = self.head
        while current:
            print(f'{current.key}: {current.value}', end=' <=>')
            current = current.next
        print('None')

    def print_node_by_position(self, position):
        if self.head is None:
            raise IndexError('Empty double linked list')
        else:
            current = self.head
            for _ in range(position - 1):
                if current.next is None:
                    raise IndexError('searching node is out of bounds')
                else:
                    current = current.next
            print(current.next)

    def delete_at_position(self, position):
        if position == 0:
            current = self.head.next
            current.prev = None
        else:
            current = self.head
            for _ in range(position - 1):
                if current.next is None:
                    raise IndexError('out of bounds')
                else:
                    current = current.next
            del_next = current.next.next
            current.next = current.next.next
            del_next.prev = current


if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.append("soccer", 100)
    dll.append("football", 200)
    dll.append("baseball", 300)
    dll.append("baseball", 400)
    dll.print_dll()
    dll.delete_at_position(2)
    dll.print_dll()
