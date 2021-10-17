inp = int(input())
m_s = 1
l = 0
s = 0
ans = inp
while(inp != 0):
    if inp == l:
        s += 1
    else:
        s = 1
    l = inp
    if s > m_s:
        m_s = s
        ans = l
    inp = int(input())
print(m_s)
print(ans)