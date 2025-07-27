import random
class FruitQuiz:
    def __init__(self):
        self.fruits={'apple':'red',
                     'orange':'orange',
                     'watermelon':'green',
                     'banana':'yellow'}
    def quiz(self):
        while (True):
            fruit,color=random.choice(list(self.fruits.items()))
            print("What is the color of {}".format(fruit))
            user_anwser=input()
            if(user_anwser.lower()==color):
                print("Correct anwser")
            else:
                print("Wrong answer")
            option=int(input("enter 0 if you wnat to play otherwise enter 1:"))
            if(option):
                break
print("Welcome to the fruit quiz!")
fq=FruitQuiz()
fq.quiz()
