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

print('loaded in catalog')

#######################################
#####     Beginning Mass Cuts     #####
#######################################
# mass cut criteria:
# 1. group mass cut
# 2. most massive halo > 1e10 at z=0, second most massive > 1/15e10 at z=0
#
# -------------------------------------


# 1. first mass cut on total group mass
lowerMWmass = 8         # 8e10 lower group mass cut 
upperMWmass = 50        # 5e11 (slightly more massive than an LMC to account for xtra subhalos)
groupMask = np.where((mvirs/h > lowerMWmass) & (mvirs/h < upperMWmass))  # creating a mask for the groups that pass the first mass cut
groupMasses = mvirs[groupMask]/h   # pulling out all the group masses in the specified range
groupNumbers = subgr[inds[groupMask]] # list of the group numbers 
firstSubhaloNumber = inds[groupMask] # first subhaloID in each group
initialGroupNumbers = groupNumbers

print('finished first mass cut')

# 2. second mass cut on z=0 primary mass > 1e10
#    this cut cuts out about 2000 groups
#firstSubMasses = submass[firstSubhaloNumber]/h      # masses of first subhalo in each group
#secondSubMasses = submass[firstSubhaloNumber+1]/h   # masses of second subhalo in each group
#submassMask = np.where((firstSubMasses > 1))  #make sure biggest subhalo has z=0 mass of at least 1e10
#firstSubhaloNumber = firstSubhaloNumber[submassMask] # updating to get the first subhalo number of each group that satisfies mass cut criterion 2
#groupNumbers = subgr[firstSubhaloNumber]  # updated list of group numbers with mass cuts 1 and 2


# 3. make sure max mass of 1 of first 5 subhalos is in 

# 1 look at first 10 subhalos in each group, and get their max masses
groups = []
for i in firstSubhaloNumber: # get rid of [0:10] after testing
#    maxMasses = []
    var = min(15, nsubs[subgr[i]])
    for j in range(var):
        subID = i + j
        inst  = mergerClass.MergerTree(135, subID)
        maxMass = inst.maxMass()[0]/h
        currentMass = submass[subID]/h   # REMEMBER LITTLE h
        if maxMass >= 8 and maxMass <= 32 and currentMass >= 1:
            groups.append(subgr[i])
            break

print('got groups')

groupNumbers = np.array(groups)

zipped = list(zip(groupNumbers))
,
df = pd.DataFrame(data = zipped, columns=['Group Numbers'])

df.to_csv('/rsgrps/gbeslastudents/katie/satellites/scripts/data_getDwarfGroups.csv',index=False,header=True)

###############
###############
###############
###############
###############


# 2 if one of the subhalos has mass in the range 8e10-3.2e11, save the group number
# 3 take the list of group numbers, pull out all the subhalos in each group with mass > 1e10. 
# 4 export list of group numbers, subhalo IDs, z=0 mass, max mass, max mass snap, positions, velocities

# First make cuts of Max mass of most massive thing in each group and save ID, max mass, and z=0 mass, and Nsubs, can also save positions and velocities
# table 1: potential candidates
# table 2: LMC analogs that have passed mass cuts, positions and velocities


# find the mass of the first subhalo in each group
#subhaloNumber = inds[groupMask]
#firstSubMasses = submass[subhaloNumber]/h

# find the mass of the second subhalo in each group
#subhalo2Number = inds[groupMask]+1
#secondSubMasses = submass[subhalo2Number]/h

#submassMask = np.where((firstSubMasses> 0.1) & (secondSubMasses > 0.01)) 
#subhaloNumber = subhaloNumber[submassMask]
#subhalo2Number = subhaloNumber+1
#firstSubMasses = submass[subhaloNumber]/h
#secondSubMasses = submass[subhalo2Number]/h

#subhaloNumber = subhaloNumber[firstSubMassMask]
#firstSubMasses = submass[subhaloNumber]/h
#secondSubMassMask = np.where((secondSubMasses> 0.01)) 
#subhalo2Number = subhaloNumber[secondSubMassMask]
#secondSubMasses = submass[subhalo2Number]/h

# get the relative positions of the first subhalo and the second subhalo
#subhalo1Pos = subpos[subhaloNumber]
#subhalo2Pos = subpos[subhalo2Number]
#x1 = subhalo1Pos[:,0]
#y1 = subhalo1Pos[:,1]
#z1 = subhalo1Pos[:,2]
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
#zipped = list(zip(subhaloNumber, groupMasses, firstSubMasses, secondSubMasses, x1, y1, z1, x2, y2, z2,vx1,vy1,vz1,vx2,vy2,vz2))

#df = pd.DataFrame(data = zipped, columns=['First Subhalo ID','Group Mass', 'First Subhalo Mass', 'Second Subhalo Mass','First Subhalo x', 'First Subhalo y', 'First Subhalo z', 'Second Subhalo x','Second Subhalo y','Second Subhalo z', 'First Subhalo v_x', 'First Subhalo v_y', 'First Subhalo v_z', 'Second Subhalo v_x', 'Second Subhalo v_y', 'Second Subhalo v_z'])

#df.to_csv('/rsgrps/gbeslastudents/katie/satellites/data/dwarfData.csv',index=False,header=True)

