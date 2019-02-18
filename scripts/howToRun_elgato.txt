#!/bin/bash
#BSUB -n 32
#BSUB -o massDist.out
#BSUB -e massDist.err
#BSUB -q "windfall"
#BSUB -R "span[ptile=16]"
#BSUB -J run_massDist
#---------------------------------------------------------------------
python massDist.py
###end of script
