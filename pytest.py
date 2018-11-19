import rekenmachine as rm

def test_add(x,y):
    if (rm.add(x,y) == x + y):
        return "add passed"
    else:
        return "add failed"

def test_subtract(x,y):   
    if (rm.subtract(x,y) == x - y):
        return "subtract passed"
    else:
        return "subtract failed"
    
def test_multiply(x,y):
    if (rm.multiply(x,y) == x * y):
        return "multiply passed"
    else:
        return "multiply failed"
    
def test_divide(x,y):
    if (rm.divide(x,y) == x * y):
        return "divide passed"

    else:
        return "divide failed"