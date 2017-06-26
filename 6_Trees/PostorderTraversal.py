from tree_by_node import BinnaryTree

def postorder(tree):
	if tree:
		postorder(tree.get_left_child())
		postorder(tree.get_right_child())
		print(tree.get_root_value())
