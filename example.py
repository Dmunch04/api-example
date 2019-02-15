import sys
import os
import json

class ExampleFunctions (object):
  def __init__ (self, obj1, obj2, obj3, obj4):
    self.obj1 = obj1
    self.obj2 = obj2
    self.obj3 = obj3
    self.obj4 = obj4

  def __str__ (self):
    return '%s: %s: %s: %s:' % (self.obj1, self.obj2, self.obj3, self.obj4)
  
def returnResult (arg1, arg2, arg3, arg4):
  #result = []
  
  r = ExampleFunctions(int(arg1), int(arg2), int(arg3), int(arg4))
  
  #result.append(r)
  
  #return result
  return r

def getResult (arg1):
  if not arg1 >= 0:
    return
  
  #returnResult(int(arg1), int(arg1 + 1), int(arg1 + 2), int(arg1 + 3))
  data = [int(arg1), int(arg1+1), int(arg1+2), int(arg1+3)]
  return data
  
def get (arg):
  result = getResult(arg)
  return returnResult(result[0], result[1], result[2], result[3])
