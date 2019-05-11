import numpy as np
import hdf5libPy3 as hdf5lib
import readsubfHDF5Py3 as readsubfHDF5
import h5py
import pandas as pd
import mergerClass

df = pd.read_csv('data_dwarfGroups.csv')
groups = df['Group Numbers']

h = 0.704

# access the dark run
base = '/rsgrps/gbeslastudents/Illustris/GroupCatalogsDark/'
basedir = base
obj = readsubfHDF5.subfind_catalog(basedir, 135, grpcat=True, keysel=['GroupFirstSub','SubhaloMass',
'SubhaloPos','SubhaloGrNr', 'Group_M_TopHat200','Group_R_TopHat200','SubhaloVel','GroupNsubs'])

print('loaded catalog')

# defining each column of the data structure
inds = obj.GroupFirstSub
submass = obj.SubhaloMass
subpos = obj.SubhaloPos
subvel = obj.SubhaloVel
subgr = obj.SubhaloGrNr
mvirs = obj.Group_M_TopHat200
rvirs = obj.Group_R_TopHat200
nsubs = obj.GroupNsubs

# gonna export only groups with 1 LMC-like subhalo
groups = groups[nsubs[groups]==1]
groupsList = list(groups)

data = []
for i in groups: 
    numHalos = nsubs[i]
    groupFirstSub = inds[i]

    for j in range(numHalos):
        subID = groupFirstSub+j

        if submass[subID]/h > 0.1: # make sure subhalo mass is > 10^9 Msun
            # data at z=0
            massz0 = submass[subID]/h
            posz0  = subpos[subID]
            posx = posz0[0]
            posy = posz0[1]
            posz = posz0[2]

            velz0  = subvel[subID]
            velx = velz0[0]
            vely = velz0[1]
            velz = velz0[2]
            
            # max mass and corresponding snapnumber
            inst = mergerClass.MergerTree(135, subID)
            maxMass, maxMassSnap    = inst.maxMass()[0]/h, inst.maxMass()[1]
            # i is group number, subID is subhalo ID, 
            data.append([i, subID, massz0, maxMass, maxMassSnap, posx, posy, posz, velx, vely, velz, 0])
    count = groupsList.index(i)
    if count%100 == 0:
        print("Have gone through ",count," groups out of ", len(groups)+1)

# zipping data and producing dataframe
#zipped = list(zip(data))
print('finished collecting data')

df = pd.DataFrame(data = data, columns=['Group Number','Subhalo ID','Mass at z=0', 'Max Mass', 'Max Mass Snap', 'Pos x', 'Pos y', 'Pos z', 'Vel x', 'Vel y', 'Vel z', 'Flag'])

df.to_csv('data_dwarfGroupSubhalos-OneSubhalo.csv',index=False,header=True)

print('finished exporting data')
