from math import *
import copy
import itertools
import bisect
import sys
from heapq import heapify, heappop, heappush
from collections import deque

import os

import sys

from io import BytesIO, IOBase
BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
# input = lambda: sys.stdin.readline().rstrip("\r\n")
# sys.setrecursionlimit(3*10**5)
input = lambda: sys.stdin.readline().rstrip("\r\n")

def  countSetBits(n):
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count

def ilst():
    return list(map(int,input().split()))
    
def islst():
    return list(map(str,input().split()))
    
def inum():
    return map(int,input().split())
    
def freq(l):
    d = {}
    for i in l:
        d[i] = d.get(i,0)+1
    return d

def log(n, k):
    count = 0
    while n > 1 :
        count+= 1 
        n = n//k
    return count
    
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
mod = 10**9+7
for _ in range(int(input())):
    n = int(input())
    string = input()
    count = 1
    for i in range(2, n, 2):
        a = 0
        if int(string[i-1])&int(string[i-2]) == int(string[i]):
            a += 1
        if int(string[i-1])|int(string[i-2]) == int(string[i]):
            a += 1 
        if int(string[i-1])^int(string[i-2]) == int(string[i]):
            a += 1
        count *= a
        count %= mod
    print(count)
