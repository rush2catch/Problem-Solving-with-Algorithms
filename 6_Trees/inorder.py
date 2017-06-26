from tree_by_node import BinaryTree

def inorder(tree):
	if tree:
		inorder(tree.get_left_child())
		print(tree.get_root_value())
		inorder(tree.get_right_child())