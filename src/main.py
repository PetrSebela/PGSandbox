import pygame
from pygame import Vector2

pygame.init()
pygame.font.init()

RESOLUTION = (1920, 1080)
WINDOW = pygame.display.set_mode(RESOLUTION)


CAMERA_SPEED = 2
movement_direction = Vector2()
camera_position = Vector2()

def quit_app():
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
        

        pygame.display.flip()