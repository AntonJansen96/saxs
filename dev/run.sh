#!/bin/bash

# Source gromacs waxsis version
source /usr/local/gromacs_waxsis/bin/GMXRC

# So gmx can find the envelope
export GMX_WAXS_FIT_REFFILE=envelope-ref.gro
export GMX_ENVELOPE_FILE=envelope.dat

# Do the solvent-only simulation, using gmx-waxsis, but without any saxs
# params in the .mdp file (we do a normal MD sim but with older gmx version).
# python3 do_solvent.py

# Create the .mdp files for solvent and rerun
python3 do_params.py
