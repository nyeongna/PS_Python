# -*- coding: utf-8 -*-

import sys

n, m = map(int, input().split())
# input() 보다 sys.stdin.readline()이 더 빠르다.
num_list = list(map(int, sys.stdin.readline().split()))
psum_list = [0]*(n+1)

for i in range(n):
    psum_list[i+1] = psum_list[i] + num_list[i]

while m > 0:
    m=m-1
    start, end = map(int, sys.stdin.readline().split())
    start, end = start-1, end-1
    print(psum_list[end+1] - psum_list[start])
