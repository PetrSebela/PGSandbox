import random
import math
import numpy

class Perlin:
    def __init__(self) -> None:
        self.CORNERS = [
            (0, 0),
            (0, 1),
            (1, 0),
            (1, 1),
        ]
        self.gradients = {}

    
    def _generate_gradient(self, x, y):
        self.gradients[(x, y)] =  random.random() * 2 * math.pi

    def _ease(self, x):
        return x
        # return 3*x*x - 2*x*x*x

    def get_value(self, chunk_x, chunk_y, offset_x, offset_y) -> float:
        corners = [ (chunk_x + corner[0], chunk_y + corner[1]) for corner in self.CORNERS]

        for corner in corners:
            if corner not in self.gradients:
                self._generate_gradient(*corner)


        local_gradients = [self.gradients[corner] for corner in corners]

        dots = [(offset_x - self.CORNERS[i][0]) * math.cos(local_gradients[i]) + 
                (offset_y - self.CORNERS[i][1]) * math.sin(local_gradients[i]) 
                for i in range(len(self.CORNERS))]
        
        intx1 = dots[2] + self._ease(offset_x - math.floor(offset_x)) * (dots[3]-dots[2])
        intx2 = dots[0] + self._ease(offset_x - math.floor(offset_x)) * (dots[1]-dots[0])
        return intx1 + self._ease(offset_y - math.floor(offset_y)) * (intx2 - intx1)


if __name__ == '__main__':
    p = Perlin()
    p.get_value(0, 0, 0.5, 0.5)