import unittest
def add(a,b):
  return a+b
def subtract(a,b):
  return a-b
def multiply(a,b):
  return a*b

class TestCalculator(unittest.TestCase):

  def test_add(self):
    selfassertEqual(add(20,20),40)
  def test_subtract(self):
    selfassertEqual(subtract(20,10),10)
  def test_multiply(self):
    selfassertEqual(multiply(20,20),40)

if __name__ =="__main__":
  print("student calsi")
  print("addition : ",add(20,20))
  print("subtraction : ",subtract(20,10))
  print("multiplication : ",multiply(5,4))
  print("\n  Excuting automated Tests ...\n")
  unittest.main(argv=['first-arg-is-ignored'],exit=False)
  
  
