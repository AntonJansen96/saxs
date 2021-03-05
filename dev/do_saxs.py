#!/bin/python3

import os, fnmatch

# PARAMETERS
envelopeLen = 0.7 # (nm)


def inferFullName(match):
    return fnmatch.filter(os.listdir('.'), match)[0]

protName = inferFullName("*_MD.pdb")

# CREATE STRUCTURE+TRAJECTORY WITH JUST PROTEIN
os.chdir("saxs")
os.system("touch empty.mdp")
os.system("gmx grompp -f empty.mdp -c ../{0} -p ../topol.top -n ../index.ndx -o dummy.tpr".format(protName))

os.system("gmx trjconv  -f ../MD.xtc -s dummy.tpr    -o protein.xtc     << EOF\nProtein\nEOF")
os.system("gmx editconf -f ../{0}    -n ../index.ndx -o prot_closed.pdb << EOF\nProtein\nEOF".format(protName))

# GENERATE CROMER-MANN PARAMETERS
os.system("gmx genscatt -s dummy.tpr << EOF\nProtein\nEOF") # Removed some unnecessary options from tutorial.

# ADD CROMER-MANN STUFF TO TOPOLOGY
cromerName = inferFullName("scatter_*.itp")

with open("sas-topol.top", "w+") as file:
    for line in open("../topol.top").read().splitlines():

        if "; Include water topology" in line:
            file.write("; Include Cromer-Mann parameters\n")
            file.write("#include \"{0}\"\n\n".format(cromerName))

        file.write(line)
        file.write('\n')

# GENERATE THE ENVELOPE
os.system("gmx genenv -d {0} -f protein.xtc -s prot_closed.pdb << EOF\nProtein\nProtein\nEOF -v".format(envelopeLen))

# CREATE THE RUN INPUT FILE .TPR FOR DOING SAXS
os.system("gmx grompp -f rerun.mdp -p sas-topol.top -c ../{0} -n ../index.ndx -o sas.tpr -maxwarn 1".format(protName))
