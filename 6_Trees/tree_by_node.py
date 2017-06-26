class BinaryTree(object):
	def __init__(self, rootObj):
		self.key = rootObj
		self.leftChild = None
		self.rightChild = None

	def insert_left(self, newNode):
		if self.leftChild == None:
			self.leftChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.leftChild = self.leftChild
			self.leftChild = t

	def insert_right(self, newNode):
		if self.rightChild == None:
			self.rightChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.rightChild = self.rightChild
			self.rightChild = t

	def get_right_child(self):
		return self.rightChild

	def get_left_child(self):
		return self.leftChild

	def set_root_value(self, obj):
		self.key = obj

	def get_root_value(self):
		return self.key


r = BinaryTree('a')
print(r)
print(r.get_root_value())
print(r.get_left_child())
r.insert_left('b')
print(r.get_left_child())
print(r.get_left_child().get_root_value())
r.insert_right('c')
print(r.get_right_child())
print(r.get_right_child().get_root_value())
r.get_right_child().set_root_value('hello')
print(r.get_right_child().get_root_value())