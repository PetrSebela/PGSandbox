from perlin import Perlin
from pygame import Surface
from config import Config
from math import floor

OCTAVES = 4

octave_generators = [ Perlin() for _ in range(OCTAVES) ]
PERSISTENCE = 0.4
ROUGHNESS = 3.5


def get_texture_at(x:int, y:int, size:int) -> list[list[(int, int, int)]]:
    texture = Surface((Config.TEXTURE_SIZE, Config.TEXTURE_SIZE))
    frequency = 1
    amplitude = 1

    for y_texture in range(Config.TEXTURE_SIZE):
        for x_texture in range(Config.TEXTURE_SIZE):
            sample = 0
            for octave_index in range(OCTAVES):
                cheat_x = (x * Config.TEXTURE_SIZE + x_texture) * frequency
                cheat_y = (y * Config.TEXTURE_SIZE + y_texture) * frequency

                s = octave_generators[octave_index].get_value(
                    floor(cheat_x / Config.TEXTURE_SIZE),
                    floor(cheat_y / Config.TEXTURE_SIZE),
                    cheat_x / Config.TEXTURE_SIZE % 1,
                    cheat_y / Config.TEXTURE_SIZE % 1,
                ) 

                sample += s * amplitude
                amplitude *= PERSISTENCE
                frequency *= ROUGHNESS

            sample /= OCTAVES
            sample *= 255
            sample = min(max(0, sample), 255)

            frequency = 1
            amplitude = 1


            texture.set_at((x_texture, y_texture), (sample, sample, sample))
    return texture
