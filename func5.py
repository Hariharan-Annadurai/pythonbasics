def sum(*args):     ##*args as a parameter which allows us to pass variable length argument list to the sum() function
   '''Function returns the sum
   of all values'''
   r = 0
   for i in args:
      r += i
   return r
print(sum.__doc__)           ##  _doc_ is used to print the characters which is presented in the '''....'''
print(sum(1, 2, 3))
print(sum(1, 2, 3, 4, 5))
