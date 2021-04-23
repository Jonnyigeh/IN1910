import numpy as np
import matplotlib.pyplot as plt

class ChaosGame:
    '''
    Initializing the class checking
        the initial n and r value is within
            acceptable parameters
    '''
    def __init__(self, n, r=1/2): #n \geq 3, 0 < r < 1
        if n < 3: #making sure it is enough points
            raise AttributeError('n >= 3, is false') #raising error
        elif 0 >= r or r >= 1: #checking if it is distributed
            raise AttributeError('0 < r and r < 1, is false') #raising error 
        else:
            #initializing
            self.n = n 
            self.r = r
            self._generate_ngon()

    def _generate_ngon(self): #defining ngon
        '''
        generating the ngon by the corners
        '''
        theta = np.linspace(0, 2*np.pi, self.n+1)
        points = []
        for i in range(self.n):
            points.append([np.sin(theta[i]), np.cos(theta[i])])
        self.apoints = np.array(points)

    def plot_ngon(self): #plotting ngon
        '''
        plotting the ngon using plt.scatter
        '''
        plt.scatter(*zip(*self.apoints))
        plt.show()

    def _starting_point(self):
        '''
        choosing starting point
            and weights
        '''
        weights = np.zeros(self.n)
        for i in range(self.n):
            weights[i] = np.random.random()
        weights *= (1 / sum(weights))
        startpoint = np.dot(weights, self.apoints)
        return startpoint

    def iterate(self, steps, discard=5):
        '''
        starting iteration by pulling 
            starting points
        discarding discard amount of
            steps, then running steps amount of steps
        '''
        x0 = self._starting_point()
        self.x = np.zeros((steps, 2))
        self.x[0] = x0
        self.j = [0] #making sure j is the same length as x
        for _ in range(discard+1):
            j = np.random.randint(0, self.n)
            x0 = self.r*x0 + (1 - self.r)*self.apoints[int(j)]
        for i in range(steps-1):
            self.j.append(np.random.randint(0, self.n))
            self.x[i+1] = self.r*self.x[i] + (1 - self.r)*self.apoints[int(self.j[i])]

    def gradient_color(self):
        '''
        Creating color list using a 
            predetermined equation,
                no input needed
        '''
        c = np.zeros(len(self.x))
        c[0] = self.j[0]
        for i in range(len(self.x)-1):
            c[i+1] = (c[i] + self.j[i+1])/2
        return c

    def plot(self, color=False, cmap="jet"):
        '''
        Plotting, use color boolean to choose
            if you want color or not, and cmap to chose
                colormap
        '''
        if color:
            plt.scatter(*zip(*self.x),c = self.gradient_color(), marker = ".", s=0.1)
        elif not(color):
            plt.scatter(*zip(*self.x),c = 'black', marker = ".", s=0.1)
            plt.axis("equal")
        plt.colorbar()

    def savepng(self, outfile, color = False, cmap = "jet"):
        '''
        Creating the figure and saving it.
            While checking if filename has .png 
                added or not.
        '''
        self.plot(color) #creating the figure
        if outfile[-4:] == '.png':
            plt.savefig(outfile)
        elif len(outfile.split(".")) == 1 or outfile[0]=='.':
            plt.savefig(outfile + '.png') #saving the figure
        else:
            raise ValueError('can only be .png, please do not use . in filename')


if __name__ == "__main__":
    for i in range(3,9):
        a = ChaosGame(i)
        a.plot_ngon()        
        #print(a.points)
        plt.show()
    b = ChaosGame(3)
    x = np.zeros(1000)
    y = np.zeros(1000)
    for i in range(1000):
        x[i], y[i] = b._starting_point()
    plt.scatter(x,y)
    plt.show()    
    b.iterate(10000)
    b.plot(color=True)
    plt.show()
    #b.savepng('try1')
    rv = [1/2, 1/3, 1/3, 3/8, 1/3]
    nv = [3, 4, 5, 5, 6]
    for i in range(5):
        c = ChaosGame(nv[i], rv[i])
        c.iterate(10000)
        c.savepng(f'./figures/chaos{i+1}.png')
        plt.show()
    pass