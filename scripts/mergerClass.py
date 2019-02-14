import numpy as np
import util.hdf5lib as hdf5lib
import simread.readsubfHDF5 as readsubfHDF5
import h5py
#import pandas as pd
import readtreeHDF5


treeDirectory = '/rsgrps/gbeslastudents/Illustris/Illustris-1-Dark-MergerTree'
tree = readtreeHDF5.TreeDB(treeDirectory)
branch = tree.get_main_branch( snapnum = 135, subfind_id = 452859, keysel = ['SnapNum', 'SubhaloMass'])

snaps = branch.SnapNum
masses = branch.SubhaloMass

print(snaps[0:10])
print(max(masses))
print(snaps[np.where(max(masses)=masses)]


