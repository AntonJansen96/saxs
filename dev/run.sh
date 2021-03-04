#!/bin/bash

# Do the solvent-only simulation
python3 do_solvent.py

# Source gromacs waxsis version
source /usr/local/gromacs_waxsis/bin/GMXRC

# So gmx can find the envelope
export GMX_WAXS_FIT_REFFILE=envelope-ref.gro
export GMX_ENVELOPE_FILE=envelope.dat

# python3 script.py
