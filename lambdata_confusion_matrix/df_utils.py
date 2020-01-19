"""
Utility function to transfer ZEROS to np.nan
"""

import numpy as np
cols_with_zeros = []
def zeros_to_npnan (cols_with_zeros):
    for col in cols_with_zeros:
        col = col.replace(0, np.nan)
    return cols_with_zeros
