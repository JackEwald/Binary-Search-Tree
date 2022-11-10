import unittest
from Binary_Search_Tree import Binary_Search_Tree

class BST_Tester(unittest.TestCase):
    
    def setUp(self):
      self.__BST_test = Binary_Search_Tree()
    
    #tree with one node tests
    def test_in_order_with_one_insert_with_in_order(self):
      self.__BST_test.insert_element(10)
      self.assertEqual('[ 10 ]', str(self.__BST_test))
    
    def test_one_node_tree_height(self):
      self.__BST_test.insert_element(10)
      returned = self.__BST_test.get_height()
      self.assertEqual(1, returned)
      
    def test_one_node_tree_removal(self):
      self.__BST_test.insert_element(10)
      self.__BST_test.remove_element(10)
      self.assertEqual('[ ]', str(self.__BST_test))
    
    def test_remove_on_empty_tree_raises_error(self):
      try:
        self.__BST_test.remove_element(10)
      except:
        ValueError
      else:
        self.fail('ValueError not raised.')
     
    def test_empty_tree_height(self):
      returned = self.__BST_test.get_height()
      self.assertEqual(0, returned)
    
    #tree with two nodes tests
    def test_in_order_with_two_node_tree(self):
      self.__BST_test.insert_element(10)
      self.__BST_test.insert_element(15)
      self.assertEqual('[ 10, 15 ]', str(self.__BST_test))
    
    def test_two_node_height(self):
      self.__BST_test.insert_element(10)
      self.__BST_test.insert_element(15)
      returned = self.__BST_test.get_height()
      self.assertEqual(2, returned)
      
    def test_two_node_tree_removal(self):
      self.__BST_test.insert_element(10)
      self.__BST_test.insert_element(15)
      self.__BST_test.remove_element(10)
      self.assertEqual('[ 15 ]', str(self.__BST_test))
      
    def test_two_node_tree_height_after_one_removal(self):
      self.__BST_test.insert_element(10)
      self.__BST_test.insert_element(15)
      self.__BST_test.remove_element(10)
      returned = self.__BST_test.get_height()
      self.assertEqual(1, returned)
      
    def test_two_node_tree_pre_order(self):
      self.__BST_test.insert_element(10)
      self.__BST_test.insert_element(15)
      returned = self.__BST_test.pre_order()
      self.assertEqual('[ 10, 15 ]', returned)
      
    def test_two_node_tree_post_order(self):
      self.__BST_test.insert_element(10)
      self.__BST_test.insert_element(15)
      returned = self.__BST_test.post_order()
      self.assertEqual('[ 15, 10 ]', returned)
      
    #tree with multiple nodes tests
    def test_in_order_of_multiple_inserts(self):
      self.__BST_test.insert_element(10)
      self.__BST_test.insert_element(15)
      self.__BST_test.insert_element(5)
      self.__BST_test.insert_element(20)
      self.__BST_test.insert_element(12)
      self.__BST_test.insert_element(7)
      self.assertEqual('[ 5, 7, 10, 12, 15, 20 ]', str(self.__BST_test))
      
    def test_insert_method_raises_error(self):
      self.__BST_test.insert_element(10)
      self.__BST_test.insert_element(15)
      self.__BST_test.insert_element(5)
      self.__BST_test.insert_element(20)
      self.__BST_test.insert_element(12)
      self.__BST_test.insert_element(7)
      try:
        self.__BST_test.insert_element(15)
      except:
        ValueError
      else:
        self.fail('ValueError not raised')
      
    def test_height_of_tree_with_multiple(self):
      self.__BST_test.insert_element(10)
      self.__BST_test.insert_element(15)
      self.__BST_test.insert_element(5)
      self.__BST_test.insert_element(20)
      self.__BST_test.insert_element(12)
      self.__BST_test.insert_element(7)
      returned = self.__BST_test.get_height()
      self.assertEqual(3, returned)
      
    def test_tree_with_multiple_pre_order(self):
      self.__BST_test.insert_element(10)
      self.__BST_test.insert_element(15)
      self.__BST_test.insert_element(5)
      self.__BST_test.insert_element(20)
      self.__BST_test.insert_element(12)
      self.__BST_test.insert_element(7)
      returned = self.__BST_test.pre_order()
      self.assertEqual('[ 10, 5, 7, 15, 12, 20 ]', returned)
      
    def test_tree_with_multiple_post_order(self):
      self.__BST_test.insert_element(10)
      self.__BST_test.insert_element(15)
      self.__BST_test.insert_element(5)
      self.__BST_test.insert_element(20)
      self.__BST_test.insert_element(12)
      self.__BST_test.insert_element(7)
      returned = self.__BST_test.post_order()
      self.assertEqual('[ 7, 5, 12, 20, 15, 10 ]', returned)
      
    def test_remove_method_raises_error(self):
      self.__BST_test.insert_element(10)
      self.__BST_test.insert_element(15)
      self.__BST_test.insert_element(5)
      self.__BST_test.insert_element(20)
      self.__BST_test.insert_element(12)
      self.__BST_test.insert_element(7)
      try:
        self.__BST_test.remove_element(25)
      except:
        ValueError
      else:
        self.fail('ValueError not raised.')
      
    def test_in_order_of_tree_with_multiple_after_removal_of_leaf_node(self):
      self.__BST_test.insert_element(10)
      self.__BST_test.insert_element(15)
      self.__BST_test.insert_element(5)
      self.__BST_test.insert_element(20)
      self.__BST_test.insert_element(12)
      self.__BST_test.insert_element(7)
      self.__BST_test.remove_element(12)
      self.assertEqual('[ 5, 7, 10, 15, 20 ]', str(self.__BST_test))
      
    def test_height_of_tree_with_multiple__after_removal_of_leaf_node(self):
      self.__BST_test.insert_element(10)
      self.__BST_test.insert_element(15)
      self.__BST_test.insert_element(5)
      self.__BST_test.insert_element(20)
      self.__BST_test.insert_element(12)
      self.__BST_test.insert_element(7)
      self.__BST_test.remove_element(12)
      returned = self.__BST_test.get_height()
      self.assertEqual(3, returned)
      
    def test_pre_order_after_removal_of_leaf_node(self):
      self.__BST_test.insert_element(10)
      self.__BST_test.insert_element(15)
      self.__BST_test.insert_element(5)
      self.__BST_test.insert_element(20)
      self.__BST_test.insert_element(12)
      self.__BST_test.insert_element(7)
      self.__BST_test.remove_element(12)
      returned = self.__BST_test.pre_order()
      self.assertEqual('[ 10, 5, 7, 15, 20 ]', returned)
      
    def test_post_order_after_removal_of_leaf_node(self):
      self.__BST_test.insert_element(10)
      self.__BST_test.insert_element(15)
      self.__BST_test.insert_element(5)
      self.__BST_test.insert_element(20)
      self.__BST_test.insert_element(12)
      self.__BST_test.insert_element(7)
      self.__BST_test.remove_element(12)
      returned = self.__BST_test.post_order()
      self.assertEqual('[ 7, 5, 20, 15, 10 ]', returned)
      
    def test_in_order_of_tree_with_multiple_after_removal_of_node_with_one_child(self):
      self.__BST_test.insert_element(10)
      self.__BST_test.insert_element(15)
      self.__BST_test.insert_element(5)
      self.__BST_test.insert_element(20)
      self.__BST_test.insert_element(12)
      self.__BST_test.insert_element(7)
      self.__BST_test.remove_element(5)
      self.assertEqual('[ 7, 10, 12, 15, 20 ]', str(self.__BST_test))
      
    def test_height_when_removal_has_no_effect(self):
      self.__BST_test.insert_element(10)
      self.__BST_test.insert_element(15)
      self.__BST_test.insert_element(5)
      self.__BST_test.insert_element(20)
      self.__BST_test.insert_element(12)
      self.__BST_test.insert_element(7)
      self.__BST_test.remove_element(5)
      returned = self.__BST_test.get_height()
      self.assertEqual(3, returned)
      
    def test_pre_order_after_removal_of_node_with_one_child(self):
      self.__BST_test.insert_element(10)
      self.__BST_test.insert_element(15)
      self.__BST_test.insert_element(5)
      self.__BST_test.insert_element(20)
      self.__BST_test.insert_element(12)
      self.__BST_test.insert_element(7)
      self.__BST_test.remove_element(5)
      returned = self.__BST_test.pre_order()
      self.assertEqual('[ 10, 7, 15, 12, 20 ]', returned)
      
    def test_post_order_after_removal_of_node_with_one_child(self):
      self.__BST_test.insert_element(10)
      self.__BST_test.insert_element(15)
      self.__BST_test.insert_element(5)
      self.__BST_test.insert_element(20)
      self.__BST_test.insert_element(12)
      self.__BST_test.insert_element(7)
      self.__BST_test.remove_element(5)
      returned = self.__BST_test.post_order()
      self.assertEqual('[ 7, 12, 20, 15, 10 ]', returned)
      
    def test_in_order_of_tree_with_multiple_after_removal_of_node_with_two_children(self):
      self.__BST_test.insert_element(10)
      self.__BST_test.insert_element(15)
      self.__BST_test.insert_element(5)
      self.__BST_test.insert_element(20)
      self.__BST_test.insert_element(12)
      self.__BST_test.insert_element(7)
      self.__BST_test.remove_element(15)
      self.assertEqual('[ 5, 7, 10, 12, 20 ]', str(self.__BST_test))
      
    def test_pre_order_after_removal_of_node_woth_two_children(self):
      self.__BST_test.insert_element(10)
      self.__BST_test.insert_element(15)
      self.__BST_test.insert_element(5)
      self.__BST_test.insert_element(20)
      self.__BST_test.insert_element(12)
      self.__BST_test.insert_element(7)
      self.__BST_test.remove_element(15)
      returned = self.__BST_test.pre_order()
      self.assertEqual('[ 10, 5, 7, 20, 12 ]', returned)
      
    def test_post_order_after_removal_of_node_with_two_children(self):
      self.__BST_test.insert_element(10)
      self.__BST_test.insert_element(15)
      self.__BST_test.insert_element(5)
      self.__BST_test.insert_element(20)
      self.__BST_test.insert_element(12)
      self.__BST_test.insert_element(7)
      self.__BST_test.remove_element(15)
      returned = self.__BST_test.post_order()
      self.assertEqual('[ 7, 5, 12, 20, 10 ]', returned)
      
    def test_in_order_of_tree_with_multiple_after_removal_of_root(self):
      self.__BST_test.insert_element(10)
      self.__BST_test.insert_element(15)
      self.__BST_test.insert_element(5)
      self.__BST_test.insert_element(20)
      self.__BST_test.insert_element(12)
      self.__BST_test.insert_element(7)
      self.__BST_test.remove_element(10)
      self.assertEqual('[ 5, 7, 12, 15, 20 ]', str(self.__BST_test))
    
    def test_pre_order_after_removal_of_root(self):
      self.__BST_test.insert_element(10)
      self.__BST_test.insert_element(15)
      self.__BST_test.insert_element(5)
      self.__BST_test.insert_element(20)
      self.__BST_test.insert_element(12)
      self.__BST_test.insert_element(7)
      self.__BST_test.remove_element(10)
      returned = self.__BST_test.pre_order()
      self.assertEqual('[ 12, 5, 7, 15, 20 ]', returned)
      
    def test_post_order_after_removal_of_root(self):
      self.__BST_test.insert_element(10)
      self.__BST_test.insert_element(15)
      self.__BST_test.insert_element(5)
      self.__BST_test.insert_element(20)
      self.__BST_test.insert_element(12)
      self.__BST_test.insert_element(7)
      self.__BST_test.remove_element(10)
      returned = self.__BST_test.post_order()
      self.assertEqual('[ 7, 5, 20, 15, 12 ]', returned)
      
    #special cases tests
    def test_height_when_removal_has_effect(self):
      self.__BST_test.insert_element(10)
      self.__BST_test.insert_element(15)
      self.__BST_test.insert_element(5)
      self.__BST_test.insert_element(20)
      self.__BST_test.insert_element(12)
      self.__BST_test.insert_element(7)
      self.__BST_test.insert_element(13)
      self.__BST_test.remove_element(13)
      returned = self.__BST_test.get_height()
      self.assertEqual(3, returned)
      
    def test_in_order_with_multiple_inserts_and_removes(self):
      self.__BST_test.insert_element(10)
      self.__BST_test.insert_element(15)
      self.__BST_test.insert_element(5)
      self.__BST_test.remove_element(15)
      self.__BST_test.insert_element(20)
      self.__BST_test.insert_element(12)
      self.__BST_test.insert_element(7)
      self.__BST_test.insert_element(15)
      self.__BST_test.remove_element(12)
      self.__BST_test.insert_element(3)
      self.assertEqual('[ 3, 5, 7, 10, 15, 20 ]', str(self.__BST_test))
    
    def test_height_with_multiple_inserts_and_removes(self):
      self.__BST_test.insert_element(10)
      self.__BST_test.insert_element(15)
      self.__BST_test.insert_element(5)
      self.__BST_test.remove_element(15)
      self.__BST_test.insert_element(20)
      self.__BST_test.insert_element(12)
      self.__BST_test.insert_element(7)
      self.__BST_test.insert_element(15)
      self.__BST_test.remove_element(12)
      self.__BST_test.insert_element(3)
      returned = self.__BST_test.get_height()
      self.assertEqual(3, returned)
      
    def test_pre_order_with_multiple_inserts_and_removes(self):
      self.__BST_test.insert_element(10)
      self.__BST_test.insert_element(15)
      self.__BST_test.insert_element(5)
      self.__BST_test.remove_element(15)
      self.__BST_test.insert_element(20)
      self.__BST_test.insert_element(12)
      self.__BST_test.insert_element(7)
      self.__BST_test.insert_element(15)
      self.__BST_test.remove_element(12)
      self.__BST_test.insert_element(3)
      returned = self.__BST_test.pre_order()
      self.assertEqual('[ 10, 5, 3, 7, 20, 15 ]', returned)
      
    def test_post_order_with_multiple_inserts_and_removes(self):
      self.__BST_test.insert_element(10)
      self.__BST_test.insert_element(15)
      self.__BST_test.insert_element(5)
      self.__BST_test.remove_element(15)
      self.__BST_test.insert_element(20)
      self.__BST_test.insert_element(12)
      self.__BST_test.insert_element(7)
      self.__BST_test.insert_element(15)
      self.__BST_test.remove_element(12)
      self.__BST_test.insert_element(3)
      returned = self.__BST_test.post_order()
      self.assertEqual('[ 3, 7, 5, 15, 20, 10 ]', returned)
      
    def test_height_after_removing_several_nodes(self):
      self.__BST_test.insert_element(10)
      self.__BST_test.insert_element(15)
      self.__BST_test.insert_element(5)
      self.__BST_test.remove_element(15)
      self.__BST_test.insert_element(20)
      self.__BST_test.insert_element(12)
      self.__BST_test.insert_element(7)
      self.__BST_test.insert_element(15)
      self.__BST_test.remove_element(12)
      self.__BST_test.insert_element(3)
      self.__BST_test.remove_element(20)
      self.__BST_test.remove_element(7)
      self.__BST_test.remove_element(5)
      returned = self.__BST_test.get_height()
      self.assertEqual(2, returned)
            
if __name__ == '__main__':
  unittest.main()
