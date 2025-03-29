def matrix(n=None, m=None, value=0):
  if n == None and m == None:
    return [[value]]
  elif m == None:
    return [[value] * n for i in range(n)]
  else:
    return [[value] * m for i in range(n)]