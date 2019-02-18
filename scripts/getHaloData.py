import numpy as np
import hdf5libPy3 as hdf5lib
import readsubfHDF5Py3 as readsubfHDF5
import h5py
import pandas as pd

h = 0.704

# access the FP run
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

# defining upper and lower mass limits in 10^10 Msun
lowerMWmass = 70.
upperMWmass = 300.

# find the group numbers with group mass in specified range
groupMask = np.where((mvirs/h> lowerMWmass) & (mvirs/h < upperMWmass)) 
groupMasses = mvirs[groupMask]/h

# find the mass of the first subhalo in each group
subhaloNumber = inds[groupMask]
firstSubMasses = submass[subhaloNumber]/h

# find the mass of the second subhalo in each group
subhalo2Number = inds[groupMask]+1
secondSubMasses = submass[subhalo2Number]/h

# get the relative positions of the first subhalo and the second subhalo
subhalo1Pos = subpos[subhaloNumber]
subhalo2Pos = subpos[subhalo2Number]


# zipping data and producing dataframe
zipped = list(zip(groupMasses, firstSubMasses, secondSubMasses, subhalo1Pos, subhalo2Pos))
df = pd.DataFrame(data = zipped, columns=['Group Mass', 'First Subhalo Mass', 'Second Subhalo Mass','First Subhalo Position', 'Second Subhalo Position'])

df.to_csv('/rsgrps/gbeslastudents/katie/satellites/data/subhaloData.csv',index=False,header=False)

# saving data
#toSave = np.column_stack((groupMassesCol, firstSubMassesCol, secondSubMassesCol))
#np.savetxt('/rsgrps/gbeslastudents/katie/tempDataBox/subhaloData.txt', toSave, delimiter = "  ")

####################################
#in case you need to time something:
#import time
#start = time.time()
#code to be timed
#end = time.time()
