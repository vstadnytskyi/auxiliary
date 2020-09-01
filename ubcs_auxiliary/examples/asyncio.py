"""
This example is inspired by https://realpython.com/python-gil/ and designed to address issues with performance bottlenecks associated with multithreading when data collection and analysis are done using the same process hence sharing Python Interpretter and are subject to GIL.

"""
import asyncio

async def get_time():
    import asyncio
    from time import time, ctime
    await asyncio.sleep(1)
    return ctime(time())
