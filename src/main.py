import pygame
from pygame import Vector2
from config import Config
from chunk_manager import ChunkManager 
from math import floor


pygame.init()
pygame.font.init()

RESOLUTION = (1920, 1080)
WINDOW = pygame.display.set_mode(RESOLUTION)
CONSOLAS_PATH = pygame.font.match_font('Ubuntu mono')
CHUNK_FONT = pygame.font.Font(CONSOLAS_PATH, 18)

CAMERA_SPEED = 3
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

                        case pygame.K_w:
                            movement_direction.y -= 1
                        case pygame.K_s:
                            movement_direction.y += 1
                        case pygame.K_a:
                            movement_direction.x -= 1
                        case pygame.K_d:
                            movement_direction.x += 1

                case pygame.KEYUP:
                    match event.key:
                        case pygame.K_w:
                            movement_direction.y -= -1
                        case pygame.K_s:
                            movement_direction.y += -1
                        case pygame.K_a:
                            movement_direction.x -= -1
                        case pygame.K_d:
                            movement_direction.x += -1

        camera_position += movement_direction * CAMERA_SPEED


        WINDOW.fill((0, 0, 25))
        # for screen_y in range(-1, int(RESOLUTION[1] / Config.TEXTURE_SIZE) + 2):
        #     for screen_x in range(-1, int(RESOLUTION[0] / Config.TEXTURE_SIZE) + 2):  
        for screen_y in range(0, int(RESOLUTION[1] / Config.TEXTURE_SIZE) + 1):
            for screen_x in range(0, int(RESOLUTION[0] / Config.TEXTURE_SIZE) + 1):  

                cc_x = screen_x + floor(camera_position.x / Config.TEXTURE_SIZE)
                cc_y = screen_y + floor(camera_position.y / Config.TEXTURE_SIZE)

                chunk_data = chunk_manager.get_chunk(cc_x, cc_y)

                WINDOW.blit(chunk_data.texture, (screen_x * Config.TEXTURE_SIZE - floor(camera_position.x % Config.TEXTURE_SIZE), 
                                            screen_y * Config.TEXTURE_SIZE - floor(camera_position.y % Config.TEXTURE_SIZE)))
                

                chunk_position_debug = CHUNK_FONT.render(f"[x, y] = {cc_x}, {cc_y}", True, (255, 255, 255))
                chunk_name_debug = CHUNK_FONT.render(f"{chunk_data.name}", True, (255, 255, 255))

                WINDOW.blit(chunk_position_debug, 
                            (screen_x * Config.TEXTURE_SIZE - floor(camera_position.x % Config.TEXTURE_SIZE) + 5, 
                             screen_y * Config.TEXTURE_SIZE - floor(camera_position.y % Config.TEXTURE_SIZE) + 5))
                WINDOW.blit(chunk_name_debug, 
                            (screen_x * Config.TEXTURE_SIZE - floor(camera_position.x % Config.TEXTURE_SIZE) + 5, 
                             screen_y * Config.TEXTURE_SIZE - floor(camera_position.y % Config.TEXTURE_SIZE) + 5 + 22))

        pygame.display.flip()