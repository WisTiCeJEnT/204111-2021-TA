inp = input('Enter a number (to stop, just [Enter]): ')
if inp == '':
  print('Nothing to do.')
else:
  inp = float(inp)
  mx = inp
  mn = inp
  sm = 0
  count = 0
  while(inp != ''):
    inp = float(inp)
    mx = max(mx, inp)
    mn = min(mn, inp)
    sm += inp
    count += 1
    inp = input('Enter a number (to stop, just [Enter]): ')
    if inp == '':
      break
  print(f"Maximum is {mx:.2f}")
  print(f"Minimum is {mn:.2f}")
  print(f"Average is {sm/count:.2f}")
