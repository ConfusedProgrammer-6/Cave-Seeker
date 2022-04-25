from Enviroment.Tile import Tile


class Static_Tiles(Tile):
    def __init__(self,size,x,y,surface):
        super().__init__(size,x,y)
        self.image = surface

