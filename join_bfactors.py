#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import argparse
from argparse import RawTextHelpFormatter
from rna_tools_lib import RNAStructure
import sys

def argument_parser():

    parser = argparse.ArgumentParser(description=__doc__, 
                        prog='probing_bfactor_pdb.py', formatter_class=RawTextHelpFormatter)
    parser.add_argument("-i1", "--input_pdb", dest="pdb_in1",   
                        help="Input PDB file.")
    parser.add_argument("-i2", "--input_pdb2", dest="pdb_in2",   
                        help="Input PDB file.")
    '''
    parser.add_argument("-r", "--reactivtity_file", required=True, dest="react_in",
                        help="File with reactivity. [copied from sheet, or ractivity format]")
    parser.add_argument("-o", "--output_pdb", required=False, dest="pdb_out", default='',
                        help="Name of output PDB file.")
    parser.add_argument("-c", "--color_by", required=False, dest="color", default='all', 
                        choices=['all', 'base', 'back', 'sugar','basesug', 'backsug'],
                        help="Which part of RNA will have raectivities set as b factor.")
    '''

    args = parser.parse_args()

    in_pdb1 = args.pdb_in1
    in_pdb2 = args.pdb_in2
    #out_pdb = args.pdb_out
    #reactivity = args.react_in
    #color_by = args.color

    return in_pdb1, in_pdb2 #, reactivity, color_by, sequence_in


def merge_two_pdbs():
    
    pdb_out_list = []

    for i in range(0,len(pdb_in_list1)):
        
        if pdb_in_list1[i][13:16] in color1:
            pdb_out_list.append(pdb_in_list1[i])
        else:
            pdb_out_list.append(pdb_in_list2[i])
    write_output(pdb_out_list)
    
def write_output(pdb_out_list):


#    if out_pdb == '':
#        outfile_name = in_pdb.replace('.pdb','') + '_' + color_by + '.pdb'
#    else:
#        outfile_name = out_pdb

    out= open('out.pdb', "w")
    for i in pdb_out_list:
        out.write(i)
    out.close()
      

def check_color():


    backbone  = ["P  ", "OP1", "OP2", "O3'", "O5'", "O3*", "O5*", "C3'", 
                "C4'", "C5'", "C3*", "C4*", "C5*"]
    base = ["N9 ", "C8 ", "N7 ", "C5 ", "C4 ", "N3 ", "O2 ", "N2 ", "N1 ",
                 "C6 ", "O6 ", "C2 ", "N6 ", "O4 ", "N4 "]
    sugar = ["C3'", "C4'", "C5'", "C3*", "C4*", "C5*", "C1'", "C1*", "C2'",
                 "C2*", "O2'", "O2*", "O4'","O4*"]

    color_by1 = backbone + sugar
    color_by2 = base
    return color_by1, color_by2
    


def read_pdb(in_pdb):
    pdb_list = []
    with open(in_pdb) as f:
        for line in f:
            if (line[:6] == "ATOM  " and line[16] != "B" and line[16] != "G") or \
                (line[:6] == "HETATM" and line[17:20] == "GTP" and \
                line[15] != "B" and line[15] != "G" and line[14] != "B" and \
                line[14] != "G" and line[16] != "B" and line[16] != "G"):
                pdb_list.append(line)
            elif line[:6] == "TER   ":
                break
    return pdb_list


if __name__ == '__main__':


    in_pdb1, in_pdb2 = argument_parser()
    
    pdb_in_list1 = read_pdb(in_pdb1)
    pdb_in_list2 = read_pdb(in_pdb2)
    color1, color2 = check_color()
    
    merge_two_pdbs()





