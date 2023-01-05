from functions import *
from random import choice


#contain a 2d array of str used for generation of maps
class CharGrid:
    def __init__(
        self,
        grid : list[str]
    ) -> None:
        self.height = len(grid)
        self.width  = len(grid[0])
        self.grid   = grid


#tile contains a 2d array of str used for tile generation as well as the possible tiles it can neighbour
class Tile():
    def __init__ (
        self,
        size            : list[int]       = [8,8],
        name            : str             = "",
        char_grid       : list[list[str]] = [],
        neighbour_tiles : list[list[str]] = [],
    ) -> None:
        self.width     = size[0]
        self.height    = size[1]
        self.name      = name
        self.char_grid = char_grid

        if len(neighbour_tiles) <= 0: return

        self.possible_up_tiles    = neighbour_tiles[0]
        self.possible_down_tiles  = neighbour_tiles[1]
        self.possible_left_tiles  = neighbour_tiles[2]
        self.possible_right_tiles = neighbour_tiles[3]

    
    def __str__(self) -> str:
        return self.name


#used to contain and a 2d array of tiles
class TileGrid:
    def __init__(
        self,
        size      : list[int] = [8, 8],
        tile_size : list[int] = [8, 8],
    ) -> None:
        self.width       = size[0]
        self.height      = size[1]
        self.tile_width  = tile_size[0]
        self.tile_height = tile_size[1]
        self.char_width  = self.width  * self.tile_width
        self.char_height = self.height * self.tile_height
        self.tile_grid   = []

        for j in range(size[1]):
            temp_row = []
            for i in range(size[0]):
                temp_row += [Tile()]
            self.tile_grid += [temp_row]


    def __len__(self):
        return self.width * self.height


    def set_tile (
        self,
        tile  : Tile,
        coord : list[int]
    ) -> None:
        self.tile_grid[coord[0]][coord[1]] = tile


    def clear_tile (
        self,
        coord : list[int]
    ) -> None:
        self.tile_grid[coord[0]][coord[1]] = Tile()


    #creates a character grid from all the tiles
    def create_chargrid(self) -> CharGrid:
        grid = []
        for y in range(self.char_height):
            temprow = []
            for x in range(self.char_width):
                #locates the tile based on the x and y by floordividing and locates the character by calculating the mod
                tile_x      = x // self.tile_width
                tile_y      = y // self.tile_height
                tile_char_x = x % self.tile_width
                tile_char_y = y % self.tile_height
                temprow     += [self.tile_grid[tile_x][tile_y].char_grid[tile_char_x][tile_char_y]]
            grid += [temprow]
            char_grid = CharGrid(grid)
        return char_grid


#a set of unique tiles for use in generation
class TileSet:
    def __init__(self) -> None:
        self.tiles = []
        self.tile_names = []


    def __len__(self) -> int:
        return len(self.tiles)


    def __contains__(self, tile_name : str) -> bool:
        return tile_name in self.tile_names

    
    def __str__(self) -> str:
        return ', '.join([n for n in self.tile_names])


    def add_tile (
        self,
        tile : Tile
    ) -> None:
        self.tiles += [tile]
        self.tile_names += [str(tile)]


    def find_tile_from_name (
        self,
        name : str
    ) -> Tile:
        if not (name in self.tile_names):
            return None
        temp_index = self.tile_names.index(name)
        return self.tiles[temp_index]


    #used to create a subset of the tileset by indexing
    def create_tiles_subset (
        self,
        subset_indexes         : list[int],
        only_subset_neighbours : bool = False
    ) -> 'TileSet':

        new_tile_set = TileSet()
        for i in subset_indexes:
            new_tile_set.add_tile(self.tiles[i])
            

        #if specified False the new subset of tiles will have the same neighbour specifications as the superset it came from
        if not only_subset_neighbours:
            return new_tile_set

        #otherwise tiles in common between the tile subset and the neighber tiles of each tile are found
        remaining_tile_names = []
        for t in new_tile_set.tiles:
            remaining_tile_names += [str(t)]

        #edge "tile" names are added because they are not in the subset of tile names, since they aren't real tiles
        for t in new_tile_set.tiles:
            t.possible_up_tiles    = list_intersection(t.possible_up_tiles,    remaining_tile_names + ["edgeU", "edgeUL", "edgeUR"])
            t.possible_down_tiles  = list_intersection(t.possible_down_tiles,  remaining_tile_names + ["edgeD", "edgeDL", "edgeDR"])
            t.possible_left_tiles  = list_intersection(t.possible_left_tiles,  remaining_tile_names + ["edgeL"])
            t.possible_right_tiles = list_intersection(t.possible_right_tiles, remaining_tile_names + ["edgeR"])

        return new_tile_set


