from pygame import Surface
import pygame
from config import Config
from generator import get_texture_at
from name_generator import get_unique_random_name
import threading


def push_array2d_to_texture_instance(array:list[list[(int, int, int)]], texture:Surface) -> None:
    for y, row in enumerate(array):
        for x, pixel in enumerate(row):
            texture.set_at((x, y), pixel)


class Chunk:
    def __init__(self, x:int, y:int) -> Surface:
        self.texture = Surface((Config.TEXTURE_SIZE,Config.TEXTURE_SIZE))
        self.position = (x, y)
        self.name = get_unique_random_name()


class ChunkManager:
    def __init__(self) -> None:
        self.chunks = {}
        self.to_generate = []
        self.active = True

        THREAD_COUNT = 1
        self.gen_lock = threading.Lock()
        self.threads = [threading.Thread(target=self.thread_worker,args=(thread_id,)) for thread_id in range(THREAD_COUNT)]
        
        for thread in self.threads:
            thread.start()


    def thread_worker(self, worker_id):
        while self.active:
            chunk = None
            if len(self.to_generate) > 0:
                with self.gen_lock:
                    chunk = self.to_generate.pop(0)

            if chunk:            
                print(f"Thread {worker_id} is processing {chunk.name}")
                texture_array = get_texture_at(*chunk.position, Config.TEXTURE_SIZE)
                push_array2d_to_texture_instance(texture_array, chunk.texture)


    def stop_thread(self):
        self.active = False
        for thread in self.threads:
            thread.join()


    def generate_new_chunk(self, x:int, y:int):
        chunk = Chunk(x, y)
        self.to_generate.append(chunk)
        self.chunks[chunk.position] = chunk
        return chunk


    def get_chunk(self, x:int, y:int) -> Chunk:
        chunk_key = (x, y)
        if chunk_key not in self.chunks:
            self.generate_new_chunk(x, y)

        return self.chunks[chunk_key]