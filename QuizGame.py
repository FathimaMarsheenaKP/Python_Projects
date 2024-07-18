print('Welcome To My Computer Quiz!')
print()
playing = input('Do you want to play? ')


if playing.lower() != 'yes':
    quit()


print("Okay! Let's play:)")
score = 0


answer = input("What does CPU stands for? ")
if answer.lower() == 'central processing unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
print()


answer = input("What does GPU stands for? ")
if answer.lower() == 'graphics processing unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
print()


answer = input("What does RAM stands for? ").lower()
if answer == 'random access memory':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
print()


answer = input("What does ROM stands for? ")
if answer.lower() == 'read only memory':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
print()
print()

print("You got " +str(score)+ " questions correct!")
print("You got " +str((score / 4)* 100) + "%.")