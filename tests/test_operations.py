from src.math_opearions import add,sub

## Add Test Case
def test_add():
  assert add(2,3)==5
  assert add(-1,1)==0
  assert add(6,4)==10

## Substract Test Case

def test_sub():
  assert sub(3,4)==-1
  assert sub(5,3)==2
  assert sub(2,2)==0
  
  
