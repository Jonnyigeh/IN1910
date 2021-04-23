from chaos_game import ChaosGame
import pytest

def test_values_error_n(): #checking if (n >= 3)==true
    with pytest.raises(AttributeError) as g:
        assert ChaosGame(2)
    assert  str(g.value) == 'n >= 3, is false'

def test_values_error_r(): #Checking if (0 < r and r < 1)==true
    with pytest.raises(AttributeError) as g:
        assert ChaosGame(3,1)
    assert  str(g.value) == '0 < r and r < 1, is false'

@pytest.mark.parametrize('x', [3, 5, 7, 8])
def test_points(x): #Checking that it creates the correct amount of points
    a = ChaosGame(x)
    assert len(a.apoints)==x


'''
We are not testing value 0 because 0 will
be wrong as it is predetermined without 
the equation.
'''
@pytest.mark.parametrize('x', [1, 50, 700, 8000])
def test_c_values(x): #Checking values for gradient color
    a = ChaosGame(3)
    a.iterate(10000)
    c = a.gradient_color()
    assert c[x] == (c[x-1] + a.j[x])/2

@pytest.mark.parametrize('x', [4, 50, 700, 8000])
def test_x_values(x): #Checking List lengths
    a = ChaosGame(3)
    a.iterate(x)
    assert len(a.x) == x and len(a.x) == len(a.j) and len(a.x) == len(a.gradient_color())

def test_savepng_error():
    a = ChaosGame(3)
    a.iterate(10000)
    with pytest.raises(ValueError) as e:
        assert a.savepng('test.not')
    assert str(e.value) == 'can only be .png, please do not use . in filename'
        
if __name__ == "__main__":
    pass
