"""
advance Sleep functions
author: Valentyn Stadnytskyi
data: 2017 - Nov 17 2018

functions:
psleep - precision sleep takes
intsleep with inputs t, dt and interupt as a function.

The precision sleep class.
functiob:
psleep - sleep specified amount of time with sub milisecond precision
test_sleep - for testing purposes. will print how much time the code waited.
This is important for the Windows platform programs if precise wait is required.
The Windows OS has ~15-17 ms latenct - the shortest time between attentions from OS.
"""

def beep():
    from IPython.display import Audio
    sound_file = 'http://www.soundjay.com/button/beep-07.wav'
    Audio(sound_file, autoplay=True)

def append_index_file(filename = None, comments = '', params = None):    
    """
    This funtiction is designed to append an index file represented as a text document with information about from which jupyter notebook it was called, comments to append and parameters to append.
    """
    import ipynbname
    from time import ctime, time, sleep
    if filename is not None:
        with open(filename, "a") as append_index:  # append mode

            append_index.write(f"------ Jupyter Notebook Entry Starts: {ctime(time())} ------ \n")
            comments += f'\n'
            commnets += f'This message was generated from {ipynbname.path()} \n'
            comments += f'------ Jupyter Notebook Entry Parameters ------ \n'
            if params is not None:
                for key in params.keys():
                    comments += f'key = {key}\n'
            else:
                comments += f'no parameters were specified \n'
            comments += f'------ Jupyter Notebook Entry Ends ------ \n \n'
            append_index.write(f"{comments}")
    else:
        print('filename is None. Please provide proper filename')
