#!/bin/python3

# PARAMETERS
forcefield = "charmm36-mar2019"
watermodel = "tip3p"
timesteps  = 50000

import os, fnmatch

def inferFullName(match):
    return fnmatch.filter(os.listdir('.'), match)[0]

# Get name of xxx_MD.pdb
name = inferFullName("*_MD.pdb")

# Create buffer directory
if not os.path.isdir('buffer'):
    os.mkdir('buffer')

os.system("gmx editconf -f {0} -o buffer/solvent.pdb -n index.ndx << EOF\nWater_and_ions\nEOF".format(name))

os.chdir('buffer')

# COUNT NUMBER OF POSITIVE AND NEGATIVE IONS IN SOLVENT
countNa = 0
countCl = 0
for line in open("solvent.pdb").read().splitlines():
    if " NA " in line:
        countNa += 1
    if " CL " in line:
        countCl += 1

# REMOVE IONS
os.system("sed -i '/ NA /d' solvent.pdb")
os.system("sed -i '/ CL /d' solvent.pdb")

# PREPARE THE SOLVENT SIMULATION
os.system("gmx pdb2gmx  -f solvent.pdb -o solvent.pdb -ff {0} -water {1}".format(forcefield, watermodel))
os.system("gmx solvate -cp solvent.pdb -o solvent.pdb -p topol.top")

os.system("gmx grompp -f ../IONS.mdp -c solvent.pdb -p topol.top -o IONS.tpr")
os.system("gmx genion -s IONS.tpr -o solvent.pdb -p topol.top -pname NA -nname CL -np {0} -nn {1} << EOF\nSOL\nEOF".format(countNa, countCl))

# energy minimization
os.system("gmx grompp -f ../EM.mdp -c solvent.pdb -p topol.top -o solvent_EM.tpr -maxwarn 1")
os.system("gmx mdrun -v -s solvent_EM.tpr -c solvent.pdb")

# prepare mdrun
os.system("gmx grompp -f ../MD.mdp -c solvent.pdb -p topol.top -o solvent.tpr -maxwarn 2")
os.system("gmx convert-tpr -s solvent.tpr -nsteps {0} -o solvent.tpr".format(timesteps))

# do mdrun
os.system("gmx mdrun -v -s solvent.tpr -x solvent.xtc")
