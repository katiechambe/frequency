import numpy as np
import hdf5libPy3 as hdf5lib
import readsubfHDF5Py3 as readsubfHDF5
import h5py
import pandas as pd
import mergerClass

h = 0.704

# access the dark matter run
base = '/rsgrps/gbeslastudents/Illustris/GroupCatalogsDark/'
basedir = base
obj = readsubfHDF5.subfind_catalog(basedir, 135, grpcat=True, keysel=['GroupFirstSub','SubhaloMass',
'SubhaloPos','SubhaloGrNr', 'Group_M_TopHat200','Group_R_TopHat200','SubhaloVel'])

# defining each column of the data structure
inds = obj.GroupFirstSub
submass = obj.SubhaloMass
subpos = obj.SubhaloPos
subvel = obj.SubhaloVel
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
x1 = subhalo1Pos[:,0]
y1 = subhalo1Pos[:,1]
z1 = subhalo1Pos[:,2]
x2 = subhalo2Pos[:,0]
y2 = subhalo2Pos[:,1]
z2 = subhalo2Pos[:,2]

# get the velocities of the first subhalo and the second subhalo
subhalo1Vel = subvel[subhaloNumber]
subhalo2Vel = subvel[subhalo2Number]
vx1 = subhalo1Vel[:,0]
vy1 = subhalo1Vel[:,1]
vz1 = subhalo1Vel[:,2]
vx2 = subhalo2Vel[:,0]
vy2 = subhalo2Vel[:,1]
vz2 = subhalo2Vel[:,2]

# trying to get the max mass of one subhalo, and it's position as a function of snapshot to plot
trialID = subhalo2Number[0]
test = mergerClass.MergerTree(135, 452859)
print(test.maxMass())


# zipping data and producing dataframe
zipped = list(zip(subhaloNumber, subhalo2Number, groupMasses, firstSubMasses, secondSubMasses, x1, y1, z1, x2, y2, z2,vx1,vy1,vz1,vx2,vy2,vz2))

df = pd.DataFrame(data = zipped, columns=['First Subhalo ID','Second Subhalo ID','Group Mass', 'First Subhalo Mass', 'Second Subhalo Mass','First Subhalo x', 'First Subhalo y', 'First Subhalo z', 'Second Subhalo x','Second Subhalo y','Second Subhalo z', 'First Subhalo v_x', 'First Subhalo v_y', 'First Subhalo v_z', 'Second Subhalo v_x', 'Second Subhalo v_y', 'Second Subhalo v_z'])

df.to_csv('/rsgrps/gbeslastudents/katie/satellites/data/subhaloData.csv',index=False,header=True)

