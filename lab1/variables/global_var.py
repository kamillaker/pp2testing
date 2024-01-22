###
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
###



###
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()
###



###
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
###


###
x = "awesome"
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
###

