class flashcards:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word+'('+self.meaning+')'
flash=[]
print("Welcome to flashcard application")
while(True):
    word=input("enter the word you want to add to your flashcard:")
    meaning=input("Enter the meaning of the word:")
    flash.append(flashcards(word,meaning))
    option=int(input("enter 0,if you want to add another flashcard otherwise enter 1 :"))
    if(option):
        break
print("\n Your flashcards")
for i in flash:
    print(i)