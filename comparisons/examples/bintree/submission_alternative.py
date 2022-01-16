"""
Your task is to create a function called check_tree that operates on a binary tree node and produces an in-order
traversal of the tree
"""

from typing import Optional


class TreeNode:
    def __init__(self, key: int, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.key = key
        self.left = left
        self.right = right


def in_order_traversal(node):
    if node is None:
        return []
    left = in_order_traversal(node.left)
    this = [node.key]
    right = in_order_traversal(node.right)
    return left + this + right
