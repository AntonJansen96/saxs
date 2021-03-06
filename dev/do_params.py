#!/bin/python3

import os

# COPY + RENAME MD.MDP
os.system("cp MD.mdp buffer/solvent.mdp")
os.system("cp MD.mdp saxs/rerun.mdp")

# DO THE BUFFER.MDP
file = open("buffer/solvent.mdp", 'a')

def addParam(name, value, comment = "NUL"):
    if (comment == "NUL"):
        file.write("{:20s} = {:17s}\n".format(name, str(value)))
    else:            
        file.write("{:20s} = {:17s} ; {:13s}\n".format(name, str(value), comment))

file.write("\n; SAXS PARAMETERS\n")
addParam('define', '-DSCATTER')
addParam('scatt-coupl', 'xray', 'SAXS/WAXS type.')
addParam('waxs-pbcatom', 0, 'The atom ID used to make the solute whole.')
addParam('waxs-fc', 1, 'Force constant for SAXS-driven MD.')
addParam('waxs-nq', 200, '100 is reasonable for SAXS from trajectory.')
addParam('waxs-startq', 0, 'Smallest q (nm^-1).')
addParam('waxs-endq', 10, 'Largest q (nm^-1).')

addParam('waxs-solute', '')
addParam('waxs-solvent', 'Water_and_ions', 'Solvent group.')

file.close()

# DO THE RERUN.MDP
file = open("saxs/rerun.mdp", 'a')

file.write("\n; SAXS PARAMETERS\n")
addParam('define', '-DSCATTER')
addParam('scatt-coupl', 'xray', 'SAXS/WAXS type.')
addParam('waxs-pbcatom', -2, 'The atom ID used to make the solute whole.')
addParam('waxs-fc', 1, 'Force constant for SAXS-driven MD.')
addParam('waxs-nq', 200, '100 is reasonable for SAXS from trajectory.')
addParam('waxs-startq', 0, 'Smallest q (nm^-1).')
addParam('waxs-endq', 10, 'Largest q (nm^-1).')

addParam('waxs-solute', 'Prot-Masses', 'Solute group.')
addParam('waxs-solvent', 'Water_and_ions', 'Solvent group.')

file.close()
