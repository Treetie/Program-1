import tkinter as tk
import sys

#Score setup
programminglist = []
artlist = []
sciencelist = []
mathlist = []
historylist = []

programmingav = 0
artav = 0
scienceav = 0
mathav = 0
historyav = 0

numscores = 0
#Command setup (functions)

#Adds to the scores lists
def calculate():
    global numscores
    #checks for invalid inputs
    if programming.get() == "" or art.get == "" or science.get() == "" or math.get() == "" or history.get() == "":
        print("Please enter valid scores")
    elif (0 > float(programming.get()) or float(programming.get()) > 100) or (0 > float(art.get()) or float(art.get()) > 100) or (0 > float(science.get()) or float(science.get()) > 100) or (0 > float(math.get()) or float(math.get()) > 100) or (0 > float(history.get()) or float(history.get()) > 100):
        print("Please enter valid scores")
    else:
        programminglist.append(round(float(programming.get())))
        artlist.append(round(float(art.get())))
        sciencelist.append(round(float(science.get())))
        mathlist.append(round(float(math.get())))
        historylist.append(round(float(history.get())))
        numscores += 1
        average()

#clears textboxes
def clear():
    programming.delete("0","end")
    art.delete("0","end")
    science.delete("0","end")
    math.delete("0","end")
    history.delete("0","end")

#resets everything
def reset():
    global programminglist
    global artlist
    global sciencelist
    global mathlist
    global historylist
    global numscores
    global programmingav
    global artav
    global scienceav
    global mathav
    global historyav
    programminglist = []
    artlist = []
    sciencelist = []
    mathlist = []
    historylist = []
    numscores = 0
    programmingav = 0
    artav = 0
    scienceav = 0
    mathav = 0
    historyav = 0

#prints results
def printsum():
    global numscores
    #Programming
    label = tk.Label(root, text=f"Class Name: Programming")
    label.grid(row=0, column=1)

    label = tk.Label(root, text=f"# Scores Entered: {numscores}")
    label.grid(row=1, column=1)

    label = tk.Label(root, text=f"Current Average: {programmingav}")
    label.grid(row=2, column=1)

    label = tk.Label(root, text=f"High Score: {max(programminglist)}")
    label.grid(row=3, column=1)

    label = tk.Label(root, text=f"Low Score: {min(programminglist)}")
    label.grid(row=4, column=1)

    #Art
    label = tk.Label(root, text=f"Class Name: Art")
    label.grid(row=6, column=1)

    label = tk.Label(root, text=f"# Scores Entered: {numscores}")
    label.grid(row=7, column=1)

    label = tk.Label(root, text=f"Current Average: {artav}")
    label.grid(row=8, column=1)

    label = tk.Label(root, text=f"High Score: {max(artlist)}")
    label.grid(row=9, column=1)

    label = tk.Label(root, text=f"Low Score: {min(artlist)}")
    label.grid(row=10, column=1)

    #Science
    label = tk.Label(root, text=f"Class Name: Science")
    label.grid(row=2, column=2)

    label = tk.Label(root, text=f"# Scores Entered: {numscores}")
    label.grid(row=3, column=2)

    label = tk.Label(root, text=f"Current Average: {scienceav}")
    label.grid(row=4, column=2)

    label = tk.Label(root, text=f"High Score: {max(sciencelist)}")
    label.grid(row=5, column=2)

    label = tk.Label(root, text=f"Low Score: {min(sciencelist)}")
    label.grid(row=6, column=2)

    #Math
    label = tk.Label(root, text=f"Class Name: Math")
    label.grid(row=9, column=2)

    label = tk.Label(root, text=f"# Scores Entered: {numscores}")
    label.grid(row=10, column=2)

    label = tk.Label(root, text=f"Current Average: {mathav}")
    label.grid(row=11, column=2)

    label = tk.Label(root, text=f"High Score: {max(mathlist)}")
    label.grid(row=12, column=2)

    label = tk.Label(root, text=f"Low Score: {min(mathlist)}")
    label.grid(row=13, column=2)

    #History
    label = tk.Label(root, text=f"Class Name: History")
    label.grid(row=12, column=1)

    label = tk.Label(root, text=f"# Scores Entered: {numscores}")
    label.grid(row=13, column=1)

    label = tk.Label(root, text=f"Current Average: {historyav}")
    label.grid(row=14, column=1)

    label = tk.Label(root, text=f"High Score: {max(historylist)}")
    label.grid(row=15, column=1)

    label = tk.Label(root, text=f"Low Score: {min(historylist)}")
    label.grid(row=16, column=1)

#exits program
def exitcode():
    sys.exit(0)

#averages scores
def average():
    global programmingav
    global artav
    global scienceav
    global mathav
    global historyav
    programmingav = round(sum(programminglist)/len(programminglist))
    artav = round(sum(artlist)/len(artlist))
    scienceav = round(sum(sciencelist)/len(sciencelist))
    mathav = round(sum(mathlist)/len(mathlist))
    historyav = round(sum(historylist)/len(historylist))

#Screen setup
root = tk.Tk()
root.title("Owen Schmitz, 1375, Grade Program")

#Main label
label = tk.Label(root, text="Input scores below")
label.grid(row=0, column=0)

#Class labels + entries
label = tk.Label(root, text="Programming:")
label.grid(row=1, column=0)
programming = tk.Entry(root)
programming.grid(row=2, column=0)

label = tk.Label(root, text="Art:")
label.grid(row=3, column=0)
art = tk.Entry(root)
art.grid(row=4, column=0)

label = tk.Label(root, text="Science")
label.grid(row=5, column=0)
science = tk.Entry(root)
science.grid(row=6, column=0)

label = tk.Label(root, text="Math:")
label.grid(row=7, column=0)
math = tk.Entry(root)
math.grid(row=8, column=0)

label = tk.Label(root, text="History:")
label.grid(row=9, column=0)
history = tk.Entry(root)
history.grid(row=10, column=0)

#Calculate button
button = tk.Button(root, text="Calculate", command=calculate)
button.grid(row=11, column=0)

#Clear button
button = tk.Button(root, text="Clear", command=clear)
button.grid(row=12, column=0)

#Reset button
button = tk.Button(root, text="Reset", command=reset)
button.grid(row=13, column=0)

#Print Summary button
button = tk.Button(root, text="Print Summary", command=printsum)
button.grid(row=14, column=0)

#Exit button
button = tk.Button(root, text="Exit", command=exitcode)
button.grid(row=15, column=0)

root.mainloop()