from calculator import add, factorial, sin, divide, subtract, multi
import numpy as np
import pytest
import math




#test-funks for add():

def test_add():
    a = 1; b = 2
    assert add(a,b) == 3, f'{a} + {b} gives wrong answer'

def test_add():
    tol = 1e-6
    assert  abs(add(0.1,0.2) - 0.3) < tol, "not working"

def test_add():
    a = "Hello "
    b = "World"
    assert add(a,b) == "Hello World", f'Adding strings with add() is not possible'

def test_add():
    with pytest.raises(TypeError):
        add(5,'test')

@pytest.mark.parametrize("xy, expe", [[(1,2),3],[(1,0),1],[(-1,1),0]])
def test_add(xy, expe):
    assert add(xy[0],xy[1]) == expe

@pytest.mark.parametrize("xy, expe", [[(0.1,0.2),0.3],[(0.0,0.0),0.0],[(0.54,0.46),1]])
def test_add(xy, expe):
    tol = 1e-6
    assert  abs(add(xy[0],xy[1]) - expe) < tol, "not working"

@pytest.mark.parametrize('xy,expe', [[('Hello ','World'),'Hello World'],[('Fiske ','Torsk'),'Fiske Torsk'],[('Norge ','Vakkert'),'Norge Vakkert']])
def test_add(xy, expe):
    assert add(xy[0], xy[1]) == expe, 'Fault when adding strings'




#test-funks for subtract():

def test_subtract():
    a = 1; b = -5
    assert subtract(a,b) == 6, f'{a} - {b} gives wrong answer'

@pytest.mark.parametrize("xy, expe", [[(1,-5),6],[(0.0,0.0),0.0],[(-4,-5),1]])
def test_subtract(xy, expe):
    assert subtract(xy[0],xy[1]) == expe, 'subtract failed'




#test-funks for factorial():

def test_factorial():
    n = 0
    assert factorial(n) == math.factorial(n), f'{factorial(n)} =! {math.factorial(n)}'

@pytest.mark.parametrize('n',[0,3,5,10])
def test_factorial(n):
    assert factorial(n) == math.factorial(n)



#test-funks for sin():

def test_sin():
    tol = 1e-6
    forventer = np.sqrt(2)/2
    b = np.pi/4
    assert abs(sin(b,20) - forventer) < tol, f'{sin(b,20)} =! {forventer}'

@pytest.mark.parametrize('n, expo',[[(np.pi/4,20),np.sqrt(2)/2],[(0,20),0],[(np.pi/2,20),1],[(3*np.pi/2,20),-1]])
def test_sin(n,expo):
    tol = 1e-6
    assert abs(sin(n[0],n[1])-expo) < tol




#test-funks for divide():

def test_divide():
    assert divide(100,10) == 10, 'Error when dividing'

def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        divide(4,0)

@pytest.mark.parametrize('n, expo',[[(100,10),10],[(81,9),9],[(2,1),2],[(1,3),0.333]])
def test_divide(n,expo):
    tol = 1e-3
    assert abs(divide(n[0],n[1])-expo) < tol, f'{divide(n[0],n[1])} =! {expo}'



#test-funks for multi():

def test_multi():
    a = 5
    b = 10
    assert multi(5,10) == 50, 'Error when multiplicating'

@pytest.mark.parametrize('n, expo',[[(100,10),1000],[(5,10),50],[(24,11),264],[(3,12),36]])
def test_multi(n,expo):
    tol = 1e-3
    assert abs(multi(n[0],n[1])-expo) < tol, f'{multi(n[0],n[1])} =! {expo}'
