from random import randint

class LinkedList():
    """Helper function to create a linked list in Python"""
    def __init__(self):
        self.head = None

    def insert(self, item):
        node = Node(item)
        node.set_next(self.head)
        self.head = node

    def size(self):
        node = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count

    def __len__(self):
        return self.size()

    def search(self, item):
        node = self.head
        found = False
        while node is not None and not found:
            if node.value == item:
                found = True
            else:
                node = node.next
        return found

    def __contains__(self, item):
        return self.search(item)

    def remove(self, item):
        node = self.head
        found = False
        previous = None
        while not found:
            if node.value == item:
                found = True
            else:
                node = node.next
        if previous is None:
            self.head = node.next
        else:
            previous.set_next(node.next)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.value
            node = node.next

    def __str__(self):
        node = self.head
        result = ""
        while node is not None:
            item = node.value
            node = node.next
            if node is None:
                linked = None
            else:
                linked = node.value
            result += str(item) + " -> " + str(linked) + "\n"
        return result


        
class Node():
    """Node object in LinkedList"""
    def __init__(self, item):
        self.value = item
        self.next = None

    def set_item(self, item):
        self.value = item

    def set_next(self, next):
        self.next = next

    def __str__(self):
        return str((self.value, self.next))

def random_list():
	ll = LinkedList()
	for i in range(15):
		ll.insert(i)
		ll.insert(randint(0, 20))
	return ll