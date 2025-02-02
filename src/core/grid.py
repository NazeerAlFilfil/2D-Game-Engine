from core.tile import Tile
from core.object_2D import Object_2D
from core.point import Point
import math

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Grid(Object_2D):
    def __init__(self, grid_width: int, grid_height: int, tile_list: dict[tuple[int, int], Tile] = {}, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_width = grid_width
        self.grid_height = grid_height

        if tile_list:
            self.tile_list = tile_list
        else:
            self._generate_grid_tiles()

    def _generate_grid_tiles(self):
        tile_list: dict[tuple[int, int], Tile] = {}

        for i in range(int(self.grid_width / -2), math.ceil(self.grid_width / 2)):
            for j in range(int(self.grid_height / -2), math.ceil(self.grid_height / 2)):
                tile = Tile(
                    index = (i, j),
                    translation = Point(i*2, j*2),
                )
                
                tile_list[(i, j)] = tile

        self.tile_list = tile_list

    def add_object_to_tile(self, tile_index: tuple[int, int], object_2d: Object_2D):
        tile: Tile = self.tile_list.get(tile_index)

        tile.object_list.append(object_2d)

    def draw(self):
        super().draw()

        for tile in self.tile_list.values():
            tile: Tile
            tile.draw()
        
        glPushMatrix()

        glEnable(GL_POINT_SMOOTH)
        glPointSize(5)

        glBegin(GL_POINTS)

        glColor3f(1, 0, 0)

        glVertex2f(0, 0)
        # glVertex2f(0.2, -0.2)
        # glVertex2f(0.2, 0.2)
        # glVertex2f(-0.2, 0.2)

        glEnd()

        glPopMatrix()