#!/usr/bin/env python2
# https://open.kattis.com/problems/reversebinary
print int(''.join(list(reversed(bin(input())[2:]))), 2)
