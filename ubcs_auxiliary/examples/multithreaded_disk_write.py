"""
This example is inspired by https://realpython.com/python-gil/ and designed to address issues with performance bottlenecks associated with multithreading when data collection and analysis are done using the same process hence sharing Python Interpretter and are subject to GIL.

"""

from numpy import random


# multi_threaded.py
import time
from threading import Thread
results = [None]*2
def generate_random_array(size = (10,1000,1000), dtype = 'uint16'):
    from numpy import random
    return random.randint(0,4095,size = size).astype(dtype)

def save_to_drive(arr,filename = '1.h5py'):
    from h5py import File
    from tempfile import gettempdir
    with File(gettempdir()+'/'+filename,'a') as f:
        f.create_dataset('data', data = arr, chunks= (1,1000,1000))
arr1 = generate_random_array(size = (100,1000,1000))
arr2 = generate_random_array(size = (100,1000,1000))
arr3 = generate_random_array(size = (100,1000,1000))
# t1 = Thread(target=save_to_drive, args=(arr1,str(time.time())+'_1.h5py'))
# t2 = Thread(target=save_to_drive, args=(arr2,str(time.time())+'_2.h5py'))
# t3 = Thread(target=save_to_drive, args=(arr3,str(time.time())+'_3.h5py'))
# start = time.time()
# t1.start()
# t2.start()
# #t3.start()
# t1.join()
# t2.join()
# #t3.join()
# end = time.time()
#
# print('Time taken in seconds -', end - start)



start = time.time()
save_to_drive(arr1,str(time.time())+'_1.h5py')
save_to_drive(arr2,str(time.time())+'_2.h5py')
#save_to_drive(arr3,str(time.time())+'_3.h5py')
end = time.time()

print('Time taken in seconds -', end - start)
