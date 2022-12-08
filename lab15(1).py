import tkinter as tk 
win=tk.Tk()
win.geometry("320x260") 
win['bg'] = "green"
file = open('report.txt', 'a', encoding='utf-8')
def func1():
    win['bg']= L1['bg']
    file.write("red, ")
def func2():
    win['bg'] = L2['bg']
    file.write('orange, ')
def func3():
    win['bg'] = L3['bg']
    file.write("yellow, ")
def func4():
    win['bg'] = L4['bg']
    file.write("green, ")
def func5():
    win['bg'] = L5['bg']
    file.write("cyan, ")
def func6():
    win['bg'] = L6['bg']
    file.write("blue, ")
def func7():
    win['bg'] = L7['bg']
    file.write("violet, ")
L1 = tk.Button(text="red",width=10, height=1, background="red", foreground= "white", command=func1) 
L2 = tk.Button(text="orange", width=10, height= 1, background="orange", foreground= "white", command=func2)
L3 = tk.Button(text="yellow", width=10, height= 1,background="yellow", foreground= "red", command=func3)
L4 = tk.Button(text="green", width=10, height= 1,background="green", foreground= "white", command=func4)
L5 = tk.Button(text="cyan", width=10, height= 1,background="cyan", foreground= "red", command=func5)
L6 = tk.Button(text="blue", width=10, height= 1,background="blue", foreground= "white", command=func6)
L7 = tk.Button(text="violet", width=10, height= 1,background="violet", foreground= "white", command=func7)
L1.pack()
L2.pack()
L3.pack()
L4.pack()
L5.pack()
L6.pack()
L7.pack()
win.mainloop()