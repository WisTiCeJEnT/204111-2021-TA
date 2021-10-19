msg = input('What is your message? ')
print('\n'.join([i*' ' + msg[i] for i in range(len(msg))]))