from configparser import LegacyInterpolation
from classes import *
from functions import *

master_tile_grids = [
    [
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
    ],
    [
        [' ',' ','#','x','x','#',' ',' '],
        [' ','#','#','x','x','#','#',' '],
        [' ','#','x','x','x','x','#',' '],
        [' ','#','x','x','x','x','#',' '],
        [' ','#','x','x','x','x','#',' '],
        [' ','#','x','x','x','x','#',' '],
        [' ','#','#','x','x','#','#',' '],
        [' ',' ','#','x','x','#',' ',' '],
    ],
    [
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ','#','#','#','#','#','#',' '],
        ['#','#','x','x','x','x','#','#'],
        ['x','x','x','x','x','x','x','x'],
        ['x','x','x','x','x','x','x','x'],
        ['#','#','x','x','x','x','#','#'],
        [' ','#','#','#','#','#','#',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
    ],
    [
        [' ',' ','#','x','x','#',' ',' '],
        [' ','#','#','x','x','#','#',' '],
        ['#','#','x','x','x','x','#',' '],
        ['x','x','x','x','x','x','#',' '],
        ['x','x','x','x','x','x','#',' '],
        ['#','#','x','x','x','x','#',' '],
        [' ','#','#','#','#','#','#',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
    ],
    [
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ','#','#','#','#','#','#',' '],
        ['#','#','x','x','x','x','#',' '],
        ['x','x','x','x','x','x','#',' '],
        ['x','x','x','x','x','x','#',' '],
        ['#','#','x','x','x','x','#',' '],
        [' ','#','#','x','x','#','#',' '],
        [' ',' ','#','x','x','#',' ',' '],
    ],
    [
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ','#','#','#','#','#','#',' '],
        [' ','#','x','x','x','x','#','#'],
        [' ','#','x','x','x','x','x','x'],
        [' ','#','x','x','x','x','x','x'],
        [' ','#','x','x','x','x','#','#'],
        [' ','#','#','x','x','#','#',' '],
        [' ',' ','#','x','x','#',' ',' '],
    ],
    [
        [' ',' ','#','x','x','#',' ',' '],
        [' ','#','#','x','x','#','#',' '],
        [' ','#','x','x','x','x','#','#'],
        [' ','#','x','x','x','x','x','x'],
        [' ','#','x','x','x','x','x','x'],
        [' ','#','x','x','x','x','#','#'],
        [' ','#','#','#','#','#','#',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
    ],
    [
        [' ',' ','#','x','x','#',' ',' '],
        [' ','#','#','x','x','#','#',' '],
        ['#','#','x','x','x','x','#','#'],
        ['x','x','x','x','x','x','x','x'],
        ['x','x','x','x','x','x','x','x'],
        ['#','#','x','x','x','x','#','#'],
        [' ','#','#','#','#','#','#',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
    ],
    [
        [' ',' ','#','x','x','#',' ',' '],
        [' ','#','#','x','x','#','#',' '],
        ['#','#','x','x','x','x','#',' '],
        ['x','x','x','x','x','x','#',' '],
        ['x','x','x','x','x','x','#',' '],
        ['#','#','x','x','x','x','#',' '],
        [' ','#','#','x','x','#','#',' '],
        [' ',' ','#','x','x','#',' ',' '],
    ],
    [
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ','#','#','#','#','#','#',' '],
        ['#','#','x','x','x','x','#','#'],
        ['x','x','x','x','x','x','x','x'],
        ['x','x','x','x','x','x','x','x'],
        ['#','#','x','x','x','x','#','#'],
        [' ','#','#','x','x','#','#',' '],
        [' ',' ','#','x','x','#',' ',' '],
    ],
    [
        [' ',' ','#','x','x','#',' ',' '],
        [' ','#','#','x','x','#','#',' '],
        [' ','#','x','x','x','x','#','#'],
        [' ','#','x','x','x','x','x','x'],
        [' ','#','x','x','x','x','x','x'],
        [' ','#','x','x','x','x','#','#'],
        [' ','#','#','x','x','#','#',' '],
        [' ',' ','#','x','x','#',' ',' '],
    ],
    [
        [' ',' ','#','x','x','#',' ',' '],
        [' ','#','#','x','x','#','#',' '],
        ['#','#','x','x','x','x','#','#'],
        ['x','x','x','x','x','x','x','x'],
        ['x','x','x','x','x','x','x','x'],
        ['#','#','x','x','x','x','#','#'],
        [' ','#','#','x','x','#','#',' '],
        [' ',' ','#','x','x','#',' ',' '],
    ],
    [
        [' ',' ','#','x','x','#',' ',' '],
        [' ',' ','#','x','x','#',' ',' '],
        [' ',' ','#','x','x','#',' ',' '],
        [' ',' ','#','x','x','#',' ',' '],
        [' ',' ','#','x','x','#',' ',' '],
        [' ',' ','#','x','x','#',' ',' '],
        [' ',' ','#','x','x','#',' ',' '],
        [' ',' ','#','x','x','#',' ',' '],
    ],
    [
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        ['#','#','#','#','#','#','#','#'],
        ['x','x','x','x','x','x','x','x'],
        ['x','x','x','x','x','x','x','x'],
        ['#','#','#','#','#','#','#','#'],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
    ],
    [
        [' ',' ','#','x','x','#',' ',' '],
        [' ',' ','#','x','x','#',' ',' '],
        ['#','#','#','x','x','#',' ',' '],
        ['x','x','x','x','x','#',' ',' '],
        ['x','x','x','x','x','#',' ',' '],
        ['#','#','#','#','#','#',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
    ],
    [
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        ['#','#','#','#','#','#',' ',' '],
        ['x','x','x','x','x','#',' ',' '],
        ['x','x','x','x','x','#',' ',' '],
        ['#','#','#','x','x','#',' ',' '],
        [' ',' ','#','x','x','#',' ',' '],
        [' ',' ','#','x','x','#',' ',' '],
    ],
    [
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ','#','#','#','#','#','#'],
        [' ',' ','#','x','x','x','x','x'],
        [' ',' ','#','x','x','x','x','x'],
        [' ',' ','#','x','x','#','#','#'],
        [' ',' ','#','x','x','#',' ',' '],
        [' ',' ','#','x','x','#',' ',' '],
    ],
    [
        [' ',' ','#','x','x','#',' ',' '],
        [' ',' ','#','x','x','#',' ',' '],
        [' ',' ','#','x','x','#','#','#'],
        [' ',' ','#','x','x','x','x','x'],
        [' ',' ','#','x','x','x','x','x'],
        [' ',' ','#','#','#','#','#','#'],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
    ],
    [
        [' ',' ','#','x','x','#',' ',' '],
        [' ',' ','#','x','x','#',' ',' '],
        ['#','#','#','x','x','#','#','#'],
        ['x','x','x','x','x','x','x','x'],
        ['x','x','x','x','x','x','x','x'],
        ['#','#','#','#','#','#','#','#'],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
    ],
    [
        [' ',' ','#','x','x','#',' ',' '],
        [' ',' ','#','x','x','#',' ',' '],
        ['#','#','#','x','x','#',' ',' '],
        ['x','x','x','x','x','#',' ',' '],
        ['x','x','x','x','x','#',' ',' '],
        ['#','#','#','x','x','#',' ',' '],
        [' ',' ','#','x','x','#',' ',' '],
        [' ',' ','#','x','x','#',' ',' '],
    ],
    [
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        ['#','#','#','#','#','#','#','#'],
        ['x','x','x','x','x','x','x','x'],
        ['x','x','x','x','x','x','x','x'],
        ['#','#','#','x','x','#','#','#'],
        [' ',' ','#','x','x','#',' ',' '],
        [' ',' ','#','x','x','#',' ',' '],
    ],
    [
        [' ',' ','#','x','x','#',' ',' '],
        [' ',' ','#','x','x','#',' ',' '],
        [' ',' ','#','x','x','#','#','#'],
        [' ',' ','#','x','x','x','x','x'],
        [' ',' ','#','x','x','x','x','x'],
        [' ',' ','#','x','x','#','#','#'],
        [' ',' ','#','x','x','#',' ',' '],
        [' ',' ','#','x','x','#',' ',' '],
    ],
    [
        [' ',' ','#','x','x','#',' ',' '],
        [' ',' ','#','x','x','#',' ',' '],
        ['#','#','#','x','x','#','#','#'],
        ['x','x','x','x','x','x','x','x'],
        ['x','x','x','x','x','x','x','x'],
        ['#','#','#','x','x','#','#','#'],
        [' ',' ','#','x','x','#',' ',' '],
        [' ',' ','#','x','x','#',' ',' '],
    ],


    
    
    
    
    [
        [' ',' ','#','x','x','#',' ',' '],
        [' ','#','#','x','x','#','#',' '],
        [' ','#','x','x','x','x','#',' '],
        [' ','#','x','x','x','x','#',' '],
        [' ','#','x','x','x','x','#',' '],
        [' ','#','x','x','x','x','#',' '],
        [' ','#','#','#','#','#','#',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
    ],
    [
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ','#','#','#','#','#','#',' '],
        ['#','#','x','x','x','x','#',' '],
        ['x','x','x','x','x','x','#',' '],
        ['x','x','x','x','x','x','#',' '],
        ['#','#','x','x','x','x','#',' '],
        [' ','#','#','#','#','#','#',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
    ],
    [
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ','#','#','#','#','#','#',' '],
        [' ','#','x','x','x','x','#',' '],
        [' ','#','x','x','x','x','#',' '],
        [' ','#','x','x','x','x','#',' '],
        [' ','#','x','x','x','x','#',' '],
        [' ','#','#','x','x','#','#',' '],
        [' ',' ','#','x','x','#',' ',' '],
    ],
    [
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ','#','#','#','#','#','#',' '],
        [' ','#','x','x','x','x','#','#'],
        [' ','#','x','x','x','x','x','x'],
        [' ','#','x','x','x','x','x','x'],
        [' ','#','x','x','x','x','#','#'],
        [' ','#','#','#','#','#','#',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
    ],
    [
        [' ',' ','#','x','x','#',' ',' '],
        [' ',' ','#','x','x','#',' ',' '],
        [' ',' ','#','x','x','#',' ',' '],
        [' ',' ','#','x','x','#',' ',' '],
        [' ',' ','#','x','x','#',' ',' '],
        [' ',' ','#','#','#','#',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
    ],
    [
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        ['#','#','#','#','#','#',' ',' '],
        ['x','x','x','x','x','#',' ',' '],
        ['x','x','x','x','x','#',' ',' '],
        ['#','#','#','#','#','#',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
    ],
    [
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ','#','#','#','#',' ',' '],
        [' ',' ','#','x','x','#',' ',' '],
        [' ',' ','#','x','x','#',' ',' '],
        [' ',' ','#','x','x','#',' ',' '],
        [' ',' ','#','x','x','#',' ',' '],
        [' ',' ','#','x','x','#',' ',' '],
    ],
    [
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ','#','#','#','#','#','#'],
        [' ',' ','#','x','x','x','x','x'],
        [' ',' ','#','x','x','x','x','x'],
        [' ',' ','#','#','#','#','#','#'],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
    ],
]

master_tile_names = [
    "empty" ,

    "roomUD",
    "roomLR",

    "roomUL",
    "roomDL",
    "roomDR",
    "roomUR",

    "roomULR",
    "roomUDL",
    "roomDLR",
    "roomUDR",

    "roomUDLR",

    "corridoorUD",
    "corridoorLR",

    "corridoorUL",
    "corridoorDL",
    "corridoorDR",
    "corridoorUR",

    "corridoorULR",
    "corridoorUDL",
    "corridoorDLR",
    "corridoorUDR",
    
    "corridoorUDLR",

    "roomU",
    "roomL",
    "roomD",
    "roomR",

    "corridoorU",
    "corridoorL",
    "corridoorD",
    "corridoorR",
]

up_tiles    = selector(master_tile_names, "U", False)
down_tiles  = selector(master_tile_names, "D", False)
left_tiles  = selector(master_tile_names, "L", False)
right_tiles = selector(master_tile_names, "R", False)
not_up_tiles    = selector(master_tile_names, "U", True)
not_down_tiles  = selector(master_tile_names, "D", True)
not_left_tiles  = selector(master_tile_names, "L", True)
not_right_tiles = selector(master_tile_names, "R", True)
print(up_tiles,down_tiles,left_tiles,right_tiles,not_up_tiles,not_down_tiles,not_left_tiles,not_right_tiles)

#order is, Up Down Left Right
master_tile_neighbours = [
    # empty
    [
        not_down_tiles,
        not_up_tiles,
        not_right_tiles,
        not_left_tiles
    ],
    # roomUD
    [
        down_tiles,
        up_tiles,
        not_right_tiles,
        not_left_tiles
    ],
    # roomLR
    [
        not_down_tiles,
        not_up_tiles,
        right_tiles,
        left_tiles
    ],
    # roomUL
    [
        down_tiles,
        not_up_tiles,
        right_tiles,
        not_left_tiles
    ],
    # roomDL
    [
        not_down_tiles,
        up_tiles,
        right_tiles,
        not_left_tiles
    ],
    # roomDR
    [
        not_down_tiles,
        up_tiles,
        not_right_tiles,
        left_tiles
    ],
    # roomUR
    [
        down_tiles,
        not_up_tiles,
        not_right_tiles,
        left_tiles
    ],
    # roomULR
    [
        down_tiles,
        not_up_tiles,
        right_tiles,
        left_tiles,
    ],
    # roomUDL
    [
        down_tiles,
        up_tiles,
        right_tiles,
        not_left_tiles
    ],
    # roomDLR
    [
        not_down_tiles,
        up_tiles,
        right_tiles,
        left_tiles
    ],
    # roomUDR
    [
        down_tiles,
        up_tiles,
        not_right_tiles,
        left_tiles
    ],
    # roomUDLR
    [
        down_tiles,
        up_tiles,
        right_tiles,
        left_tiles
    ],
    # corridoorUD
    [
        down_tiles,
        up_tiles,
        not_right_tiles,
        not_left_tiles
    ],
    # corridoorLR
    [
        not_down_tiles,
        not_up_tiles,
        right_tiles,
        left_tiles
    ],
    # corridoorUL
    [
        down_tiles,
        not_up_tiles,
        right_tiles,
        not_left_tiles
    ],
    # corridoorDL
    [
        not_down_tiles,
        up_tiles,
        right_tiles,
        not_left_tiles
    ],
    # corridoorDR
    [
        not_down_tiles,
        up_tiles,
        not_right_tiles,
        left_tiles
    ],
    # corridoorUR
    [
        down_tiles,
        not_up_tiles,
        not_right_tiles,
        left_tiles
    ],
    # corridoorULR
    [
        down_tiles,
        not_up_tiles,
        right_tiles,
        left_tiles,
    ],
    # corridoorUDL
    [
        down_tiles,
        up_tiles,
        right_tiles,
        not_left_tiles
    ],
    # corridoorDLR
    [
        not_down_tiles,
        up_tiles,
        right_tiles,
        left_tiles
    ],
    # corridoorUDR
    [
        down_tiles,
        up_tiles,
        not_right_tiles,
        left_tiles
    ],    
    # corridoorUDLR
    [
        down_tiles,
        up_tiles,
        right_tiles,
        left_tiles
    ],
    #roomU
    [
        down_tiles,
        not_up_tiles,
        not_right_tiles,
        not_left_tiles
    ],
    #roomL
    [
        not_down_tiles,
        not_up_tiles,
        right_tiles,
        not_left_tiles
    ],
    #roomD
    [
        not_down_tiles,
        up_tiles,
        not_right_tiles,
        not_left_tiles
    ],
    #roomR
    [
        not_down_tiles,
        not_up_tiles,
        not_right_tiles,
        left_tiles
    ],
    #corridoorU
    [
        down_tiles,
        not_up_tiles,
        not_right_tiles,
        not_left_tiles
    ],
    #corridoorL
    [
        not_down_tiles,
        not_up_tiles,
        right_tiles,
        not_left_tiles
    ],
    #corridoorD
    [
        not_down_tiles,
        up_tiles,
        not_right_tiles,
        not_left_tiles
    ],
    #corridoorR
    [
        not_down_tiles,
        not_up_tiles,
        not_right_tiles,
        left_tiles
    ],
]

master_tile_set = TileSet()

for i, (temp_grid, temp_name, temp_neighbours) in enumerate(zip(master_tile_grids, master_tile_names, master_tile_neighbours)):
    temp_tile = Tile (
        size            = [8,8],
        name            = temp_name,
        char_grid       = temp_grid,
        neighbour_tiles = temp_neighbours
    )
    master_tile_set.add_tile(temp_tile)

# room_tile_set = master_tile_set.create_tiles_subset(
#     subset_indexes = quick_range(1, 12),
#     only_subset_neighbours = True
# )

# print(room_tile_set.tiles[0].possible_up_tiles)
# print(room_tile_set.tiles[0].possible_down_tiles)
# print(room_tile_set.tiles[0].possible_left_tiles)
# print(room_tile_set.tiles[0].possible_right_tiles)