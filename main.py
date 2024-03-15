from tkinter import messagebox as tkmb

import customtkinter
from icecream import ic

ic("Quizlet Initialized")


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.currentQuestiosn = 0

    def checkAnswer(self, answer):
        if answer == self.questions[self.currentQuestiosn][1]:
            self.score += 1
        self.currentQuestion += 1

    def isFinished(self):
        return self.currentQuestion >= len(self.questions)


class QuizApp:
    def __init__(self, master):
        self.master = master
        self.quiz = Quiz(
            questions=[
                ("How to do simple maths", "I dont know"),
                ("What is the capital of France", "Paris"),
            ]
        )
        self.questionLabel = customtkinter.CTkLabel(master)
        self.questionLabel.pack()
        self.answerEntry = customtkinter.CTkEntry(master)
        self.answerEntry.pack()
        self.checkButton = customtkinter.CTkButton(master, text="Check answer")
        self.checkButton.pack()

    def askQuestion(self):
        if self.quiz.isFinished():
            tkmb.showinfo(
                title="Quiz Finished", message=f"You scored: {self.quiz.score}"
            )
            self.master.quit()
        else:
            self.questionLabel.configure(
                text=self.quiz.questions[self.quiz.currentQuestiosn][0]
            )
            self.answerEntry.delete(0, customtkinter.END)

    def checkAnswer(self):
        self.quiz.checkAnswer(self.answerEntry.get())
        self.askQuestion()


if __name__ == "__main__":
    master = customtkinter.CTk()
    quizApp = QuizApp(master)
    master.mainloop()
