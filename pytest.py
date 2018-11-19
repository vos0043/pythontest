
# coding: utf-8

# In[37]:


# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers 
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

def test_add(x,y):
    if (add(x,y) == x + y):
        return "add passed"
    else:
        return "add failed"

def test_subtract(x,y):   
    if (subtract(x,y) == x - y):
        return "subtract passed"
    else:
        return "subtract failed"
    
def test_multiply(x,y):
    if (multiply(x,y) == x * y):
        return "multiply passed"
    else:
        return "multiply failed"
    
def test_divide(x,y):
    if (divide(x,y) == x * y):
        return "divide passed"

    else:
        return "divide failed"


# In[ ]:


#Changes for the sake of changes

