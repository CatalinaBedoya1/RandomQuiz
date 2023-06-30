from tkinter import *
import readquiz
import random

questions = readquiz.loadQuestions()
total = 0
correct = 0




def getNewQuestion():
    global total, correct
    total += 1
    question, answer = random.choice(questions)  
    questionLabel['text'] = question  
    if answer:
        yesButton["command"] = goodAnswer
        noButton["command"] = badAnswer
        scoreLabel+=1
    else:
        yesButton["command"] = badAnswer
        noButton["command"] = goodAnswer



def badAnswer():
    global total, correct
    correct += 0
    total += 1
    statusLabel['text'] = 'Your answer was incorrect'
    statusLabel['bg'] = 'pink'
    scoreLabel['text'] = 'Score: ' + str(correct) + '/' + str(total)
    getNewQuestion()

def goodAnswer():
    global total, correct
    correct += 1
    total += 1
    statusLabel['text'] = 'Your answer was correct'
    statusLabel['bg'] = 'light green'
    scoreLabel['text'] = 'Score: ' + str(correct) + '/' + str(total)
    getNewQuestion()


    

root = Tk()
root.title("It's Quiz time!")
questionFrame = Frame(root)
buttonFrame = Frame(root)
status = Frame(root)
status['bg'] = 'light green'


questionLabel = Message(root, width=300)
questionLabel.pack()
yesButton = Button(buttonFrame, text="Yes", command=goodAnswer)
yesButton.pack(side=LEFT)
noButton = Button(buttonFrame, text="No", command=badAnswer)
noButton.pack(side=LEFT)


statusLabel = Label(status, text="Status: ")
statusLabel.pack(side=LEFT)
scoreLabel = Label(status, text="Score: 0/0")
scoreLabel.pack(side=RIGHT)


questionFrame.pack()
buttonFrame.pack()
status.pack(side=BOTTOM, fill=Y)


getNewQuestion()


root.mainloop()
