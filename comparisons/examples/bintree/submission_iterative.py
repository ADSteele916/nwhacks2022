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


def in_order_traversal(node: Optional[TreeNode]):
    current = node
    stack = []
    output = []
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif len(stack) > 0:
            current = stack.pop()
            output.append(current.key)
            current = current.right
        else:
            break
    return output
