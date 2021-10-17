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


count = [0, 0, 0]
n = int(input('N: '))
for i in range(n):
    a = int(input(f'Order {i+1} A: '))
    b = int(input(f'Order {i+1} B: '))
    c = int(input(f'Order {i+1} C: '))
    box = select_box([a, b, c])
    if box != -1:
        print(f'Box size {box+1}')
        count[box] += 1
    else:
        print('Oversize product')
for i in range(3):
    print(f'Use Box size {i+1}: {count[i]}')
