"""
collection of functions for interacting with UBCS/LCP channel archiver
"""

def read_logfile(filename, tmin=None, tmax=None):
    """
    reads file generated by Channel Archiver and return all values between time minimim (tmin) and time maximum (tmax)
    """
    from numpy import genfromtxt
    data = genfromtxt(filename,skip_header=0, delimiter = '\t')
