"""
 user : 'postgres',
    host : 'localhost',
    password : 'postgres',
    database : 'typescriptdatabase',
    port : 5432
"""

from tkinter import Tk, Canvas, Frame, Label, Entry, Button, W , E, Listbox, END
import psycopg2

root = Tk()
root.title("Python & PostgreSQL")

def save_new_student(nombre,edad,direccion):
    
    #print(nombre)

    conn = psycopg2.connect(dbname="tareas",
        user="postgres",
        password = "postgres", 
        host="localhost",
        port="5432")
    
    cursor = conn.cursor()
    query = '''INSERT INTO students (name,address, age) VALUES (%s,%s,%s)'''
    cursor.execute(query, (nombre,direccion,edad))
    print("Data Saved")
    conn.commit()
    conn.close()
    
def display_students():
    conn = psycopg2.connect(dbname="tareas",
        user="postgres",
        password = "postgres", 
        host="localhost",
        port="5432")
    
    cursor = conn.cursor()
    query = '''SELECT * FROM students'''
    cursor.execute(query)
    row = cursor.fetchall()

    listbox = Listbox(frame, width=20, height=5)
    listbox.grid(row=10, columnspan=4, sticky=W+E)

    for x in row:
        listbox.insert(END,x)


    conn.commit()
    conn.close()



# Canvas
canvas = Canvas(root,height=380,width=400)
canvas.pack()

frame = Frame()
frame.place(relx=0.1 , rely=0.1, relwidth=0.8, relheight=0.8)

label = Label(frame, text='Add a Student')
label.grid(row=0, column=1)

# NAME INPUT
label = Label(frame, text='Name')
label.grid(row=1, column=0)
entry_name = Entry(frame)
entry_name.grid(row=1,column=1)

# AGE INPUT
label = Label(frame, text='Age')
label.grid(row=2, column=0)
entry_age = Entry(frame)
entry_age.grid(row=2,column=1)

# Adress INPUT
label = Label(frame, text='Address')
label.grid(row=3, column=0)
entry_address = Entry(frame)
entry_address.grid(row=3,column=1)

# Button

button = Button(frame,text="Add", command=lambda:save_new_student(entry_name.get(),
    entry_age.get(),
    entry_address.get()))
button.grid(row=4,column=1, sticky=W+E)


# BUSCAR

display_students()

root.mainloop()