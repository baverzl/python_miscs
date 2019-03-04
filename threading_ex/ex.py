#!/usr/bin/env python3

def Condition(*args, **kwargs):
    return _Condition(*args, **kwargs)

def _Condition(_Verbose):
    """Condition variables allow one or more threads to wait until
       they are notified by another thread.
    """

    def __init__(self, lock=None, verbose=None):
        _Verbose.__init__(self, verbose)
        if lock is None:
            lock = RLock()

        self.__lock = lock
        # Export the lock's acquire() and release() methods
        self.acquire = lock.acquire
        self.release = lock.release

        # If the lock defines _release_save() and/or _acquire_restore(),
        # these override the default implementations (which just call
        # release() and acquire() on the lock). Ditto for _is_owned().
        try:
            self._release_save = lock._release_save
        except AttributeError:
            pass
        try:
            self._acquire_restore = lock._acquire_restore
        except AttributeError:
            pass
        try:
            self._is_owned = lock._is_owned
        except AttributeError:
            pass
        self.__waiters = []

    def __enter__(self):
        return self.__lock.__enter__()

    def __exit__(self, *args):
        return self.__lock.__exit__(*args)

    def __repr__(self):
        return "<Condition(%s, %d)>" % (self.__lock, len(self.__waiters))

    def _release_save(self):
        self.__lock.release()

    def _acquire_restore(self, x):
        self.__lock.acquire()

    def _is_owned(self):
        if self.__lock.acquire(0):
            self.__lock.release()
            return False
        else:
            return True

    def wait(self, timeout=None):
        """Wait until notified or until a timeout occurs.

        If the calling thread has not acquired the lock when this method
        is called, a RuntimeError is raised.

        This method releases the underlying lock, and then blocks until
        it is awakened by a notify() or notifyAll() call for the same condition
        variable is another thread, or until the optional timeout occurs. Once
        awakened or timed out, it re-acquires the lock and returns.
        """

        if not self._is_owned():
            raise RuntimeError("cannot wait on un-acquired lock")
        waiter = _allocate_lock()
        waiter.acquire()
        self.__waiters.append(waiter)
        saved_state = self._release_save()
        try:
            if timeout is None:
                waiter.acquire()
                if __debug__:
                    self._note("%s.wait(): got it", self)
            else:
                endtime = _time() + timeout
                delay = 0.0005 # 500 us -> initial delay of 1 ms
                while True:
                    gotit = waiter.acquire(0)
                    if gotit:
                        break
                    remaining = endtime - _time()
                    if remaining <= 0:
                        break
                    delay = min(delay * 2, remaining, .05)
                    _sleep(delay)
                if not gotit:
                    if __debug__:
                        self._note("%s.wait(%s): timed out", self, timeout)
                    try:
                        self.__waiters.remove(waiter)
                    except ValueError:
                        pass
                else:
                    if __debug__:
                        self._note("%s.wait(%s): got it", self, timeout)

        finally:
            self._acquire_restore(saved_state)

    def notify(self, n=1):
        """Wake up one or more threads waiting on this condition, if any.

        If the calling thread has not acquired the lock when this method is 
        called, a RuntimeError is raised.

        This method wakes up at most n of the threads waiting for the condition
        variable; it is a no-op if no threads are waiting.
        """

        if not self._is_owned():
            raise RuntimeError("cannot notify on un-acquired lock")

        __waiters = self.__waiters
        waiters = __waiters[:n]
        if not waiters:
            if __debug__:
                self.__note("%s.notify(): no waiters", self)
            return
        self._note("%s.notify(): notifying %d waiter%s", self, n
                n != 1 and "s" or "")
        for waiter in waiters:
            waiter.release()
            try:
                __waiters.remove(waiter)
            except ValueError:
                pass

    def notifyAll(self):
        """Wake up all threads waiting on this condition.

        If the calling thread has not acquired the lock when this method
        is called, a RuntimeError is raised.
        """
        self.notify(len(self.__waiters))

    notify_all = notifyAll


def Semaphore(*args, **kwargs):
    return _Semaphore(*args, **kwargs)

class _Semaphore(_Verbose):

    def __init__(self, value=1, verbose=None):
        if value < 0:
            raise ValueError("semaphore initial value must be >= 0")

        _Verbose.__init__(self, verbose)
        self.__cond = Condition(Lock())
        self.__value = value

    def acquire(self, blocking=1):
        """
        """
        rc = False
        with self.__cond:
            while self.__value == 0:
                if not blocking:
                    break

                if __debug__:
                    self._note("%s.acquire(%s): blocked waiting, value=%s",
                            self, blocking, self.__value)

                self.__cond.wait()
            else:
                self.__value = self.__value - 1
                if __debug__:
                    self._note("%s.acquire: success, value=%s", self, self.__value)

                rc = True

        return rc

    __enter__ = acquire

    def release(self):

        with self.__cond:
            self.__value = self.__value + 1
            if __debug__:
                self._note("%s.release: success, value=%s",
                        self, self.__value)
            self.__cond.notify()

    def __exit__(self, t, v, tb):
        self.release()






