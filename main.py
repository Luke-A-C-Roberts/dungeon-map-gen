from classes      import *
from arraytoimage import *
from tile_sets    import *


#creation of an empty tile grid and map
tg = TileGrid(size = [32,32], tile_size = [8,8])
gen = TileGridGenerator()

#generation using the master tile set
tg = gen.gen_tile_grid (
    tile_grid = tg,
    tile_set  = master_tile_set,
    gen_type  = "wave_function_collapse"
)

#creation of grid of characters from the tiles and creation of image
cg = tg.create_chargrid()

chargrid_to_image(cg, "/home/luke/Pictures/map.png")