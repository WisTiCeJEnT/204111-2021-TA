# Ex1
seq = [1,3,2,6]
seq2 = [x*3 for x in seq]

# Ex2
c_list = [-40,0,20,37,40,100]
f_list = [9*c/5+32 for c in c_list]

# Ex3
N = 20
s = [x for x in range(1, N+1) if (x%2==1 and x%5!=0)]

# Ex4
def f(n):
    return sum([(2*i+5)**2 for i in range(1, n+1)])
f(1)
f(5)
f(10)

# Ex5
nums = [i for i in range(1, 100) if (i%5 == 0 or i%7 == 0)]