import pygame
from pygame import Vector2
from config import Config
from chunk_manager import ChunkManager 

pygame.init()
pygame.font.init()

RESOLUTION = (1920, 1080)
WINDOW = pygame.display.set_mode(RESOLUTION)


CAMERA_SPEED = 2
movement_direction = Vector2()
camera_position = Vector2()

chunk_manager = ChunkManager()


def quit_app():
    chunk_manager.stop_thread()
    pygame.quit()
    exit(0)


if __name__ == '__main__':
    while True:
        # event processing
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    quit_app()

                # handle inputs
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_ESCAPE:
                            quit_app()

        camera_position += movement_direction * CAMERA_SPEED
        
        for screen_y in range(-1, int(RESOLUTION[1] / Config.TEXTURE_SIZE) + 1):
            for screen_x in range(-1, int(RESOLUTION[0] / Config.TEXTURE_SIZE) + 1):
                WINDOW.blit(chunk_manager.get_chunk(screen_x, screen_y), (screen_x * Config.TEXTURE_SIZE, screen_y * Config.TEXTURE_SIZE))

        pygame.display.flip()