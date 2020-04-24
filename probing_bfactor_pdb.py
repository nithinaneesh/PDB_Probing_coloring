#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
import sys
import argparse
import os
from argparse import RawTextHelpFormatter


def argument_parser():

    parser = argparse.ArgumentParser(description=__doc__, prog='probing_bfactor_pdb.py', formatter_class=RawTextHelpFormatter)
    parser.add_argument("-i", "--input_pdb", dest="pdb_in",   
                        help="Input PDB file")
    parser.add_argument("-r", "--reactivtity_file", required=True, dest="react_in",
                        help="File with reactivity")
    parser.add_argument("-o", "--output_pdb", required=False, dest="pdb_out",
                        help="Name of output PDB file.")
    parser.add_argument("-c", "--color", required=False, dest="color", default='default', choices=['yellow', 'pink',
                        'spring', 'rainbow', 'gyr', 'grey', 'blue', 'red', 'green', 'default'],
                        help="Color of output images")


    args = parser.parse_args()

    in_pdb = args.pdb_in
    out_pdb = args.pdb_out
    reactivity = args.react_in
    return in_pdb, out_pdb, reactivity


def read_pdb():

    print('kupka')


'''


ATOM
Record Format

COLUMNS        DATA  TYPE    FIELD        DEFINITION
-------------------------------------------------------------------------------------
 1 -  6        Record name   "ATOM  "
 7 - 11        Integer       serial       Atom  serial number.
13 - 16        Atom          name         Atom name.
17             Character     altLoc       Alternate location indicator.
18 - 20        Residue name  resName      Residue name.
22             Character     chainID      Chain identifier.
23 - 26        Integer       resSeq       Residue sequence number.
27             AChar         iCode        Code for insertion of residues.
31 - 38        Real(8.3)     x            Orthogonal coordinates for X in Angstroms.
39 - 46        Real(8.3)     y            Orthogonal coordinates for Y in Angstroms.
47 - 54        Real(8.3)     z            Orthogonal coordinates for Z in Angstroms.
55 - 60        Real(6.2)     occupancy    Occupancy.
61 - 66        Real(6.2)     tempFactor   Temperature  factor.
77 - 78        LString(2)    element      Element symbol, right-justified.
79 - 80        LString(2)    charge       Charge  on the atom.

'''





if __name__ == '__main__':

    in_pdb, out_pdb, reactivity = argument_parser()

    read_pdb()


