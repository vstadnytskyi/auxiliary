def start_new_thread(function, *args , **kwargs):
    """
    launches the input 'function' in a separate thread with daemon == True

    Parameters
    ----------
    function:
        function object
    *args:
        iterable of arguments
    **kwargs:
        dictionary of keywords


    Returns
    -------

    Examples
    --------
    the example of usage

    >>> def func(*arg,**kwargs):
            from time import time,sleep
            t1 = time()
            sleep(N)
            t2 = time()
            print('this thread slept for {} seconds'.format(t2-t1))
            print('input parameters: args = {}, kwargs = {!r}'.format(arg[0],kwargs['keyword']))
    >>> start_new_thread(func, 1, keyword = 'this is key 1 value')
    this thread slept for 1.002244234085083 seconds
    input parameters: args = 1, kwargs = 'keywords argument'
    """
    from threading import Thread
    thread = Thread(target=function, args = args, kwargs = kwargs)
    thread.daemon = True
    thread.start()

def test_start_new_thread(N = 3,M = 'this is key 1 value'):
    def func(*arg,**kwargs):
        from time import time,sleep
        t1 = time()
        sleep(N)
        t2 = time()
        print('this thread slept for {} seconds'.format(t2-t1))
        print('input parameters: args = {}, kwargs = {!r}'.format(arg[0],kwargs['keyword']))
    start_new_thread(func,N , keyword = M)
