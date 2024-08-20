heads = int(input('Enter the total number of heads:'))
legs = int(input('Enter the total number of legs:'))
if legs % 2 !=0 or heads == 0 or heads > legs:
   print('No solution')
else:  
   r = int((legs + (-2*heads))/2)
   c = int(heads - r)
   print(c,r)