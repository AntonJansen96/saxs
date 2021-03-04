#!/bin/bash

# Source gromacs waxsis version here
source /usr/local/gromacs_waxsis/bin/GMXRC

# So gmx can find the envelope
export GMX_WAXS_FIT_REFFILE=envelope-ref.gro
export GMX_ENVELOPE_FILE=envelope.dat

python3 script.py
