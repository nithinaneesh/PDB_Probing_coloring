#!/usr/bin/env python3

import tempfile
from pymol import cmd
import math



def align_all( subset = [] ):
  """
  Superimpose all open models onto the first one.
  This may not work well with selections.

  This function is probably taken from https://daslab.stanford.edu/site_data/docs_pymol_rhiju.pdf
  """
  print("""This returns a list with 7 items:

    RMSD after refinement
    Number of aligned atoms after refinement
    Number of refinement cycles
    RMSD before refinement
    Number of aligned atoms before refinement
    Raw alignment score
    Number of residues aligned """)

  AllObj=cmd.get_names("all")
  for x in AllObj[1:]:
    #print(AllObj[0],x)
    subset_tag = ''
    if isinstance( subset, int ):
      subset_tag = ' and resi %d' % subset
    elif isinstance( subset, list ) and len( subset ) > 0:
      subset_tag = ' and resi %d' % (subset[0])
      for m in range( 1,len(subset)): subset_tag += '+%d' % subset[m]
    elif isinstance( subset, str ) and len( subset ) > 0:
      subset_tag = ' and %s' % subset
    values = cmd.align(x+subset_tag,AllObj[0]+subset_tag)
    print(AllObj[0], x, ' '.join([str(v) for v in values]), '-- RMSD', values[3], ' of ', values[6], 'residues')
    cmd.zoom()

def corona():

    cmd.hide("sticks", "all")
    cmd.hide("lines", "all")
    cmd.show("cartoon", "all")
    cmd.set("cartoon_ring_mode", 3)
    cmd.set("cartoon_ring_finder", 2)
    cmd.set("cartoon_ladder_mode", 2)
    cmd.set("cartoon_ring_transparency", 0.30)
    #cmd.spectrum('b', 'white_paleyellow_yellow_red_brown_grey', minimum=-0.25, maximum=1.25, byres=1)
    cmd.spectrum('b', 'white_yellow_red_brown', minimum=0, maximum=100, byres=1)


def shape():

    cmd.hide("sticks", "all")
    cmd.hide("lines", "all")
    cmd.show("cartoon", "all")
    cmd.set("cartoon_ring_mode", 3)
    cmd.set("cartoon_ring_finder", 2)
    cmd.set("cartoon_ladder_mode", 2)
    cmd.set("cartoon_ring_transparency", 0.30)
    cmd.spectrum('b', 'white_paleyellow_yellow_red_brown_grey', minimum=-0.25, maximum=1.25, byres=1)
    #cmd.spectrum('b', 'white_paleyellow_yellow_red_brown_grey', minimum=-250, maximum=1250, byres=1)


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
    print('aa')
    
    cmd.extend('shape', shape)
    cmd.extend('dms', dms)
    cmd.extend('cmct', cmct)
    cmd.extend('aa', align_all)
    cmd.extend('gocoronago', corona)


    # set dash lines
    cmd.set('dash_color', 'red')
    cmd.set('dash_width', 4)
