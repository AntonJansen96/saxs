#!/bin/bash

# Make sure trajectory is whole and centered
# gmx trjconv -f MD.xtc -o MD.xtc -s MD.tpr -center -pbc whole << EOF
# Protein
# System
# EOF

# make directories
mkdir buffer saxs

# Source gromacs waxsis version
source /usr/local/gromacs_waxsis/bin/GMXRC

# So gmx can find the envelope
export GMX_WAXS_FIT_REFFILE=envelope-ref.gro
export GMX_ENVELOPE_FILE=envelope.dat
# export GMX_WAXS_VERBOSE=3

# Create the .mdp files for solvent and rerun
python3 do_params.py

# Do the solvent-only simulation, using gmx-waxsis, but without any saxs
# params in the .mdp file (we do a normal MD sim but with older gmx version).
python3 do_solvent.py

# Prepare the saxs run
python3 do_saxs.py

cd saxs
gmx mdrun -v -s sas.tpr -rerun ../MD.xtc -sw ../buffer/solvent.tpr -fw ../buffer/solvent.xtc
cd ..
