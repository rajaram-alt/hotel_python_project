import unittest
import hotel_project
   
class SimpleTest(unittest.TestCase):
   def testadd1(self):
      self.assertEqual(hotel_project.top_three_menu('log.txt'),['chappathi','parotta','pasta'])
      self.assertEqual(hotel_project.top_three_menu('error_log.txt'),'eater_id and foodmenu_id matches once more ..!')
      
if __name__ == '__main__':
   unittest.main()