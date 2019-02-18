import numpy as np

def positionCorrection(satellitePosition, hostPosition):
    boxSize = 75000 # box size in Mpc
    differences = satellitePosition - hostPosition
    corrected = []
    for diff in differences:
        x = diff
        if np.abs(diff) > (boxSize/2):
            if diff > 0:
                x = boxSize - diff
            else:
                x = boxSize + diff
        corrected.append(x)
    return corrected

