"""
For a given binary tree, print the height 
"""

""
Visualisation https://youtu.be/aqLTbtWh40E
Thoughts: a binary tre's height is the hieghest dept to the last leaf node so for given any node the hieght under it would be max(hieght(left subtree) + height(right subtree)+ 1

  |
 / \
/\ 
"""


def height(node):
  if node == None:
    return 0
  left_h = height(node.left)
  left_r = height(node.right)
  
  return 1 + max(left_h, left_r)
  



