#!/usr/bin/env python3

def hello_world(name):
  message = f"Hello, {name}"
  print(message)
  return message

returned_value = hello_world('John')
print(f"the returned value is '{returned_value}'")