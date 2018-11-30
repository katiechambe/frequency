'''
 choose the hydro sample with the same criteria as the DM primary
sample:
    1. Mvir within 0.7-3x10^12
    2. LMCs within Rvir at z=0 and infall mass of 8-32e10
    3. keep IDs of both, Mvir, Mstar, Msub, LMC rel. v and r
'''

import util.hdf5lib as hdf5lib
import simread.readsubfHDF5 as readsubfHDF5                      
import numpy as np
import h5py


h = 0.704


#access the FP run
base = '/rsgrps/gbeslastudents/Illustris/GroupCatalogsDark/' 
basedir = base
obj = readsubfHDF5.subfind_catalog(basedir, 135, grpcat=True, keysel=['GroupFirstSub','SubhaloMass', 'SubhaloVel', 'SubhaloPos','SubhaloGrNr', 'Group_M_Crit200', 'Group_M_TopHat200','SubhaloMassType', 'Group_R_TopHat200'])


# defining each column of the data structure
inds = obj.GroupFirstSub
submass = obj.SubhaloMass
subvel = obj.SubhaloVel
subpos = obj.SubhaloPos
subgr = obj.SubhaloGrNr
grcrit = obj.Group_M_Crit200
mtops = obj.Group_M_TopHat200
rtops = obj.Group_R_TopHat200
submasstype = obj.SubhaloMassType

# We can find the number of groups by figuring out the length of the inds
# structure
print('The number of groups in the snapshot is %i.' % len(inds))

# We can also find the total number of halos (the number of groups and the number
# of subhalos) in the snapshot at z=0 by looking at the length of the list of all
# masses of all malos
print('The total number of halos in this snapshot is %i.' % len(submass))

# Now we want to find the number of the most massive halos that have approximately
# the mass of the milky way halo
lowerMWmass = 70 # lower milky way halo mass in 10^10 Msun
upperMWmass = 300 # upper milky way halo mass in 10^10 Msun
lowerSatmass = 8 # lower massive satellite mass in 10^10 Msun
upperSatmass = 32 # upper massive satellite mass in 10^10 Msun

# finding the indices of the host galaxies (masses of 0.7-3e12 solar)
hostInds = inds[np.where(( submass[inds] <= upperMWmass ) & ( submass[inds] >= lowerMWmass ))]
satelliteInds = inds[np.where(( submass[inds+1] <= lowerSatmass ) & ( submass[inds+1] >= lowerMWmass ))]


print('The number of Milky way type halos is %i' % len(hostInds))
print('The number of Milky way type halos hosting massive satellites is %i' % len(satelliteInds))

MWtypesubmass = submass[hostInds]
MWtypesubvel = subvel[hostInds]
MWtypesubpos = subpos[hostInds]
MWtypesubgr = subgr[hostInds]
MWtypegrcrit = grcrit[hostInds]
MWtypemtops = mtops[hostInds]
MWtypertops = rtops[hostInds]










#import merger_tree_class as mtc
#from cosmo_tools import snapnum2z, time
#from scipy import linalg as la
#from correct_position import *
#import scipy.linalg as la

