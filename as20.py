What is the difference between range and xrange function?
range() and xrange() are two functions that could be used to iterate a certain number of times in for loops in Python.
 In Python 3, there is no xrange , but the range function behaves like xrange in Python 2.
 If you want to write code that will run on both Python 2 and Python 3, you should use range().

range() – This returns a list of numbers created using range() function.

xrange() – This function returns the generator object that can be used to display numbers only by looping. 
Only particular range is displayed on demand and hence called “lazy evaluation“.
