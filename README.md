# PDB_Probing_coloring


## PyMOL plugin

The repository has a nice accompaniyng PyMOL plugin `Pymol_plugin_Probing_coloring.py`.

Installaition of the plugin:

1. Open PyMOL
2. Click `Plugin` button on top of the window
3. Click `Plugin Manager` from the list
4. Go to `Install New Plugin` tab
5. Click `Choose file...` button
6. Select the `Pymol_plugin_Probing_coloring.py` plugin
7. Click `OK`
8. Your plugin is installed! Very nice!

Usage:

In PyMOL command line type one of the three: `shape`, `dms`, `cmct`; and enjoy very nice cartoon representation colored by the probing scheme.

## Prerequisites

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
