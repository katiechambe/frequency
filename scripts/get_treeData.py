import numpy as np
import hdf5libPy3 as hdf5lib
import readsubfHDF5Py3 as readsubfHDF5
import h5py
import pandas as pd
import mergerClass
import pickle

print('Loaded modules')

df = pd.read_csv('../data/subhaloData.csv')
firstSubID = df['First Subhalo ID']
secondSubID = firstSubID+1

test       = [mergerClass.MergerTree(135, ids) for ids in secondSubID]
maxMass    = np.array([instance.maxMass()[0] for instance in test])
maxSnap    = np.array([instance.maxMass()[1] for instance in test])
data       = [instance.getData() for instance in test]
snaps      = [data[i][0] for i in range(len(test))]
masses     = [data[i][1] for i in range(len(test))]
positions  = [data[i][2] for i in range(len(test))]
velocities = [data[i][3] for i in range(len(test))]
massz0     = [data[i][4] for i in range(len(test))]

#haloIDs = np.concatentate(np.array([np.array([firstSubID[j] for i in range(len(snaps[j]))]) for j in range(len(firstSubID)) ]))
#haloSnaps = np.concatenate(snaps)
#haloMasses = np.concatenate(masses)
#np.concatenate(positions)[:,0]

zipped = list(zip(firstSubID, massz0, maxMass, maxSnap))
df = pd.DataFrame(data = zipped, columns=(['Second Subhalo ID', 'Mass at z=0', 'Max Mass', 'Max Mass Snapshot']))
df.to_csv('/rsgrps/gbeslastudents/katie/satellites/data/subhalo2TreeData.csv',index=False,header=True)

################################
# tried with a list
#zipped = list(zip(firstSubID, snaps, masses, maxMass, positions, [velocities]))
#df = pd.DataFrame(data = zipped, columns=(['Subhalo ID','Snapshot Numbers', 'Masses', 'Max Mass', 'Positions', 'Velocities']))
#df.to_csv('/rsgrps/gbeslastudents/katie/satellites/data/subhaloTreeData.csv',index=False,header=True)

# tried with a dictionary and with pickle
#zipped = {i: [i, s, m, mm, p, v] for i, s, m, mm, p, v  in zip(firstSubID, snaps, masses,maxMass, positions,velocities)}


#dict(zip(keys, values))

#pickle.dump(zipped, open('/rsgrps/gbeslastudents/katie/satellites/data/data.p', 'wb')) #Save lists to file

#df = pd.DataFrame(data = zipped, columns=(['Sub','Subhalo ID','Snapshot Numbers', 'Masses', 'Max Mass', 'Positions', 'Velocities']))

#df.to_pickle('/rsgrps/gbeslastudents/katie/satellites/data/subhaloTreeData.pkl')
