from pygame import Surface


class chunk_manager:
    def __init__(self) -> None:
        self.chunks = {}
        self.chunks.setdefault()
    
    def get_chunk(self, x:int, y:int) -> Surface:
        chunk_key = (x, y)