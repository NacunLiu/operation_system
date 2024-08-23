#! _*_ encoding=utf-8 _*_


from operation_system import d2_doubly_linked_list


class FIFOCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.map = {}
        self.list = d2_doubly_linked_list.DoublyLinkedList()

    def get(self, key):
        if key not in self.map:
            return -1
        else:
            node = self.map.get(key)
            return node.value
