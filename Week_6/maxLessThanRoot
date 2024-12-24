# Python function maxLessThan(root, K), that accepts the root node of the binary search tree and a number K and returns the maximum number less than or equal to K in the tree.
# If K is the less than every number in the tree return None . Each node in the tree is an object of class Tree , and the tree will have at least one node.

class Tree:
  #constructor
  def __init__(self, initval=None):
    self.value = initval
    if self.value:
      self.left = Tree()
      self.right = Tree()
    else:
      self.left = self.right = None
    return
  
  #Only empty node has value None
  def isempty(self):
    return(self.value == None)
  
  #Leaf nodes have both children empty
  def isleaf(self):
    return(self.value != None and self.left.isempty() and self.right.isempty())
  
#insert element to BST
def insertToBST(root, x):
  # Tree should have atleast one element.
  temp = root
  while (not temp.isempty()):
    if (x < temp.value):
      temp = temp.left
    else:
      temp = temp.right

  temp.value = x
  temp.left = Tree()
  temp.right = Tree()
def maxLessThan(root,K):
    max_val = None
    current = root
    while (not current.isempty()):
        if current.value<K:
            max_val = current.value
            current=current.right
        else:
            current = current.left
    return max_val
    
L = [int(item) for item in input().split(" ")]
x = int(input())
root = Tree(L[0])
for item in L[1:]:
  insertToBST(root, item)

print(maxLessThan(root, x))
