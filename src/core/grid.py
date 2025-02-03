from core.tile import Tile
from core.object_2D import Object_2D
from core.point import Point
import math

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Grid(Object_2D):
    def __init__(self, grid_width: int, grid_height: int, tile_list: list[Tile] = None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_width = grid_width
        self.grid_height = grid_height

        if tile_list:
            self.tile_list = tile_list
        else:
            self._generate_grid_tiles()

    def _generate_grid_tiles(self):
        tile_list: list[Tile] = []

        for i in range(self.grid_width):
            for j in range(self.grid_height):
                index = i * self.grid_width + j
                # translation_x = 2 * (j - max(0, self.grid_height-1) / 2 )
                # translation_y = 2 * (-i + max(0, self.grid_width-1) / 2 )
                translation_x = 2 * (i - max(0, self.grid_width-1) / 2 )
                translation_y = 2 * (-j + max(0, self.grid_height-1) / 2 )
                tile = Tile(
                    index = index,
                    translation = Point(translation_x, translation_y),
                )
                
                tile_list.append(tile)

        self.tile_list = tile_list

    def add_object_to_tile(self, tile_index: int, object_2d: Object_2D):
        tile: Tile = self.tile_list[tile_index]
        tile.add_object(object_2d)

    def draw(self):
        super().draw()

        for tile in self.tile_list:
            tile: Tile
            tile.draw()
        
        glPushMatrix()

        glEnable(GL_POINT_SMOOTH)
        glPointSize(5)

        glBegin(GL_POINTS)

        glColor3f(1, 1, 0)

        glVertex2f(0, 0)

        glEnd()

        glPopMatrix()