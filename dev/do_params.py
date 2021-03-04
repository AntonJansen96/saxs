#!/bin/python3

file = open("MD.mdp", 'a')

def addParam(name, value, comment = "NUL"):
    if (comment == "NUL"):
        file.write("{:20s} = {:20s}\n".format(name, str(value)))
    else:            
        file.write("{:20s} = {:20s} ; {:13s}\n".format(name, str(value), comment))

file.write("\n; SAXS PARAMETERS\n")
addParam('define', '-DSCATTER')
addParam('scatt-coupl', 'xray', 'SAXS/WAXS type.')
addParam('waxs-pbcatom', 5175, 'Number of solute atoms.')
addParam('waxs-fc', 1)
addParam('waxs-nq', 100)
addParam('waxs-startq', 0)
addParam('waxs-endq', 5)
addParam('waxs-solute', 'Prot-Masses', 'Solute group.')
addParam('waxs-solvent', 'Water_and_ions', 'Solvent group.')

file.close()
