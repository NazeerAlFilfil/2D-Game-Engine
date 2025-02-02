from core.object_2D import Object_2D

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Tile(Object_2D):
    def __init__(self, index: tuple[int, int], object_list: list[Object_2D] = [], *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.index = index
        self.object_list = object_list

    def draw(self):
        super().draw()

        for obj in self.object_list:
            obj: Object_2D
            obj.draw(scaling=self.scaling, rotation=self.rotation, translation=self.translation)

        glPushMatrix()

        glTranslatef(self.translation.x, self.translation.y, 0)
        glRotatef(-self.rotation, 0, 0, 1)
        glScalef(self.scaling.x, self.scaling.y, 1)

        glBegin(GL_LINES)

        glColor3f(1, 0, 0)

        glVertex2f(-1, -1)
        glVertex2f(1, -1)
        
        glVertex2f(1, -1)
        glVertex2f(1, 1)

        glVertex2f(1, 1)
        glVertex2f(-1, 1)

        glVertex2f(-1, 1)
        glVertex2f(-1, -1)

        glEnd()

        glPopMatrix()

    def move_object_to(self, other_tile: 'Tile', object_2d: 'Object_2D'):
        if object_2d in self.object_list:
            self.object_list.remove(object_2d)
            other_tile.object_list.append(object_2d)