#!/bin/python3

import os
import fnmatch

import loaddata as load

def inferFullName(match):
    return fnmatch.filter(os.listdir('.'), match)[0]

protein = inferFullName("*_MD.pdb")

if not os.path.isdir('solvent'):
    os.mkdir('solvent')

os.system("gmx editconf -f {0} -o solvent/solvent.pdb -n index.ndx << EOF\nWater_and_ions\nEOF".format(protein))

os.chdir('solvent')

# COUNT NUMBER OF POSITIVE AND NEGATIVE IONS IN SOLVENT
countNa = 0
countCl = 0

for line in load.StrList('solvent.pdb'):
    if " NA " in line:
        countNa += 1
    if " CL " in line:
        countCl += 1

# REMOVE IONS FROM SOLVENT
os.system("sed -i '/ NA /d' solvent.pdb")
os.system("sed -i '/ CL /d' solvent.pdb")

# PREPARE THE SOLVENT SIM

os.system("gmx pdb2gmx -f solvent.pdb -o solvent.pdb -ff charmm36-mar2019 -water tip3p")
os.system("gmx solvate -cp solvent.pdb -o solvent.pdb -p topol.top")

os.system("gmx grompp -f ../IONS.mdp -c solvent.pdb -p topol.top -o IONS.tpr")
os.system("gmx genion -s IONS.tpr -o solvent.pdb -p topol.top -pname NA -nname CL -np {0} -nn {1} << EOF\nSOL\nEOF".format(countNa, countCl))

# energy minimization
os.system("gmx grompp -f ../EM.mdp -c solvent.pdb -p topol.top -o solvent_EM.tpr -maxwarn 1")
os.system("gmx mdrun -v -s solvent_EM.tpr -c solvent.pdb")

# prepare mdrun
os.system("gmx grompp -f ../MD.mdp -c solvent.pdb -p topol.top -o solvent.tpr -maxwarn 1")
os.system("gmx convert-tpr -s solvent.tpr -nsteps 500000 -o solvent.tpr")

# do mdrun
os.system("gmx ")
