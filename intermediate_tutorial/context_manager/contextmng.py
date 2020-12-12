with open('notes.txt', 'w') as file: # this context manager knows to close the file after we're done
    file.write('some todo') 

file = open('notes.txt', 'w') # with no context manager
try:
    file.write('some todo2 ')
finally:
    file.close()

from threading import Lock

lock = Lock()

lock.acquire()

lock.release()

# with lock:
    # acquires and releases automatically

class ManagedFile: # creating your own context manager with class
    def __init__(self,filename):
        print('init')
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print('exception has been handled')
        print('exc: ', exc_type, exc_value)
        print('exit')
        return True

with ManagedFile('notes2.txt') as file:
    print('do some stuff')
    file.write('some todo')
print('continuing')

# creating a context manager through a function
from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        # write exit method to free up resources
        f.close()

with open_managed_file('notes3.txt') as f:
    f.write('some todoooo')