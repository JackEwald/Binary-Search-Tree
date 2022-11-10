class Binary_Search_Tree:

  class __BST_Node:

    def __init__(self, value):
      self.value = value
      self.right = None
      self.left = None
      self.height = 0
    
    def __get_node_height(self, node):
      if node is None:
        return -1
      else:
        return node.height
    
    def adjust_height(self):
      if self.left is not None and self.right is not None:
        self.height = 1 + max(self.__get_node_height(self.left), self.__get_node_height(self.right))
      elif self.left is not None:
        self.height = 1 + self.__get_node_height(self.left)
      elif self.right is not None:
        self.height = 1 + self.__get_node_height(self.right)
      else:
        self.height = 1

  def __init__(self):
    self.__root = None

  def __recursive_insert(self, value, root):
    if root is None:    
      root = self.__BST_Node(value)
      self.height = root.adjust_height()
    #raises ValueError if value being inserted is already in the tree
    elif root.value == value:
      raise ValueError
    #the next two elif statements call the function again depending on if the
    #value being inserted is greater or less than the root node
    elif value < root.value:
      root.left = self.__recursive_insert(value, root.left)
    elif value >= root.value:
      root.right = self.__recursive_insert(value, root.right)
    self.height = root.adjust_height()
    return root
    
  def insert_element(self, value):
    self.__root = self.__recursive_insert(value, self.__root)

  def __recursive_remove(self, value, root):
    #raises ValueError if value is not found
    if root is None:
      raise ValueError
    if root.value > value: 
      root.left = self.__recursive_remove(value, root.left)
    elif root.value < value: 
      root.right = self.__recursive_remove(value, root.right)
    else: 
      #the following lines of code run through all possible outcomes 
      #for the remove method depending on how many children a node has
      if root.right is None:
        self.height = root.adjust_height()
        return root.left
      if root.left is None:
        self.height = root.adjust_height()
        return root.right
      temp = root.right
      while temp.left is not None:
        temp = temp.left
      root.value = temp.value
      root.right = self.__recursive_remove(temp.value, root.right)
    self.height = root.adjust_height()
    return root

  def remove_element(self, value):
    self.__root = self.__recursive_remove(value, self.__root) 

  def __recursive_in_order(self, node):
    if node is not None:
      self.__recursive_in_order(node.left)
      self.__string += str(node.value) + ', '
      self.__recursive_in_order(node.right)

  def in_order(self):
    if self.__root is None:
      self.__string = '[ ]'
    else:
      self.__string = '[ '
      self.__recursive_in_order(self.__root)
      self.__string = self.__string[:-2]
      self.__string += ' ]'
    return self.__string   

  def __recursive_pre_order(self, node):
    if node is not None:
      self.__string += str(node.value) + ', '
      self.__recursive_pre_order(node.left)
      self.__recursive_pre_order(node.right)
    
  def pre_order(self):
    if self.__root is None:
      self.__string = '[ ]'
    else:
      self.__string = '[ '
      self.__recursive_pre_order(self.__root)
      self.__string = self.__string[:-2]
      self.__string += ' ]'
    return self.__string

  def __recursive_post_order(self, node):
    if node is not None:
      self.__recursive_post_order(node.left)
      self.__recursive_post_order(node.right)
      self.__string += str(node.value) + ', '

  def post_order(self):
    if self.__root is None:
      self.__string = '[ ]'
    else:
      self.__string = '[ '
      self.__recursive_post_order(self.__root)
      self.__string = self.__string[:-2]
      self.__string += ' ]' 
    return self.__string
  
  def get_height(self):
    if self.__root is not None:
      return self.__root.height
    else:
      return 0

  def __str__(self):
    return self.in_order()

if __name__ == '__main__':
  pass #unit tests make the main section unnecessary.
