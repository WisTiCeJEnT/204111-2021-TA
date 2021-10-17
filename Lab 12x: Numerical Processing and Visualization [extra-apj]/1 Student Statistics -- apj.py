import numpy as np

def read_file(filename):
    # return 2D array
    print('Reading data from', filename)
    return np.loadtxt(filename, delimiter=',')

def query_score(table):
    print(f'Found scores of {table.shape[0]} student(s) on {table.shape[1]} subject(s)')
    std = int(input('Enter student no.: '))
    sbj = int(input('Enter subject no.: '))
    print(f"Student #{std}'s score on subject #{sbj} is {table[std-1][sbj-1]:.1f}")

def print_fails(table):
    nrows,ncols = table.shape
    for r in range(nrows):
        for c in range(ncols):
            if table[r][c] < 50:
                print(f'Student #{r+1} fails subject #{c+1} with score {table[r][c]:.1f}')

def print_student_summary(table):
    print('Student Summary')
    print('===============')
    for i in range(len(table)):
        print(f'Total score for student #{i+1}: {sum(table[i]):.0f}')

def print_subject_summary(table):
    print('Subject Summary')
    print('===============')
    for i in range(len(table.T)):
        print(f'Average score for subject #{i+1}: {sum(table.T[i])/len(table.T[i]):.2f}')


def query_student_mean(table):
    std = int(input('Enter student no.: '))
    print(f'Average score for student #{std} = {sum(table[std-1])/len(table[std-1]):.2f}')


filename = input("Enter filename: ")
table = read_file(filename)

while (True):
    print("1. Query score")
    print("2. Print failing students")
    print("3. Print student summary")
    print("4. Print subject summary")
    print("5. Query student mean")
    print("6. Quit")
    choice = int(input("Enter choice: "))
    if (choice == 6):
        break
    elif (choice == 1):
        query_score(table)
    elif (choice == 2):
        print_fails(table)
    elif (choice == 3):
        print_student_summary(table)
    elif (choice == 4):
        print_subject_summary(table)
    elif (choice == 5):
        query_student_mean(table)