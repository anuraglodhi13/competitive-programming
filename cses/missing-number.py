#!/usr/bin/env python2
n = input()
print n * (n + 1) / 2 - sum(map(int, raw_input().split()))
