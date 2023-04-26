import tkinter
from tkinter import *

todo=Tk()
todo.title("To-Do-List App") 
todo.geometry("400x650+400+100")
todo.resizable(False,False)

task_list=[]
def addTask():
    task=task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task )
def deleteTask():
      global task_list
      task=str(listbox.get(ANCHOR))
      if task in task_list:
          task_list.remove(task)
          with open("tasklist.txt",'w')as taskfie:
              for task in task_list:
                  taskfie.write(task+"\n")
          listbox.delete(ANCHOR)
def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt","r")as taskfile:
             tasks=taskfile.readlines()
        for task in tasks:
            if task !='\n':
                task_list.append(task)
                listbox.insert(END, task)
    except:
        file=open('tasklist.txt','w')
        file.close()
#toplabel
toplabel=Label(todo,text="TO-DO-LIST",font="arial 20 bold",bg="#45e22a",width=390)
toplabel.pack()
#main
frame=Frame(todo,width=400,height=50,bg="white")
frame.place(x=0,y=180)

task=StringVar()
task_entry=Entry(frame,width=18,font="serif 20",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

button=Button(frame,text="ADD",font="elephant 14 bold",width=6,bg="#5a95ff",fg="#fff",bd=0,command=addTask)
button.place(x=300,y=0)

#listbox
frame1=Frame(todo,bd=3,width=700,height=200,bg="#32005b")
frame1.pack(pady=(195,0))

listbox=Listbox(frame1,font="arial 12",width=40,height=16,bg="#ac343b",fg="white",cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT,fill=BOTH,padx=2)

openTaskFile()

#scrollbars
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

#delete
bottomframe=Frame(todo,width=390,height=60)
bottomframe.pack(side=BOTTOM)
button=Button(bottomframe,text="DELETE",font="elephant 14",width=10,bg="red",fg="#fff",command=deleteTask)
button.pack(side=BOTTOM,pady=13)
  
todo.mainloop()
