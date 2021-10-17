from bs4 import BeautifulSoup
import os


f = open(input('filename: ')).read()
# f = open('7.html').read()
soup = BeautifulSoup(f, features='html.parser')
lab_title = soup.find(id='lab-title').find_all('div')
lab_title = lab_title[0].text.strip()+' '+lab_title[1].text.splitlines()[1].strip()
print(lab_title)
os.mkdir(lab_title)
tasks = soup.find_all('div', {'class': 'task'})
for task in tasks:
    task_name = task.find('span').text
    print(task_name)
    open(f'./{lab_title}/{task_name}.py', 'w')