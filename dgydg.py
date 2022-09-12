class Node:
    def __init__(self, data, prev=None, next=None):
        self.__data = data
        self.__prev__ = prev
        self.__next__ = next

    def get_data(self):
        return self.__data

    def __str__(self):
        return f"data: {self.get_data()}, prev: {self.__prev__.get_data() if self.__prev__ else None}, next: {self.__next__.get_data() if self.__next__ else None}"


class LinkedList:
    def __init__(self, first=None, last=None):
        self.__length = 0
        self.__first__ = Node(None, None, None)
        self.__last__ = Node(None, None, None)
        if last != None and first == None:
            raise ValueError("invalid value for last")
        if first != None and last == None:
            self.__length = 1
            self.__first__ = Node(first, None, None)
            self.__last__ = self.__first__
        if first != None and last != None:
            self.__length = 2
            self.__first__ = Node(first, None, None)
            self.__last__ = Node(last, None, None)
            self.__first__.__prev__ = None
            self.__first__.__next__ = self.__last__
            self.__last__.__next__ = None
            self.__last__.__prev__ = self.__first__

    def __len__(self):
        return self.__length

    def __str__(self):
        if self.__first__.get_data():
            strin = ''
            cur = self.__first__
            while cur:
                if cur != self.__first__:
                    strin = strin + "; "
                strin = strin + str(cur)
                cur = cur.__next__
            return f"LinkedList[length = {self.__length}, [{strin}]]"
        return f"LinkedList[]"

    def clear(self):
        cur = self.__first__.__next__
        self.__first__ = Node(None)
        while cur:
            cur = cur.__next__
            if cur:
                cur.__prev__ = None
        self.__length = 0
        self.__last__ = self.__first__

    def append(self, element):
        cur = Node(element, self.__last__, None)
        self.__last__.__next__ = cur
        self.__last__ = cur
        if self.__first__.get_data():
            pass
        else:
            self.__first__ = cur
        self.__length += 1

    def pop(self):
        if self.__first__.get_data():
            cur = self.__last__
            self.__last__ = cur.__prev__
            self.__last__.__next__ = None
            element = None
            self.__length -= 1
        else:
            raise IndexError("LinkedList is empty!")

    def popitem(self, element):
        cur = self.__first__
        f = 1
        while cur:
            if cur.get_data() == element:
                if self.__first__ == self.__last__:
                    self.__first__ = Node(None)
                    self.__last__ = self.__first__
                else:
                    if self.__last__.get_data() == element:
                        self.__last__ = self.__last__.__prev__
                        self.__last__.__next__ = None
                    else:
                        if self.__first__.get_data() == element:
                            self.__first__ = self.__first__.__next__
                            self.__first__.__prev__ = None
                        else:
                            cur.__prev__.__next__ = cur.__next__
                            cur.__next__.__prev__ = cur.__prev__
                cur = None
                f = None
                self.__length -= 1
            else:
                cur = cur.__next__
        if f:
            raise KeyError(f"{element} doesn't exist!")


linked_list = LinkedList(10)
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

# print(linked_list)  # LinkedList[]
# print(len(linked_list))  # 0

# print(linked_list)  # LinkedList[length = 1, [data: 10, prev: None, next: None]]
# print(len(linked_list))  # 1
# linked_list.append(20)
# print(linked_list)  # LinkedList[length = 2, [data: 10, prev: None, next: 20; data: 20, prev: 10, next: None]]
# print(len(linked_list))  # 2
#
# linked_list.pop()
# print(linked_list)  # LinkedList[length = 1, [data: 10, prev: None, next: None]]
# print(len(linked_list))  # 1
linked_list.popitem("20")
print(linked_list)
