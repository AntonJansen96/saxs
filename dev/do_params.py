#!/bin/python3

file = open("MD.mdp", 'a')

def addParam(name, value, comment = "NUL"):
    if (comment == "NUL"):
        file.write("{:20s} = {:17s}\n".format(name, str(value)))
    else:            
        file.write("{:20s} = {:17s} ; {:13s}\n".format(name, str(value), comment))

file.write("\n; SAXS PARAMETERS\n")
addParam('define', '-DSCATTER')
addParam('scatt-coupl', 'xray', 'SAXS/WAXS type.')
addParam('waxs-pbcatom', 5175, 'Number of solute atoms.')
# addParam('waxs-fc', 1, 'Force constant for SAXS-driven MD.')
addParam('waxs-nq', 100, '100 is reasonable for SAXS from trajectory.')
addParam('waxs-startq', 0, 'Smallest q (nm^-1).')
addParam('waxs-endq', 5, 'Largest q (nm^-1).')

addParam('waxs-solute', 'Prot-Masses', 'Solute group.')
addParam('waxs-solvent', 'Water_and_ions', 'Solvent group.')

file.close()

# ADD THE SAXS PARAMETERS SPECIFIC TO THE SOLVENT TO solvent.mdp
# file = open("solvent.mdp", 'a')

# def addParam(name, value, comment = "NUL"):
#     if (comment == "NUL"):
#         file.write("{:20s} = {:17s}\n".format(name, str(value)))
#     else:            
#         file.write("{:20s} = {:17s} ; {:13s}\n".format(name, str(value), comment))

# file.write("\n; SAXS PARAMETERS\n")
# addParam('define', '-DSCATTER')
# addParam('scatt-coupl', 'xray', 'SAXS/WAXS type.')
# addParam('waxs-pbcatom', 0, 'Number of solute atoms.')
# addParam('waxs-fc', 1, 'Force constant for SAXS-driven MD.')
# addParam('waxs-nq', 100, '100 is reasonable for SAXS from trajectory.')
# addParam('waxs-startq', 0, 'Smallest q (nm^-1).')
# addParam('waxs-endq', 5, 'Largest q (nm^-1).')

# addParam('waxs-solute', '')
# addParam('waxs-solvent', 'Water_and_ions', 'Solvent group.')

# file.close()