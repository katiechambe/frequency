import numpy as np
import hdf5libPy3 as hdf5lib
import readsubfHDF5Py3 as readsubfHDF5
import h5py
import pandas as pd
import mergerClass

df = pd.read_csv('data_dwarfGroupSubhalos-OneSubhalo.csv')
groups = df['Group Number']

#h = 0.704

# access the dark run
base = '/rsgrps/gbeslastudents/Illustris/GroupCatalogsDark/'
basedir = base
obj = readsubfHDF5.subfind_catalog(basedir, 135, grpcat=True, keysel=['GroupFirstSub'])

print('loaded catalog')

# defining each column of the data structure
inds = obj.GroupFirstSub
#submass = obj.SubhaloMass
#subpos = obj.SubhaloPos
#subvel = obj.SubhaloVel
#subgr = obj.SubhaloGrNr
#mvirs = obj.Group_M_TopHat200
#rvirs = obj.Group_R_TopHat200
#nsubs = obj.GroupNsubs

# gonna export only groups with 1 LMC-like subhalo
#groups = groups[nsubs[groups]==1]
groupsList = list(groups)

data = []
for i in groups:  
    groupFirstSub = inds[i]
    inst = mergerClass.MergerTree(135,groupFirstSub)
    snaps, masses, positions, velocities, _, ids, subfindID = inst.getData()
    for j in range(len(snaps)):
        data.append([i, groupFirstSub, snaps[j], masses[j], positions[j][0], positions[j][1], positions[j][2], velocities[j][0], velocities[j][1], velocities[j][2], ids[j], subfindID[j]])
    count = groupsList.index(i)
    if count%10 == 0:
        print("Have gone through ",count," groups out of ", len(groups)+1)

print('finished collecting data')

df = pd.DataFrame(data = data, columns=['Group Number','Subhalo ID', 'Snapshot','Mass', 'Pos x', 'Pos y', 'Pos z', 'Vel x', 'Vel y', 'Vel z', 'Subhalo ID at Snap', 'Subfind ID at snapp'])

df.to_csv('data_oneSubhaloGroups.csv',index=False,header=True)

print('finished exporting data')
