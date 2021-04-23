import numpy as np
import matplotlib.pyplot as plt
from chaos_game import ChaosGame

class Variations:
    '''
    the constructor here takes two lists of cooridnates
    as well as the name of the transformation to use
    and defines _func for later use
    '''
    def __init__(self, x, y, name):
        if type(name) != str:
            raise AttributeError('name must be a string')
        self.x = x
        self.y = y
        self.name = name
        self._func = getattr(Variations, name)(x, y)

    '''
    here we implement the transformations
    as static methods
    '''
    @staticmethod
    def disc(x, y):
        theta = np.arctan2(x, y)
        r = np.sqrt(x**2 + y**2)
        u = theta/np.pi*(np.sin(np.pi*r))
        v = theta/np.pi*(np.cos(np.pi*r))
        return np.array([u, v])

    @staticmethod
    def handkerchief(x, y):
        theta = np.arctan2(x, y)
        r = np.sqrt(x**2 + y**2)
        u = r*np.sin(theta + r)
        v = r*np.cos(theta - r)
        return np.array([u, v])

    @staticmethod    
    def linear(x, y):
        u = x
        v = y
        return np.array([u, v])
    
    @staticmethod
    def swirl(x, y):
        r = np.sqrt(x**2 + y**2)
        u = x*np.sin(r**2) - y*np.cos(r**2)
        v = x*np.cos(r**2) + y*np.sin(r**2)
        return np.array([u, v])

    @staticmethod
    def ex(x, y):
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan2(x, y)
        ro0 = np.sin(theta + r)
        ro1 = np.cos(theta - r)
        return r*np.array([ro0**3 + ro1**3,\
            ro0**3 - ro1**3])

    @staticmethod
    def exponential(x, y):
        return np.exp(x - 1)*np.array([np.cos(np.pi*y), np.sin(np.pi*y)])

    '''
    returning the transformation as two lists
    '''
    def transform(self):
        return self._func

    '''
    using n to define which kind of ngon
    using name to define which transformation
    using r to define ratios
    and using steps to define how many steps
        used
    '''
    @classmethod
    def from_chaos_game(cls,  n, name, r=1/2, steps= 10000):
        instance = ChaosGame(n, r)
        instance.iterate(steps)
        if name == 'color':
            return instance.gradient_color()
        x = instance.x[:,0]
        y = instance.x[:,1]
        inst = Variations(x, y, name)
        return inst.transform()

'''
creating a function that takes in
    two variations and combines them
        returning the combination
'''
def linear_combination_wrap(var1, var2):
    def combinations(w):
        return w*var1 + (1-w)*var2
    return combinations

if __name__ == "__main__":
    '''
    here we are solving 4b
    '''
    N = 100
    grid_values = np.linspace(-1, 1, N)
    x, y = np.meshgrid(grid_values, grid_values)
    x_values = x.flatten()
    y_values = y.flatten()
        
    transformations = ["linear", "handkerchief", "swirl", "disc", "ex", "exponential"]
    variations = [Variations(x_values, y_values, version) for version in transformations]

    
    fig, axs = plt.subplots(2, 2, figsize=(9, 9))
    for i, (ax, variation) in enumerate(zip(axs.flatten(), variations)):
    
        
        u, v = variation.transform()
        
        #ax.plot(u, -v, markersize=1, marker=".", linestyle="", color="black")
        ax.scatter(u, -v, s=0.2, marker=".", color = 'black')
        ax.set_title(variation.name)
        ax.axis("off")

    #fig.savefig("figures/variations_4b.png")
    plt.show()
    #4b end

    '''
    Under we have part 4c, here
    we plot the 4-gon's with 10000 steps
    with different transformations.
    '''
    u,v = Variations.from_chaos_game(4,'linear', r=1/3, steps=10000)
    color = Variations.from_chaos_game(4, 'color', r=1/3, steps=10000)
    transformations = ["linear", "handkerchief", "swirl", "disc", "ex", "exponential"]

    
    for i in transformations:
        u, v = Variations.from_chaos_game(4, i, r=1/3, steps=10000)
        #ax.plot(u, -v, markersize=1, marker=".", linestyle="", color="black")
        plt.scatter(u, -v, s=0.2, marker=".", c = color, label = f'{i}')
        plt.axis("equal")
        plt.legend()
        plt.show()
    #fig.savefig("figures/variations_4b.png")
    #plt.show()
    #4c end

    '''
    4d tests under
    '''
    coeffs = np.linspace(0, 1, 4)

    variation1 = Variations.from_chaos_game(3, "ex")
    variation2 = Variations.from_chaos_game(3, "linear")
    variation12 = linear_combination_wrap(variation1, variation2)    
        
    fig, axs = plt.subplots(2, 2, figsize=(9, 9))
    for ax, w in zip(axs.flatten(), coeffs):
        u, v = variation12(w)
        
        ax.scatter(u, -v, s=0.2, marker=".", c = color)
        ax.set_title(f"weight = {w:.2f}")
        ax.axis("off")
    plt.show()
    #end
    pass