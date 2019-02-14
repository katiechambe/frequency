import numpy as np
import util.hdf5lib as hdf5lib
import simread.readsubfHDF5 as readsubfHDF5
import h5py

h = 0.704

#access the FP run
base = '/rsgrps/gbeslastudents/Illustris/GroupCatalogsDark/'
basedir = base
obj = readsubfHDF5.subfind_catalog(basedir, 135, grpcat=True, keysel=['GroupFirstSub','SubhaloMass',
'SubhaloPos','SubhaloGrNr', 'Group_M_TopHat200','Group_R_TopHat200'])

# defining each column of the data structure
inds = obj.GroupFirstSub
submass = obj.SubhaloMass
subpos = obj.SubhaloPos
subgr = obj.SubhaloGrNr
mvirs = obj.Group_M_TopHat200
rvirs = obj.Group_R_TopHat200

print("finished importing data")

lowerMWmass = 70.    # mass in 10^10 Msun
upperMWmass = 300.   # mass in 10^10 Msun


MWmasses = []

for i in range(len(inds)): 
    if ((mvirs[i]/h > lowerMWmass)  and (upperMWmass > mvirs[i]/h)):
        MWmasses.append(mvirs[i]/h)

np.savetxt('/rsgrps/gbeslastudents/katie/tempDataBox/MWmasses.txt', MWmasses, delimiter = "  ")
