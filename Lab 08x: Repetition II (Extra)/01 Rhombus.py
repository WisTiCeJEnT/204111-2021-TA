"""
input: 7
   #
  ###
 #####
#######
 #####
  ###
   # 
"""
n = int(input('input: '))
for i in range(0, n, 2):
    print(' '*((n+1)//2-i//2-1) + '#'*(i+1))
for i in range(1, n//2+1):
    print(' '*(i) + '#'*(n-(i*2)))