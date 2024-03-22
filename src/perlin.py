import random
import math
import numpy
from pygame import Surface, Vector2
from config import Config


class Perlin:
    def __init__(self) -> None:
        self.CORNERS = [
            Vector2(0,  0),
            Vector2(0, -1),
            Vector2(1,  0),
            Vector2(1, -1)
        ]

        self.gradients = {}

    
    def _generate_gradient(self, x, y):
        angle = random.random() * 2 * math.pi
        self.gradients[(x, y)] =  Vector2(math.cos(angle), math.sin(angle))
        

    def _ease(self, x):
        return 3*x*x - 2*x*x*x

    def get_texture(self, x, y) -> Surface:
        texture = Surface((Config.TEXTURE_SIZE, Config.TEXTURE_SIZE))

        corners_coordinates = [(x + corner.x, 
                                y + corner.y) 
                                for corner in self.CORNERS]
        
        for corner in corners_coordinates:
            if corner not in self.gradients:
                self._generate_gradient(*corner)

        local_gradients = [ self.gradients[corner] for corner in corners_coordinates ]


        for x_texture in range(Config.TEXTURE_SIZE):
            for y_texture in range(Config.TEXTURE_SIZE):

                position = Vector2( 
                    x_texture / Config.TEXTURE_SIZE, 
                    y_texture / Config.TEXTURE_SIZE 
                )
                
                dots = [ local_gradients[vector_index].dot(position - self.CORNERS[vector_index] ) for vector_index in range(len(local_gradients)) ]

                intx1 = dots[0] + self._ease(position.x) * (dots[2] - dots[0])
                intx2 = dots[1] + self._ease(position.x) * (dots[3] - dots[1])
                sample = intx1 + self._ease(1 - position.y) * (intx2 - intx1)
                color = (sample + 1) / 2 * 255
                clamped_color = min(max(0, color), 255)
                
                texture.set_at((x_texture, y_texture), (clamped_color, clamped_color, clamped_color))
        
        return texture
    

    def get_value(self, x, y, offset_x, offset_y):
        corners_coordinates = [(x + corner.x, 
                                y + corner.y) 
                                for corner in self.CORNERS]
        
        for corner in corners_coordinates:
            if corner not in self.gradients:
                self._generate_gradient(*corner)

        local_gradients = [ self.gradients[corner] for corner in corners_coordinates ]
                
        dots = [ local_gradients[vector_index].dot(Vector2(offset_x, offset_y) - self.CORNERS[vector_index] ) for vector_index in range(len(local_gradients)) ]

        intx1 = dots[0] + self._ease(offset_x) * (dots[2] - dots[0])
        intx2 = dots[1] + self._ease(offset_x) * (dots[3] - dots[1])
        sample = intx1 + self._ease(1 - offset_y) * (intx2 - intx1)
        corrected = (sample + 1) / 2
        clamped = min(max(0, corrected), 1)
        return clamped
                

if __name__ == '__main__':
    p = Perlin()
    p.get_value(0, 0, 0.5, 0.5)