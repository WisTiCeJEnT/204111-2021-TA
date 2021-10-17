def select_box(p):
    D = [
        [15, 10, 8],
        [25, 15, 12],
        [50, 40, 20]
    ]
    for di in range(len(D)):
        d = D[di]
        if all([p[i] <= d[i] for i in range(3)]):
            return di
    return -1
a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))
box = select_box([a, b, c])
if box != -1:
    print(f'Box size {box+1}')
else:
    print('Oversize product')
