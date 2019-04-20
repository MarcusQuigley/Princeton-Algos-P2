import unittest
from weeks import week1

class TestWeek1(unittest.TestCase):
  def test_powerOf(self):
    expected = 120
    actual = week1.powerOf(5)
    self.assertEqual(expected, actual)

  def test_transposition(self):
    matrix = [[1, 2, 3], [4, 5, 6], [7,8,9]]
    expected = [[1, 4, 7], [2, 5, 8], [3,6,9]]
    actual = week1.transposition(matrix,3,3)
    self.assertEqual(expected, actual)


  def test_histogram(self):
    matrix = [1,3,3,4,5,4,4,3,2,4,5,6,7,8,1]
    expected = [0,2,1,3,4,2,1,1,1]
    actual = week1.histogram(matrix,9)
    self.assertEqual(expected, actual)

  def test_course_schedule_fail(self):
    actual = week1.course_schedule(2,[[0,1],[1,0]])
    self.assertFalse(actual)

  def test_course_schedule_pass(self):
    actual = week1.course_schedule(4,[[1,0],[2,0],[3,2]])
    self.assertTrue(actual)
  
  def test_topological_sort_pass(self):
    actual = week1.topological_sort(5,[[0,1],[0,2],[0,3], [4,0], [4,3]])
    print(*actual)
    self.assertIsNotNone(actual)
  
  def test_topological_sort_pass2(self):
    actual = week1.topological_sort(7,[[0,1],[0,2],[0,5], [1,4], [5,2], [6,0], [6,4], [3,6], [3,4], [3,2], [3,5]])
    print(*actual)
    self.assertIsNotNone(actual)
  


