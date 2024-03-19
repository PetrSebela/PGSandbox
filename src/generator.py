from perlin import Perlin
import math
p = Perlin()


def get_texture_at(x:int, y:int, size:int) -> list[list[(int, int, int)]]:
    print(p.gradients)
    # texture = [[(int(x / size * 255),int(y / size * 255),0) for x in range(size)] for y in range(size)]
    print(f"{x},{y}")
    texture = []
    for y_texture in range(size):
        row = []
        for x_texture in range(size):
            value = (p.get_value(   x, 
                                    y, 
                                    y_texture / size, 
                                    x_texture / size) + 1) / 2 * 255
            value = max(min(value, 255), 0)
            row.append((value, value, value))
        texture.append(row)


    return texture
