def binary_tree(r):
	return [r, [], []]

def insert_left(root, newBranch):
	t = root.pop(1)
	if len(t) > 1:
		root.insert(1, [newBranch, t, []])
	else:
		root.insert(1, [newBranch, [], []])
	return root

def insert_right(root, newBranch):
	t = root.pop(2)
	if len(t) > 1:
		root.insert(2, [newBranch, [], t])
	else:
		root.insert(2, [newBranch, [], []])
	return root

def get_root_value(root):
	return root[0]

def set_root_value(root, newVal):
	root[0] = newVal

def get_left_child(root):
	return root[1]

def get_right_child(root):
	return root[2]

myTree = ['a', ['b', ['d', [], []], ['e', [], []]], ['c', ['f', [], []], []]]
branch_1 = ['g']
branch_2 = ['k']
insert_left(myTree, branch_1)
print(myTree)
insert_right(myTree[1], ['h'])
print(myTree)
insert_right(myTree[2], ['k'])
print(myTree)