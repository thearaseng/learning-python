#!/usr/bin/env python3

print(2 in [4, 7, 2])
print(2 not in [4, 7, 2])

if 1 == 1:
  print('this is true')
  print('it is still in the code block')

name = 'Kevin'
if len(name) >= 6:
  print('name is long')
elif len(name) == 5:
  print('name is 5 characters')
else:
  print('name is short')

if False:
  print('was true')
else:
  print('was false')