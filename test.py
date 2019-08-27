import fcntl
import os
from multiprocessing.shared_memory import SharedMemory

print(fcntl.__dict__)
f = open('file.txt')
print(f)
print(f.fileno())
s = '19378128y8edhkaHDWUIWGAUKJDUQWdwiehdfiabdfajwuefjasbvdfuaewbdfjasvudkfhnsavbdfukaskdjfbukaws'
print(fcntl.fcntl(f.fileno(), fcntl.F_GETPATH, s))
print(s)
print(fcntl.fcntl(2, fcntl.F_GETPATH, s))
print(s)

shm = SharedMemory(create=True, size=10)
print(shm._fd)
print(os.fstat(shm._fd))
print(fcntl.fcntl(shm._fd, fcntl.F_GETPATH, s))