#used to keep track of which tiles have been visited by coordinate
class CoordStack:
    def __init__(self) -> None:
        self.__stack : list[tuple[int]] = []


    def __contains__(self, coord : tuple[int]) -> bool:
        return coord in self.__stack


    def __str__(self) -> str:
        return ', '.join([str(i) for i in self.__stack])


    def __len__(self) -> int:
        return len(self.__stack)


    def push(self, coord : tuple[int]) -> None:
        self.__stack += [coord]

    
    def pop(self) -> tuple[int]:
        temp_coord = self.__stack[-1]
        self.__stack = self.__stack[:-1]
        return temp_coord


    def peak(self) -> tuple[int]:
        return self.__stack[-1]


    def return_stack(self) -> list[tuple[int]]:
        return self.__stack


#class used to generate a tile grid
class TileGridGenerator:
    def gen_tile_grid (
        self,
        tile_grid : TileGrid,
        tile_set  : TileSet,
        gen_type  : str
    ) -> TileGrid:
        if gen_type == "random":
            self.__random_tiles(tile_grid, tile_set)
        elif gen_type == "wave_function_collapse":
            self.__wave_function_collapse_tiles(tile_grid, tile_set)
        return tile_grid

    
    def __random_tiles (
        self,
        tile_grid : TileGrid,
        tile_set  : TileSet,
    ) -> TileGrid:
        for j in range(tile_grid.height):
                for i in range(tile_grid.width):
                    tile_grid.set_tile(choice(tile_set.tiles), [i,j])
        return tile_grid


    def __wave_function_collapse_tiles (
        self,
        tile_grid : TileGrid,
        tile_set  : TileSet,
    ) -> TileGrid:

        def __potenial_tile_name_init (
            temp_tile_options: list,
            temp_width: int,
            temp_height: int
        ) -> list[str]:
            #initializes all the potential tile names in a grid (per cell)
            temp_potential_tile_names = []
            for j in range(temp_height):
                temp_row = []
                for i in range(temp_width):
                    temp_row += [temp_tile_options]
                temp_potential_tile_names += [temp_row]
            return temp_potential_tile_names


        def __find_entropies (
            temp_potential_tiles : list,
            temp_width           : int,
            temp_height          : int
        ) -> list[int]:
            entropies = temp_potential_tiles
            for j in range(temp_height):
                for i in range(temp_width):
                    entropies[i][j] = len(entropies[i][j])
            return entropies


        def __find_entropy_coords (
            temp_entropy   : int,
            temp_entropies : list[int],
            temp_width     : int,
            temp_height    : int
        ) -> list[tuple[int]]:

            entropy_coords = []

            for j in range(temp_height):
                for i in range(temp_width):
                    if temp_entropies[i][j] == temp_entropy:
                        entropy_coords += [(i,j)]

            return entropy_coords

        new_tile_grid = tile_grid
        all_tile_options = tile_set.tile_names
        potential_tile_names = []
        width  = new_tile_grid.width
        height = new_tile_grid.height

        #initializes all the potential tile names in a grid (per cell)
        potential_tile_names = __potenial_tile_name_init(all_tile_options, width, height)

        #initializes coordinate stack
        used_coord_stack = CoordStack()


        while len(used_coord_stack) < len(tile_grid):

            entropies_per_tile = []
            for j, r in enumerate(potential_tile_names):
                temp_list = []
                for i, t in enumerate(r):
                    temp_list += [potential_tile_names[i][j].copy()]
                entropies_per_tile += [temp_list]

            entropies_per_tile = __find_entropies(entropies_per_tile, width, height)
            entrpoy_list = list(set(sum(entropies_per_tile, [])))
            entrpoy_list.sort()
            entropy_pointer = 0

            if not min(entrpoy_list) == 0:
                #selects an unused tile from the list of coodinates corresponding a specific entropy
                #if the coordinates are already in the coordstack it removes it as an option and tries to find a new tile
                #if there are no tiles unused corresponding to the entropy it tries the entropy above that
                do_coordinate_search = True
                while do_coordinate_search and entropy_pointer <= len(entrpoy_list) - 1:
                    coords_list = __find_entropy_coords(entrpoy_list[entropy_pointer], entropies_per_tile, width, height)
                    while do_coordinate_search and len(coords_list) > 0:
                        random_coords = choice(coords_list)
                        if not random_coords in used_coord_stack:
                            do_coordinate_search = False
                        else:
                            coords_list.remove(random_coords)
                    entropy_pointer += 1
                
                used_coord_stack.push(random_coords)
                print(f"placed: {random_coords}, ", end="")
                random_tile_name = choice(potential_tile_names[random_coords[0]][random_coords[1]])
                new_tile = tile_set.find_tile_from_name(random_tile_name)

                new_possible_up_tiles    = new_tile.possible_up_tiles
                new_possible_down_tiles  = new_tile.possible_down_tiles
                new_possible_left_tiles  = new_tile.possible_left_tiles
                new_possible_right_tiles = new_tile.possible_right_tiles

                if random_coords[0] > 0:
                    potential_tile_names[random_coords[0] - 1][random_coords[1]] = \
                        list_intersection(potential_tile_names[random_coords[0] - 1][random_coords[1]], new_possible_up_tiles)
                if random_coords[0] < height - 2:
                    potential_tile_names[random_coords[0] + 1][random_coords[1]] = \
                        list_intersection(potential_tile_names[random_coords[0] + 1][random_coords[1]], new_possible_down_tiles)
                if random_coords[1] > 0:
                    potential_tile_names[random_coords[0]][random_coords[1] - 1] = \
                        list_intersection(potential_tile_names[random_coords[0]][random_coords[1] - 1], new_possible_left_tiles)
                if random_coords[1] < width - 2:
                    potential_tile_names[random_coords[0]][random_coords[1] + 1] = \
                        list_intersection(potential_tile_names[random_coords[0]][random_coords[1] + 1], new_possible_right_tiles)

                new_tile_grid.set_tile(new_tile, list(random_coords))
                       
            else:
                #removing tile 
                coord_for_removal = used_coord_stack.pop()
                print(f"backtracked: {coord_for_removal}, ", end="")
                new_tile_grid.clear_tile(list(coord_for_removal))

                #reseting possible neighbour tiles
                used_coords = used_coord_stack.return_stack()
                potential_tile_names = __potenial_tile_name_init(all_tile_options, width, height)

                for coord in used_coords:
                    tile_for_reset = new_tile_grid.tile_grid[coord[0]][coord[1]]
                    up_tiles    = tile_for_reset.possible_up_tiles
                    down_tiles  = tile_for_reset.possible_down_tiles
                    left_tiles  = tile_for_reset.possible_left_tiles
                    right_tiles = tile_for_reset.possible_right_tiles

                    if coord[0] > 0:
                        potential_tile_names[coord[0] - 1][coord[1]] = \
                            list_intersection(potential_tile_names[coord[0] - 1][coord[1]], up_tiles)
                    if coord[0] < height - 2:
                        potential_tile_names[coord[0] + 1][coord[1]] = \
                            list_intersection(potential_tile_names[coord[0] + 1][coord[1]], down_tiles)
                    if coord[1] > 0:
                        potential_tile_names[coord[0]][coord[1] - 1] = \
                            list_intersection(potential_tile_names[coord[0]][coord[1] - 1], left_tiles)
                    if coord[1] < width - 2:
                        potential_tile_names[coord[0]][coord[1] + 1] = \
                            list_intersection(potential_tile_names[coord[0]][coord[1] + 1], right_tiles)            
        return(new_tile_grid)