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
    parser.add_argument("-c", "--color_by", required=False, dest="color", default='all', choices=['all', 'base',
                        'back', 'sugar','basesug', 'backsug'],
                        help="Which part of RNA will have raectivities as b factor")


    args = parser.parse_args()

    in_pdb = args.pdb_in
    out_pdb = args.pdb_out
    reactivity = args.react_in
    color_by = args.color
    return in_pdb, out_pdb, reactivity, color_by


def change_bfactor():
    
    #print(pdb_in_list)
    print(reactivities_df)
    print(reactivities_df.shape[0])

    backbone  = ["P  ", "OP1", "OP2", "O3'", "O5'", "O3*", "O5*", "C3'", "C4'", "C5'", "C3*", "C4*", "C5*"]
    base = ["N9 ", "C8 ", "N7 ", "C5 ", "C4 ", "N3 ", "O2 ", "N2 ", "N1 ", "C6 ", "O6 ", "C2 ", "N6 ", "O4 ", "N4 "]
    sugar = ["C3'", "C4'", "C5'", "C3*", "C4*", "C5*", "C1'", "C1*", "C2'", "C2*", "O2'", "O2*", "O4'","O4*"]

    if color_by == 'all':
        color = backbone + base + sugar
    elif color_by == 'base':
        color = base
    elif color_by == 'back':
        color = backbone
    elif color_by == 'sugar':
        color = sugar
    elif color_by == 'basesug':
        color = base + sugar
    elif color_by == 'backsug':
        color = backbone + sugar
        
    pdb_out_list = pdb_in_list.copy()
    
    
    for i in range(0, reactivities_df.shape[0]):  # go through the reactivity df
        for k in range(0, len(pdb_in_list)):  # go through the whole pdb
            if int(pdb_in_list[k][22:26]) == i:  # check residue number and get pdb rows of sthis residue 
                line = list(pdb_out_list[k])
                if pdb_in_list[k][13:16] in color:  # check if the atom is in color list, and change bfactor if yes 
                    re = list(str("%.2f" % reactivities_df.iloc[i]["react"]))
                    put = [" ", " "]+re
                    line[60:66] = put
                    line = ''.join(line)
                else:  # color other atoms to grey (b factor 1.25)
                    put = [" ", " ", "1", ".", "2", "5"]
                    line[60:66] = put
                    line = ''.join(line)
                pdb_out_list[k] = line
       

    print(pdb_out_list)
    out= open("out.pdb", "w")
    for i in pdb_out_list:
        out.write(i)
    out.close()



def read_pdb():

    print('kupka')
    pdb_list = []
    with open(in_pdb) as f:
        for line in f:
            if (line[:6] == "ATOM  " and line[16] != "B" and line[16] != "G") or (line[:6] == "HETATM" and line[17:20] == "GTP" \
                and line[15] != "B" and line[15] != "G" and line[14] != "B" and line[14] != "G" \
                and line[16] != "B" and line[16] != "G"):
                print('atom')
                pdb_list.append(line)
    
    '''
    out= open("out.pdb", "w")
    for i in pdb_list:
        out.write(i)
    out.close()
    '''
    #print(pdb_list)
    return pdb_list    

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

def read_react():
    
    
    with open(reactivity) as f:
        count = sum(1 for _ in f)
#    print(count)
    
    if count >2:
        react_df = pd.read_csv(reactivity, sep=' ',index_col=False,header=None, names=["num","react"])
        react_df.set_index("num", inplace=True)
        print('from columns')
    else:
        react_df = pd.read_csv(reactivity, sep='\t',index_col=False,header=None)
        react_df = react_df.transpose()[0]
        react_df = pd.DataFrame(react_df)
        react_df.index.name="num"
        react_df.index += 1
        react_df.columns = ["react"]
        print('from sheet')    
#    print(react_df, type(react_df))

    return react_df


if __name__ == '__main__':

    in_pdb, out_pdb, reactivity, color_by = argument_parser()

    pdb_in_list = read_pdb()
    reactivities_df = read_react()
    
    change_bfactor()    


