from tree_by_node import BinaryTree

def preorder(tree):
	if tree:
		print(tree.get_root_value())
		preorder(tree.get_left_child())
		preorder(tree.get_right_child())

test_tree_1 = BinaryTree('a')
test_tree_1.insert_left('b')
test_tree_1.insert_right('c')
preorder(test_tree_1)