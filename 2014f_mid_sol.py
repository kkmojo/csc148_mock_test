2014 Fall Midter 2014 by looplearning
Answer by 。 


Q1
a)Stack: First-In-Last-Out(FILO), Queue: Last-In-First-Out(LILO)
b)It is because that the effiency to insert at the end is O(1), but effiency to insert at the beginning is O(n)
c)it depends. If we have a attributes to indicate the last node of the linked list then the effiency will be the same. 
	but if we don't have that attributes. then, insert at the first is fast then insert at the end, because we need to
	use loops to iterate to the end of the linked list


d)
	a)
	>>> a.show()
	'Hi'
	b)
	>>> b.show()
	'I'm a B'
	c)
	>>> a.noshow()
	Error class A does not have method noshow()
	d)
	>>> b.noshow()
	'shhh'

Q2
def combine(stack1, stack2):
	"""(Stack, Stack) -> Stack

	Return a new stack containing the elements of stack1, and then the elements of stack2 above them
	"""
	merged = Stack()
	temp1 = Stack()
	temp2 = Stakc()
	while not stack1.is_empty():
		temp1.push(stack1.pop())
	while not stack2.is_empty():
		temp2.push(stack2.pop())
	while not temp1.is_empty():
		item = temp1.pop()
		merged.push(item)
		stack1.push(item)
	while not temp2.is_empty():
		item = temp2.pop()
		merged.push(item)
		stack2.push(item)
	return merged

Q3
a)the linked list will break on the second node

b)
def insert_second(self, item):
	if self.first is None:
		raise Exception
	else:
		newNode = Node(item)
		newNode.next = self.first.next
		self.first.next = newNode


Q4
def filter_positive(lst):
	pos_lst = LinkedList([])
	curr = lst.first

	while curr:
		if curr.item > 0:
			if not pos_lst.first:
				pos_lst.first = Node(curr.item)
			else:
				last = pos_lst.first
				while last.next:
					last = last.next
				last.next = Node(curr.item)
		curr = curr.next
	return pos_lst


Q5(Bonus)
class DoubleNode:
	"""
	=== Attributes ===
	@type item: obj
	@type next: DoubleNode
	@type prev: DoubleNode
	"""
	def __init__(self, item):
		self.item = item
		self.next = None
		self.prev = None

class DoubleLinkedList:
	"""
	=== Attributes ===
	@type first: DoubleNode
	"""
	def __init__(self, lst):
		if len(items) == 0:  # No items, and an empty list!
            self._first = None
        else:
            self._first = DoubleNode(items[0])
            current_node = self._first
            for item in items[1:]:
            	newNode = DoubleNode(item)
                current_node.next = newNode
                newNode.prev = current_node
                current_node = current_node.next


