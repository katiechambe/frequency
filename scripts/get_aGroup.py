import numpy as np
import hdf5libPy3 as hdf5lib
import readsubfHDF5Py3 as readsubfHDF5
import h5py
import pandas as pd
import mergerClass

h = 0.704

# access the dark run
base = '/rsgrps/gbeslastudents/Illustris/GroupCatalogsDark/'
basedir = base
obj = readsubfHDF5.subfind_catalog(basedir, 135, grpcat=True, keysel=['GroupFirstSub','SubhaloMass',
'SubhaloPos','SubhaloGrNr', 'Group_M_TopHat200','Group_R_TopHat200','SubhaloVel','GroupNsubs'])

# defining each column of the data structure
inds = obj.GroupFirstSub
submass = obj.SubhaloMass
subpos = obj.SubhaloPos
subvel = obj.SubhaloVel
subgr = obj.SubhaloGrNr
mvirs = obj.Group_M_TopHat200
rvirs = obj.Group_R_TopHat200
nsubs = obj.GroupNsubs

# defining upper and lower mass limits in 10^10 Msun
lowerMWmass = 8         # 8e10
upperMWmass = 50        # 5e11 (slightly more massive than an LMC to account for xtra subhalos)

# find the group numbers with group mass in specified range
groupMask = np.where((mvirs/h> lowerMWmass) & (mvirs/h < upperMWmass))
groupMasses = mvirs[groupMask]/h

# look for the subhalo group number for the first group
subhalo1Number = inds[groupMask]
#groupNumbers = subgr[subhaloNumber]

# see if we can mask the subhalo group number array to pull out all halos in one group
mask = subgr == subgr[subhaloNumber[0]]

groupNumbers = subgr[mask]
masses = submass[mask]
poss = subpos[mask]

#subhalo1Pos = subpos[mask]
#subhalo2Pos = subpos[mask]
x1 = poss[:,0]
y1 = poss[:,1]
z1 = poss[:,2]
#x2 = subhalo2Pos[:,0]
#y2 = subhalo2Pos[:,1]
#z2 = subhalo2Pos[:,2]

# get the velocities of the first subhalo and the second subhalo
#subhalo1Vel = subvel[subhaloNumber]
#subhalo2Vel = subvel[subhalo2Number]
#vx1 = subhalo1Vel[:,0]
#vy1 = subhalo1Vel[:,1]
#vz1 = subhalo1Vel[:,2]
#vx2 = subhalo2Vel[:,0]
#vy2 = subhalo2Vel[:,1]
#vz2 = subhalo2Vel[:,2]

# trying to get the max mass of one subhalo, and it's position as a function of snapshot to plot
#trialID = subhalo2Number[0]
#test = mergerClass.MergerTree(135, 452859)
#print(test.maxMass())


# zipping data and producing dataframe
zipped = list(zip(groupNumbers, subhaloNumber, masses, x1, y1, z1))

df = pd.DataFrame(data = zipped, columns=['Group Number','Subhalo ID','First Subhalo Mass', 'First Subhalo x', 'First Subhalo y', 'First Subhalo z'])

df.to_csv('/rsgrps/gbeslastudents/katie/satellites/data/aGroup.csv',index=False,header=True)

