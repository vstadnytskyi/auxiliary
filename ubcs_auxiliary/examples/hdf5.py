def write_safely():
    """
    an example of how to write to hdf5 file safely.
    """
    from h5py import File
    from tempfile import gettempdir
    root = gettempdir()
    import os
    f = File(os.join.path(root,'test.hdf5'),'r')


def check_if_hdf5_is_open():
    pass

def check_memory_leak():
    from memory_profiler import profile

    @profile
    def mess_with_memory():
        huge_list = range(20000000)
        del huge_list
        print("why this kolaveri di?")
