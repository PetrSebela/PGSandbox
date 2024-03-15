def get_texture_at(x:int, y:int, size:int) -> list[list[(int, int, int)]]:
    texture = [[(int(x / size * 255),int(y / size * 255),0) for x in range(size)] for y in range(size)]
    return texture
