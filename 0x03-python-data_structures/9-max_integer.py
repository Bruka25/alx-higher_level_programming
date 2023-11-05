#!/usr/bin/python3
def max_integer(my_list=[]):

   if not my_list:
      return None

   max_num = my_list[0]
   #traverse through the list to find the biggest integer
   for x in my_list:
       if x > max_num:
           max_num = x
   
   return max_num
