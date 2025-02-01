from core.point import Point
from PIL import Image
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Object_2D:
    '''
    An Object class to represent 2D objects.
    '''

    def __init__(
            self,

            sprite: str,

            #global_origin: Point = Point(0, 0),
            #local_origin: Point = Point(0, 0),
            #z_level: int = 0,

            scaling: Point = Point(1, 1),
            rotation: float = 0,
            translation: Point = Point(0, 0),

            # velocity: Point = Point(0, 0),
            # acceleration: Point = Point(0, 0),
            
            visible: bool = True,
            active: bool = True,
            ):
        # sprite path
        self.sprite = sprite

        # coordinates
        # self.global_origin = global_origin
        # self.local_origin = local_origin
        # self.z_level = z_level
        
        # transformation
        self.scaling = scaling
        self.rotation = rotation
        self.translation = translation

        # physics
        # self.velocity = velocity
        # self.acceleration = acceleration

        # visibility & activation
        self.visible = visible
        self.active = active

        self.texture_id = self._load_texture()

        # methods
        # self.on_click
        # self.update
        # self.draw

    def _load_texture(self) -> int:
        '''
        Loads a texture from an image file and prepares it for use in OpenGL.

        This method opens the image file, converts it to RGBA format, and then
        uploads the texture to OpenGL with nearest-neighbor filtering to avoid
        smoothing. It also sets texture wrapping parameters
        to clamp the texture at its edges, preventing any unwanted stretching.

        The texture is stored in OpenGL with a generated texture ID, which is returned
        for further use in the game engine.

        Returns:
            texture_id (int): The OpenGL texture ID of the loaded texture.
        '''

        # Open the image file using PIL
        image = Image.open(self.sprite)

        # Convert the image to RGBA format (Red, Green, Blue, Alpha for transparency)
        image = image.convert('RGBA')

        # Convert the image data to raw bytes in RGBA format
        image_data = image.tobytes('raw', 'RGBA', 0, -1)

        # Get the width and height of the image
        width, height = image.size

        # Generate a new OpenGL texture ID
        texture_id = glGenTextures(1)

        # Bind the generated texture ID to the 2D texture target
        glBindTexture(GL_TEXTURE_2D, texture_id)

        # Set the texture filtering method to nearest-neighbor (no smoothing)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

        # Set the texture wrapping mode to clamp to the edges (no tiling)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)

        # Upload the image data to OpenGL as a 2D texture
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)

        # Return the texture ID for future use (binding the texture to objects)
        return texture_id
    
    def draw(self, scaling: 'Point' = Point(1, 1), rotation: float = 0, translation: 'Point' = Point(0, 0)):
        '''
        Draws the object on the screen by applying transformations, binding the texture, 
        and rendering a textured rectangle (quad) that represents the object.

        This method handles the drawing process for the object, including translation, 
        rotation, and scaling. It also binds the previously loaded texture and draws the 
        object as a textured quad (square/rectangle) with the appropriate transformations.

        The object is drawn only if it is marked as visible.

        No return value; the method directly modifies the OpenGL state to render the object.
        '''
        
        # Check if the object is visible. If not, skip the drawing process.
        if self.visible:
            # Save the current transformation matrix
            glPushMatrix()

            # Combine provided values
            scaling = self.scaling + scaling
            rotation = self.rotation + rotation
            translation = self.translation + translation

            # Apply translation transformation based on the object's position.
            # The translation vector moves the object along the x and y axes, and optionally on the z-axis.
            glTranslatef(translation.x, translation.y, 0)

            # Apply rotation transformation. The object is rotated around the origin (0, 0, 0).
            # The rotation is performed around the z-axis in the 2D plane.
            glRotatef(-rotation, 0, 0, 1)

            # Apply scaling transformation. The object is scaled along the x and y axes.
            # The z-axis scaling is set to 1, as the object is 2D.
            glScalef(scaling.x, scaling.y, 1)

            # Enable 2D textures for this drawing operation
            glEnable(GL_TEXTURE_2D)

            # Bind the texture that was previously loaded (using the texture ID)
            glBindTexture(GL_TEXTURE_2D, self.texture_id)

            # Begin drawing a quad (rectangle) with texture coordinates applied.
            glBegin(GL_QUADS)

            # Define the first vertex of the quad at the bottom-left corner.
            # glTexCoord2f(0, 0) sets the texture coordinate for the bottom-left corner of the sprite.
            # glVertex2f(-0.5, -0.5) sets the vertex position in the 2D plane.
            glTexCoord2f(0, 0)
            glVertex2f(-0.5, -0.5)

            # Define the second vertex of the quad at the bottom-right corner.
            # glTexCoord2f(1, 0) sets the texture coordinate for the bottom-right corner of the sprite.
            # glVertex2f(0.5, -0.5) sets the vertex position in the 2D plane.
            glTexCoord2f(1, 0)
            glVertex2f(0.5, -0.5)

            # Define the third vertex of the quad at the top-right corner.
            # glTexCoord2f(1, 1) sets the texture coordinate for the top-right corner of the sprite.
            # glVertex2f(0.5, 0.5) sets the vertex position in the 2D plane.
            glTexCoord2f(1, 1)
            glVertex2f(0.5, 0.5)

            # Define the fourth vertex of the quad at the top-left corner.
            # glTexCoord2f(0, 1) sets the texture coordinate for the top-left corner of the sprite.
            # glVertex2f(-0.5, 0.5) sets the vertex position in the 2D plane.
            glTexCoord2f(0, 1)
            glVertex2f(-0.5, 0.5)

            # End the drawing of the quad
            glEnd()

            # Disable 2D textures after the drawing operation
            glDisable(GL_TEXTURE_2D)

            # Restore the previous transformation matrix, undoing all transformations
            # applied after glPushMatrix().
            glPopMatrix()

