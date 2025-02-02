import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from core.grid import Grid
from core.tile import Tile
from core.object_2D import Object_2D
from core.point import Point

def main():
    pygame.init()
    pygame.display.set_mode((1600, 900), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Python Engine")
    glViewport(0, 0, 1600, 900)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-16, 16, -9, 9)
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    clock = pygame.time.Clock()
    FPS = 60

    SCALE = 1

    object_list = []

    white_rock_1 = Object_2D(
        sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/white/rock.png',
        scaling=Point(1, 1) * SCALE,
        translation=Point(-3.5, 3.5) * SCALE,
        )
    white_horse_1 = Object_2D(
        sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/white/horse.png',
        scaling=Point(1, 1) * SCALE,
        translation=Point(-2.5, 3.5) * SCALE,
        )
    white_bishop_1 = Object_2D(
        sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/white/bishop.png',
        scaling=Point(1, 1) * SCALE,
        translation=Point(-1.5, 3.5) * SCALE,
        )
    white_king = Object_2D(
        sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/white/king.png',
        scaling=Point(1, 1) * SCALE,
        translation=Point(-0.5, 3.5) * SCALE,
        )
    white_queen = Object_2D(
        sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/white/queen.png',
        scaling=Point(1, 1) * SCALE,
        translation=Point(0.5, 3.5) * SCALE,
        )
    white_bishop_2 = Object_2D(
        sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/white/bishop.png',
        scaling=Point(1, 1) * SCALE,
        translation=Point(1.5, 3.5) * SCALE,
        )
    white_horse_2 = Object_2D(
        sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/white/horse.png',
        scaling=Point(1, 1) * SCALE,
        translation=Point(2.5, 3.5) * SCALE,
        )
    white_rock_2 = Object_2D(
        sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/white/rock.png',
        scaling=Point(1, 1) * SCALE,
        translation=Point(3.5, 3.5) * SCALE,
        )
    
    object_list.append(white_rock_1)
    object_list.append(white_horse_1)
    object_list.append(white_bishop_1)
    object_list.append(white_king)
    object_list.append(white_queen)
    object_list.append(white_bishop_2)
    object_list.append(white_horse_2)
    object_list.append(white_rock_2)
    
    white_pawn_1 = Object_2D(
        sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/white/pawn.png',
        scaling=Point(1, 1) * SCALE,
        translation=Point(-3.5, 2.5) * SCALE,
        )
    white_pawn_2 = Object_2D(
        sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/white/pawn.png',
        scaling=Point(1, 1) * SCALE,
        translation=Point(-2.5, 2.5) * SCALE,
        )
    white_pawn_3 = Object_2D(
        sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/white/pawn.png',
        scaling=Point(1, 1) * SCALE,
        translation=Point(-1.5, 2.5) * SCALE,
        )
    white_pawn_4 = Object_2D(
        sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/white/pawn.png',
        scaling=Point(1, 1) * SCALE,
        translation=Point(-0.5, 2.5) * SCALE,
        )
    white_pawn_5 = Object_2D(
        sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/white/pawn.png',
        scaling=Point(1, 1) * SCALE,
        translation=Point(0.5, 2.5) * SCALE,
        )
    white_pawn_6 = Object_2D(
        sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/white/pawn.png',
        scaling=Point(1, 1) * SCALE,
        translation=Point(1.5, 2.5) * SCALE,
        )
    white_pawn_7 = Object_2D(
        sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/white/pawn.png',
        scaling=Point(1, 1) * SCALE,
        translation=Point(2.5, 2.5) * SCALE,
        )
    white_pawn_8 = Object_2D(
        sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/white/pawn.png',
        scaling=Point(1, 1) * SCALE,
        translation=Point(3.5, 2.5) * SCALE,
        )
    
    object_list.append(white_pawn_1)
    object_list.append(white_pawn_2)
    object_list.append(white_pawn_3)
    object_list.append(white_pawn_4)
    object_list.append(white_pawn_5)
    object_list.append(white_pawn_6)
    object_list.append(white_pawn_7)
    object_list.append(white_pawn_8)

    black_rock_1 = Object_2D(
        sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/black/rock.png',
        scaling=Point(1, 1) * SCALE,
        translation=Point(-3.5, -3.5) * SCALE,
        )
    black_horse_1 = Object_2D(
        sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/black/horse.png',
        scaling=Point(1, 1) * SCALE,
        translation=Point(-2.5, -3.5) * SCALE,
        )
    black_bishop_1 = Object_2D(
        sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/black/bishop.png',
        scaling=Point(1, 1) * SCALE,
        translation=Point(-1.5, -3.5) * SCALE,
        )
    black_king = Object_2D(
        sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/black/king.png',
        scaling=Point(1, 1) * SCALE,
        translation=Point(-0.5, -3.5) * SCALE,
        )
    black_queen = Object_2D(
        sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/black/queen.png',
        scaling=Point(1, 1) * SCALE,
        translation=Point(0.5, -3.5) * SCALE,
        )
    black_bishop_2 = Object_2D(
        sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/black/bishop.png',
        scaling=Point(1, 1) * SCALE,
        translation=Point(1.5, -3.5) * SCALE,
        )
    black_horse_2 = Object_2D(
        sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/black/horse.png',
        scaling=Point(1, 1) * SCALE,
        translation=Point(2.5, -3.5) * SCALE,
        )
    black_rock_2 = Object_2D(
        sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/black/rock.png',
        scaling=Point(1, 1) * SCALE,
        translation=Point(3.5, -3.5) * SCALE,
        )
    
    object_list.append(black_rock_1)
    object_list.append(black_horse_1)
    object_list.append(black_bishop_1)
    object_list.append(black_king)
    object_list.append(black_queen)
    object_list.append(black_bishop_2)
    object_list.append(black_horse_2)
    object_list.append(black_rock_2)
    
    black_pawn_1 = Object_2D(
        sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/black/pawn.png',
        scaling=Point(1, 1) * SCALE,
        translation=Point(-3.5, -2.5) * SCALE,
        )
    black_pawn_2 = Object_2D(
        sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/black/pawn.png',
        scaling=Point(1, 1) * SCALE,
        translation=Point(-2.5, -2.5) * SCALE,
        )
    black_pawn_3 = Object_2D(
        sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/black/pawn.png',
        scaling=Point(1, 1) * SCALE,
        translation=Point(-1.5, -2.5) * SCALE,
        )
    black_pawn_4 = Object_2D(
        sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/black/pawn.png',
        scaling=Point(1, 1) * SCALE,
        translation=Point(-0.5, -2.5) * SCALE,
        )
    black_pawn_5 = Object_2D(
        sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/black/pawn.png',
        scaling=Point(1, 1) * SCALE,
        translation=Point(0.5, -2.5) * SCALE,
        )
    black_pawn_6 = Object_2D(
        sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/black/pawn.png',
        scaling=Point(1, 1) * SCALE,
        translation=Point(1.5, -2.5) * SCALE,
        )
    black_pawn_7 = Object_2D(
        sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/black/pawn.png',
        scaling=Point(1, 1) * SCALE,
        translation=Point(2.5, -2.5) * SCALE,
        )
    black_pawn_8 = Object_2D(
        sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/black/pawn.png',
        scaling=Point(1, 1) * SCALE,
        translation=Point(3.5, -2.5) * SCALE,
        )
    
    object_list.append(black_pawn_1)
    object_list.append(black_pawn_2)
    object_list.append(black_pawn_3)
    object_list.append(black_pawn_4)
    object_list.append(black_pawn_5)
    object_list.append(black_pawn_6)
    object_list.append(black_pawn_7)
    object_list.append(black_pawn_8)

    pawn = Object_2D(
        sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/black/pawn.png',
        )
    rock = Object_2D(
        sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/black/rock.png',
        )

    tile = Tile(
        index=(0, 0),
        object_list=[rock, pawn],
        #sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/tiles/blue.png',
        translation=Point(-1, 0),
        #scaling=Point(1, 1),
        )
    
    tile_2 = Tile(
        index=(0, 1),
        object_list=[],
        #sprite='C:/Users/hassan.ali/Desktop/Projects/2D-Game-Engine/assets/images/tiles/yellow.png',
        translation=Point(1, 0),
        #scaling=Point(1, 1),
    )

    tile.move_object_to(tile_2, rock)
    
    #tile.object_list.append(pawn)

    grid = Grid(
        grid_width=8,
        grid_height=8,
    )

    grid.add_object_to_tile((0, 0), rock)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        glClearColor(0.5, 0.5, 0.5, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # for obj in object_list:
        #     obj: Object_2D
        #     obj.draw()

        # tile.draw()
        # tile_2.draw()

        grid.draw()

        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()
                
if __name__ == '__main__':
    main()