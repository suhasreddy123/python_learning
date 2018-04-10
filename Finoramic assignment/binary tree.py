# Python program to find if there is a root to sum path

class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


""" 
Given a tree and a sum, return true if there is a path from the root
down to a leaf, such that adding up all the values along the path
equals the given sum.

Strategy: subtract the node value from the sum when recurring down,
and check to see if the sum is 0 when you run out of tree.
"""


# s is the sum
def hasPathSum(node, s):
    # Return true if we run out of tree and s = 0
    if node is None:
        return (s == 0)

    else:
        ans = 0

        # Otherwise check both subtrees
        subSum = s - node.data

        # If we reach a leaf node and sum becomes 0, then
        # return True
        if (subSum == 0 and node.left == None and node.right == None):
            return True

        if node.left is not None:
            ans = ans or hasPathSum(node.left, subSum)
        if node.right is not None:
            ans = ans or hasPathSum(node.right, subSum)

        return ans

    # Driver program to test above functions


s = 22
root = Node(5)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(11)
root.right.left = Node(13)
root.right.right = Node(4)
root.left.left.left = Node(7)
root.left.left.right = Node(2)
root.right.right.left = Node(5)
root.right.right.right = Node(1)




if hasPathSum(root, s):
    print("There is a root-to-leaf path with sum %d" % (s))
else:
    print("There is no root-to-leaf path with sum %d" % (s))

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
