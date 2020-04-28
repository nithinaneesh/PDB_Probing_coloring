#!/usr/bin/env python3

import tempfile
from pymol import cmd
import math


def shape():

    cmd.hide("sticks", "all")
    cmd.hide("lines", "all")
    cmd.show("cartoon", "all")
    cmd.set("cartoon_ring_mode", 3)
    cmd.set("cartoon_ring_finder", 2)
    cmd.set("cartoon_ladder_mode", 2)
    cmd.set("cartoon_ring_transparency", 0.30)
    cmd.spectrum('b', 'white_paleyellow_yellow_red_brown_grey', minimum=-0.25, maximum=1.25, byres=1)


def dms():

    cmd.hide("sticks", "all")
    cmd.hide("lines", "all")
    cmd.show("cartoon", "all")
    cmd.set("cartoon_ring_mode", 3)
    cmd.set("cartoon_ring_finder", 2)
    cmd.set("cartoon_ladder_mode", 2)
    cmd.set("cartoon_ring_transparency", 0.30)
    cmd.spectrum('b', 'white_yellow_green_forest_grey', minimum=-0.25, maximum=1.25, byres=1)


def cmct():

    cmd.hide("sticks", "all")
    cmd.hide("lines", "all")
    cmd.show("cartoon", "all")
    cmd.set("cartoon_ring_mode", 3)
    cmd.set("cartoon_ring_finder", 2)
    cmd.set("cartoon_ladder_mode", 2)
    cmd.set("cartoon_ring_transparency", 0.30)
    cmd.spectrum('b', 'white_lightpink_tv_red_firebrick_grey', minimum=-0.25, maximum=1.25, byres=1)


    
try:
    from pymol import cmd
except ImportError:
    print("PyMOL Python lib is missing")
else:
    print('   RNA Probing Coloring  ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Quickref: ')
    print('shape')
    print('dms')
    print('cmct')

    cmd.extend('shape', shape)
    cmd.extend('dms', dms)
    cmd.extend('cmct', cmct)


    # set dash lines
    cmd.set('dash_color', 'red')
    cmd.set('dash_width', 4)
