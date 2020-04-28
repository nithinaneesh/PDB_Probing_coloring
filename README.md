# PDB_Probing_coloring

Python script for chaniging b_factor values in a PDB file to values representing RNA chemical probing reactivies.
The file with modified b_factor can be used to visualize the reactivities in structure visualization tool such as PyMOL or Chimera.

## Usage:

`./probing_bfactor_pdb.py -i test.pdb -r react_sheet.txt -c back`

**Options:**

- -i - Input file

- -o - output file name, if not set, the new file will be generated with addition of which part of RNA was modified (e.g., base, sugar)

- -r - file with probing reactivities

- -c - which part of RNA to change b_factor: {all,base,back,sugar,basesug,backsug}

**how to color newly obtained pdb in PyMOL**

You can either use my super PyMOL script, provided in this repo or type in PyMOL command line: `spectrum b, white_paleyellow_yellow_red_brown_grey, minimum=-0.25, maximum=1.25, byres=1`.

**Inputs**

PDB file - PDB file with RNA structure, must have one structure (chain), residue numbering from one (1)

Reactivity file - file with reactivities, script accepts two formats: Ractivity format as in RNAfold or RNAProbe; single-line txt file with reactivities copied from a google sheet (values tab-separated).

Ractivity format:
```
1 0.0
2 0.0
3 0.0
4 0.01
5 0.0
6 0.7
7 0.05
...
```

Single-line format:
```
0.87	1	1	0.56	0.21	0.2	0.08	0.17	0.1	0.17...
```


### PyMOL plugin

The repository has a nice accompaniyng PyMOL plugin `Pymol_plugin_Probing_coloring.py`.

**Installaition of the plugin:**

1. Open PyMOL
2. Click `Plugin` button on top of the window
3. Click `Plugin Manager` from the list
4. Go to `Install New Plugin` tab
5. Click `Choose file...` button
6. Select the `Pymol_plugin_Probing_coloring.py` plugin
7. Click `OK`
8. Your plugin is installed! Very nice!

**Usage:**

In PyMOL command line type one of the three: `shape`, `dms`, `cmct`; and enjoy very nice cartoon representation colored by the probing scheme.

### Prerequisites

#### Python 3

```
$ sudo apt update
$ sudo apt upgrade
$ sudo apt install software-properties-common
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt install python3.7 -y
$ sudo apt install build-essential libssl-dev libffi-dev python3-dev
```

#### Python package isnatller

```
$ sudo apt install -y python3-pip
```

#### Python modules

1. Pandas:

```
pip3 install pandas
```

2. Argument Parser:

```
pip3 install argparse
```

#### Make the script executable

`chmod a+x probing_bfactor_pdb.py`
