import random
import time
import tkinter as tk


def getProblem(add_min=(2, 2), add_max=(100, 100), mul_min=(2, 2), mul_max=(12, 100)):

    operation = random.randint(0, 3)

    if operation < 2:
        int1 = random.randint(add_min[0], add_max[0])
        int2 = random.randint(add_min[1], add_max[1])
        if operation == 1:
            display = (str(int1) + " + " + str(int2))
            sol = int1 + int2
        else:
            display = (str(max(int1, int2)) + " - " + str(min(int1, int2)))
            sol = max(int1, int2) - min(int1, int2)
    else:
        int1 = random.randint(mul_min[0], mul_max[0])
        int2 = random.randint(mul_min[1], mul_max[1])
        if operation == 2:
            display = (str(int1) + " x " + str(int2))
            sol = int1 * int2
        else:
            display = (str(int2 * int1) + " ÷ " + str(int1))
            sol = int2
    return (display, sol)



def main():
    start[0] = time.time()

    target[0] = targetVar.get()

    TargetLabel.pack_forget()
    restart.pack_forget()
    SetTarget.pack_forget()
    finishedLabel.pack_forget()
    restart.pack_forget()

    curSolvedInt[0] = 0

    curSolved.set("Score: " + str(curSolvedInt[0]))

    curProblemLabel.pack()
    text.pack()
    score.pack()

    run(0)


def run(solved):

    if solved == int(target[0]):
        totaltime = round((time.time() - start[0]), 2)
        end(totaltime)

    problem = getProblem()

    curProblem.set(problem[0] + " =")
    sol[0] = problem[1]


def check(event: tk.Event = None) -> None:
    if text.get().strip() == str(sol[0]):
        text.delete(0,3)
        curSolvedInt[0] += 1
        curSolved.set("Score: " + str(curSolvedInt[0]))
        run(curSolvedInt[0])


def Start():
    TargetLabel.pack()
    SetTarget.pack()
    restart.pack()


def end(totaltime):
    curProblemLabel.pack_forget()
    text.pack_forget()
    score.pack_forget()
    finished.set("Solved " + str(curSolvedInt[0]) + " problems in " + str(totaltime) + " seconds")
    finishedLabel.pack()
    TargetLabel.pack()
    SetTarget.pack()
    restart.pack()


#Start Time
start = [0]

#Create GUI
root = tk.Tk()
root.geometry("500x200")
root.maxsize(500, 200)

#Finish Game Stats
finished = tk.StringVar()
finishedLabel = tk.Label(root,textvariable=finished,font=("Adobe Garamond Pro",15))


#Restart Button
restart = tk.Button(root, text ="Start", command = main)


ans = tk.StringVar()
sol = [0]



#Current Problem Label
curProblem = tk.StringVar()
curProblem.set("Hello")
curProblemLabel = tk.Label(root,textvariable = curProblem,font=("Adobe Garamond Pro",15))

#Current Score Label
curSolved = tk.StringVar()
curSolvedInt = [0]
curSolved.set("Score: " + str(curSolvedInt[0]))
score = tk.Label(root,textvariable = curSolved,font=("Orator Std",10))

#Text Box
text = tk.Entry(root)
text.bind("<KeyRelease>", check)

#Set Target
targetVar = tk.StringVar()
TargetLabel = tk.Label(root,text = "Set Target:",font=("Adobe Garamond Pro",12))
SetTarget = tk.Entry(root,text="Target Problems Solved: ", textvariable = targetVar)
target = [0]




Start()

root.mainloop()
