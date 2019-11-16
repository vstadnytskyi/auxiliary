class MultiProcessing():
    def __init__(self,function,args):
        """
        launches the input 'function' in a separate process. the args atribute has to be itterable. The class will initiate as many processes as itterables in the args.

        Parameters
        ----------
        function:
            function object
        *args:
            iterable of arguments

        Returns
        -------
        jobs :: list
            list of jobs

        Examples
        --------
        the example of usage
        >>> def function(N):
            from time import time, sleep
            import os
            print('Starting Process: pid: {}'.format(os.getpid()))
            t1 = time()
            print('[{} s] Start sleeping for {} seconds'.format(round(time()-t1,4),N))
            print('[{} s] Sleeping... '.format(round(time()-t1,4)))
            sleep(N)
            print('[{} s] Done sleeping for {} seconds'.format(round(time()-t1,4),N))
        >>> mp = MultiProcessing(funcion, (1,2,3))
            Starting Process: pid: 91038
            [0.0 s] Start sleeping for 1 seconds
            [0.0001 s] Sleeping...
            Starting Process: pid: 91039
            [0.0 s] Start sleeping for 2 seconds
            [0.0001 s] Sleeping...
            Starting Process: pid: 91040
            [0.0 s] Start sleeping for 3 seconds
            [0.0002 s] Sleeping...
            [1.0003 s] Done sleeping for 1 seconds
            [2.0001 s] Done sleeping for 2 seconds
            [3.0013 s] Done sleeping for 3 seconds
        """
        import multiprocessing
        import os
        self.jobs = []
        for arg in args:
            p = multiprocessing.Process(target=function,args=(arg,))
            p.start()
            self.jobs.append(p)

def function(N):
    """
    an example function for test purposes. It sleeps for N seconds. Prints statements when sleep starts and finishes.
    """
    from time import time, sleep
    import os
    print('Starting Process: pid: {}'.format(os.getpid()))
    t1 = time()
    print('[{} s] Start sleeping for {} seconds'.format(round(time()-t1,4),N))
    print('[{} s] Sleeping... '.format(round(time()-t1,4)))
    sleep(N)
    print('[{} s] Done sleeping for {} seconds'.format(round(time()-t1,4),N))

def test():
    """
    simple test showing how to use
    """
    mp = MultiProcessing(function,(1,2,3))

mp = MultiProcessing(function,(1,2,3))
#How to use classes.
mp.jobs #will give you a list of processes
#mp.jobs[0].pid #gives you process id
#mp.jobs[0].kill() #kills the process
