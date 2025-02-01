from core.object_2D import Object_2D

class Tile(Object_2D):
    def __init__(self, object_list: list = [], *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.object_list = object_list

    def draw(self):
        super().draw()

        for obj in self.object_list:
            obj: Object_2D
            obj.draw(scaling=self.scaling, rotation=self.rotation, translation=self.translation)