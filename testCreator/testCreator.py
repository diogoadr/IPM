import random

file = open("questions.txt", "r")

lines = []

for line in file:
    lines.append(line[:len(line)-1])

file.close()

answer = 0

while answer != 5:
    i = 1
    num = random.randrange(0,19)*5
    print(lines[num])
    
    while lines[num+i][2] != "!":
        print(lines[num+i][3:])
        i += 1
        
    right = i

    while i <= 4:
        print(lines[num+i][3:])
        i += 1

    print('Enter your answer:')
    answer = int(input())

    if(answer != right):
        print(f"WRONG ANSWER! {right}")
    else:
        print("well done!")

