import random

NUM_QUESTIONS = 53

file = open("questions.txt", "r")

lines = []

for line in file:
    lines.append(line[:len(line)-1])

file.close()

right = 0
answer = 0
score = 0
answered_questions = 0

while answer != 5:
    
    i = 1
    num = random.randrange(0,NUM_QUESTIONS-1)*5
    print(lines[num])

    # Generate and print the random list
    random_list = random.sample(range(1, 5), 4)

    for i in range(0, 4):
        # Print the possible answers randomly
        print(f"    {i+1}.{lines[num+random_list[i]][3:]}")
        
        # Saves the correct answer
        if lines[num+random_list[i]][2] == "!":
            right = i+1

    print('Enter your answer:')
    answer = int(input())

    if answer != right and answer != 5:
        print(f"WRONG ANSWER! {right}")
        answered_questions += 1
        
    elif answer == right:
        print("well done!")
        score += 1
        answered_questions += 1

print(f"Final Score: {score}/{answered_questions}")