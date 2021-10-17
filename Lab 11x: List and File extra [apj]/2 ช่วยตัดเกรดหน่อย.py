def grader(x, avr, sd):
    if x >= avr + 1.0 * sd:
        return 'A'
    elif x >= avr + 0.5 * sd:
        return 'B'
    elif x >= avr - 0.5 * sd:
        return 'C'
    elif x >= avr - 1.0 * sd:
        return 'D'
    else:
        return 'F'

def func1(scores):
    arr = [s[1] for s in scores]
    avr = sum(arr)/len(arr)
    sd = (sum([(x - avr)**2 for x in arr])/(len(arr)-1))**(1/2)
    for s in scores:
        print(f'{s[0]} score: {s[1]} grade: {grader(s[1], avr, sd)}')


def func2(scores):
    maxx = max([s[1] for s in scores])
    print(f'Highest Score with the score of {maxx}:')
    for s in scores:
        if s[1] == maxx:
            print('-', s[0])

def get_score_from_file(filename) :
	lines = open(filename).readlines()
	score_list = [line.split(',') for line in lines]
	for i in range(len(score_list)) :
		score_list[i][1] = int(score_list[i][1])
	return score_list

scores = get_score_from_file('2.in')
func = input('Input function: ')
if func == '1' :
	func1(scores)
elif func == '2':
	func2(scores)