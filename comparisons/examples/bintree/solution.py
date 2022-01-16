"""
Your task is to create a function called check_tree that operates on a binary tree node and produces an in-order
traversal of the tree
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, key: int, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.key = key
        self.left = left
        self.right = right


def in_order_traversal(node: Optional[TreeNode]) -> List[int]:
    """Returns a list containing an in-order traversal of the given binary tree.

    Args:
        node: The root node of a binary tree.

    Returns:
        A list of the tree's nodes in order.
    """
    if node is None:
        return []
    return [*in_order_traversal(node.left), node.key, *in_order_traversal(node.right)]
