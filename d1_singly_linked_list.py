class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


#  the basic idea of creating a singly linked list is to start from the head
#  first we initiate the head and is None
#  when creating the linked list we are actually using a pointer(current) to point to each node in serial and assign the address to the node.next
#  for appending node to the linked list first we judge the head is None or not if it's None then we assign the new node to the head
# if the linked list already has a head then we tried to find the end(node.next = None) then we assign the new node to the end
# 其实新添加一个node就是将链表末尾的节点的地址指向新建的node
# 节点的两个属性就是值和地址
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_at_position(self, position, data):
        if position == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            # tricky 的地方在于当我们将节点地址assign给current的时候，current既是一个节点也是一个引用，它里边存储的是节点的地址，但是可以直接使用节点属性
            # current 首先将head节点的地址给它，但是因为它的地址指向的是一个节点对象，所以也能引用这个对象
            # current.next就是引用这个对象的next属性，调用其中的地址
            current = self.head
            for _ in range(position - 1):
                if current.next is None:
                    raise IndexError("position out of bound")
                current = current.next
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node

    def delete_at_position(self, position):
        if self.head is None:
            raise IndexError("position out of bounds")
        if position == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(position - 1):
                if current.next is None:
                    raise IndexError("position out of bounds")
                else:
                    current = current.next
            if current.next is None:
                raise IndexError("position out of bounds")
            else:
                current.next = current.next.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def get_length_of_sll(self):
        if self.head is None:
            return ("singy linked list is empty")
        else:
            current = self.head
            length = 1
            while current.next:
                length += 1
                current = current.next
            return length

    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return current
            else:
                current = current.next
        return None


if __name__ == '__main__':
    sll = SinglyLinkedList()
    sll.append("A")
    sll.append("B")
    sll.append("C")
    sll.append("D")
    sll.append("E")
    sll.append("F")
    sll.append("G")
    sll.append("H")
    sll.print_list()
    print(sll.get_length_of_sll())
    print(sll.search("C"))
