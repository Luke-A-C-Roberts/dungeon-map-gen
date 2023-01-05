from PIL.Image import new, Image
from classes import *
from random  import randint
from typing  import Type


def chargrid_to_image (
        chargrid : Type[CharGrid],
        path     : str
    ) -> None:

    img = new (
        mode  = 'RGB',
        size  = [chargrid.width, chargrid.height],
        color = (0,0,0)
    )
    px = img.load()

    for j, r in enumerate(chargrid.grid):
        for i, c in enumerate(r):
            if c == " ":
                col = (0,0,0)
            elif c == "#":
                rand = randint(200,256)
                green = randint(0,20)
                col = (rand,rand + green,rand)
            elif c == "x":
                rand = randint(85,115)
                green = randint(0,20)
                col = (rand,rand + green,rand)
            px[i, j] = col

    img.save(path)