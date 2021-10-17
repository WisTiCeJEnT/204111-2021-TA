import numpy as np
def up(n):
    print('\n'.join([' '*(n-i-1)+'+'*(i*2+1) for i in range(n)] + [(' '*(n-1)+'+')]*n))

def down(n):
    print('\n'.join(([' '*(n-i-1)+'+'*(i*2+1) for i in range(n)] + [(' '*(n-1)+'+')]*n)[::-1]))
    
def left(n):
    print('\n'.join([''.join(ll) for ll in [list(l) for l in np.array([list(l+' '*(2*n-len(l))) for l in ([' '*(n-i-1)+'+'*(i*2+1) for i in range(n)] + [(' '*(n-1)+'+')]*n)], dtype=object).T]]))

def right(n):
    print('\n'.join([''.join(ll) for ll in [list(l) for l in np.array([list(l+' '*(2*n-len(l))) for l in ([' '*(n-i-1)+'+'*(i*2+1) for i in range(n)] + [(' '*(n-1)+'+')]*n)[::-1]], dtype=object).T]]))

