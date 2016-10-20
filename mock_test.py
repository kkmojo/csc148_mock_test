def size(S):
	"""Return the size of the stack, stack should remain same
	after the operation 

	>>> S = Stack()
	>>> S.push(1)
	>>> S.push(2)
	>>> S.push(3)
	>>> size(s)
	3
	>>> s.is_empty()
	False
	"""
	temp = Stack()
	count = 0
	while not s.is_empty():
		count += 1
		temp.push(s.pop())

	while not temp.is_empty():
		s.push(temp.pop())
	return count


def Merge_sum_linklist(L1, L2):
	"""Return a new linked list, which the value
	is the sum of the two linked value in the same position.
	"""
	new_list = LinkedList()

	c1 = L1.first
	c2 = L2.first
	while c1 or c2:
		v1 = 0
		v2 = 0

		if c1:
			v1 = c1.value
			c1 = c1.next
		if c2:
			v2 = c2.value
			c2 = c2.next
		new_list.addNode(v1 + v2)
	return new_list


def Marker:
	"""A class represents the marker

	=== Attributes ===
	@type _record = dict[str, dict[str, float]]
	@type marking_shceme: dict[str, float]
	"""

	def __init__(self, scheme):
		"""Initialize the class

		@type self: Marker
		@type scheme: dict[str, float]
		@type: None
		"""
		self._records = {}


	def add_mark(self, name, category, mark):
		"""add the mark to the record

		@type self: Marker
		@type name: str
			the name of the student
		@type category: str
			the category of the mark
		@type mark: float
			the mark
		@rtype: None
		"""
		if name not in self._records:
			self._records[name] = {category: mark}
		else:
			self._records[name][category] = mark

	def loop_up(self, name, category):
		"""loop up the mark

		@type self: Marker
		@type name: str
		@type category: str
		@rtype: float
		"""
		if name in self._records and category in self._records[name]:
			return self._records[name][category]

	def final_exam(self, name):
		"""Return the final mark of the student

		@type self: Marker
		@rtype name: float
		"""
		final = 0
		if name in self._records:
			for breakdown in self.scheme:
				if breakdown in self._records[name]:
					final += self.scheme[breakdown] * self._records[name][breakdown]
		return final