import numpy as np 
from scipy.stats import levy 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

class Walker: 

    def __init__(self, dim: int) -> None:
        self.pos_x = 0
        self.pos_y = 0
        self.pos_z = 0

        if(dim == 3): 
            self.x_arr = []
            self.y_arr = []
            self.z_arr = []    
        else:
            self.x_arr = []
            self.y_arr = []
        
        self.alpha = 0.35
        self.beta = 0.5
        self.dim = dim
        self.max_dist = 50

    def update_pos(self):
        rand_levy = levy.rvs(self.alpha,self.beta, size=self.dim)
        
        if bool(random.getrandbits(1)): 
            self.pos_x += min(self.max_dist, rand_levy[0])
        else: 
            self.pos_x -= min(self.max_dist, rand_levy[0])

        if(bool(random.getrandbits(1))): 
            self.pos_y += min(self.max_dist, rand_levy[1])
        else:
            self.pos_y -= min(self.max_dist, rand_levy[1])



        if self.dim == 3: 
            self.pos_z = self.pos_z + rand_levy[2]
            self.x_arr.append(self.pos_x)
            self.y_arr.append(self.pos_y)
            self.z_arr.append(self.pos_z)
            
        else:
            self.x_arr.append(self.pos_x)
            self.y_arr.append(self.pos_y)

    def update(self, num, x, y, line): 
        line.set_data(x[:num], y[:num])
        x_min = np.amin(self.x_arr)
        x_max = np.amax(self.x_arr)
        y_min = np.amin(self.y_arr)
        y_max = np.amax(self.y_arr)
        line.axes.axis([x_min, x_max, y_min, y_max])
        return line,

    def show_path(self): 
        if self.dim == 3: 
            raise Exception("Not Implemented Yet")
        fig, ax = plt.subplots()

        line, = ax.plot(self.x_arr, self.y_arr, 'b')

        visual = animation.FuncAnimation(fig, self.update, len(self.x_arr), fargs=[self.x_arr, self.y_arr, line],
                                            interval =100, blit=False)

        plt.show()
            
walker = Walker(2)
t_step = 100


for i in range(t_step):
    print("x: {}".format(walker.pos_x))
    print("y: {}".format(walker.pos_y))
    print("*" * 10) 
    walker.update_pos()
    
walker.show_path()

 