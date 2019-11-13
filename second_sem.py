from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector


#connecting to database
conn=mysql.connector.connect(
     host='localhost',
     user='root',
     passwd='root',
     database='student'
    )
#create cursor
c=conn.cursor()
#commit changes
conn.commit()
#close connection
conn.close()



#creating tkinter window
root=Tk()
root.geometry('800x700')
root.title('student data base')
root.config(bg='light blue')

#starting gui code
#creating frame
top_frame=Frame(root,padx=50,bg='light blue')
middle_frame=Frame(root,padx=10,pady=10,bg='light blue')
button_frame=Frame(root,padx=1,pady=40,bg='light blue')
combobox_frame=Frame(root,bg='black')
treeview_frame=Frame(root)
treeview_frame.place()
combobox_frame.place(x=610,y=82)


top_frame.pack()
middle_frame.place(x=20,y=60)
button_frame.place(x=60,y=320)

# creating combobox
combo=ttk.Combobox(combobox_frame)
combo['values'] = ('STUDENT_ID', 'STUDENT_NAME', 'ADDRESS','DEGREE','CONTACT_NO')
combo.set('STUDENT_ID')
combo.pack()
combo_degree=ttk.Combobox(middle_frame,width=33)
combo_degree['value']=('BSc hons Computing','BSc hons ethical hacking')
combo_degree.set('BSc hons ethical hacking')
combo_degree.grid(row=3, column=1)





#Inserting title in frame
top_lbl=Label(top_frame,text='SUTDENT DATA BASE',font='TimesNewRoman 21', bg='light blue',relief=RIDGE,bd=4)
top_lbl.pack()


#Creating label
lbl1=Label(middle_frame, text = 'STUDENT_ID',padx=15,font='TimesNewRoman 12 bold ',width=15, bg='light blue',relief=RIDGE)
lbl2=Label(middle_frame, text = 'STUDENT_NAME',padx=15,font='TimesNewRoman 12 bold',width=15, bg='light blue',relief=RIDGE)
lbl3=Label(middle_frame, text = 'ADDRESS',padx=15,font='TimesNewRoman 12 bold',width=15, bg='light blue',relief=RIDGE)
lbl4=Label(middle_frame, text = 'DEGREE',padx=15,font='TimesNewRoman 12 bold',width=15, bg='light blue',relief=RIDGE)
lbl5=Label(middle_frame, text = 'CONTACT_NO',padx=15,font='TimesNewRoman 12 bold',width=15, bg='light blue',relief=RIDGE)
combobox_label=Label(root, text = 'SORT_BY',font='TimesNewRoman 12 bold' ,bg='light blue',relief=RIDGE)
#griding label
lbl1.grid(row=0,column=0,padx=10,pady=10)
lbl2.grid(row=1,column=0,padx=10,pady=10)
lbl3.grid(row=2,column=0,padx=10,pady=10)
lbl4.grid(row=3,column=0,padx=10,pady=10)
lbl5.grid(row=4,column=0,padx=10,pady=10)
combobox_label.place(x=490,y=82)

#creating entry
entry1=Entry(middle_frame,font='TimesNewRoman 12 italic')
entry2=Entry(middle_frame,font='TimesNewRoman 12 italic')
entry3=Entry(middle_frame,font='TimesNewRoman 12 italic')
entry5=Entry(middle_frame,font='TimesNewRoman 12 italic')
search_entry=Entry(root,font='TimesNewRoman 12 italic',width=16)
#griding entry
entry1.grid(row=0, column=1,padx=20,ipadx=20)
entry2.grid(row=1, column=1,padx=20,ipadx=20)
entry3.grid(row=2, column=1,padx=20,ipadx=20)
entry5.grid(row=4, column=1,padx=20,ipadx=20)
search_entry.place(x=600,y=200)
#creating function
def ADD_info():
    try:
        # connecting to database
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='student'
        )
        STUDENT_ID = entry1.get()
        STUDENT_NAME = entry2.get()
        ADDRESS = entry3.get()
        DEGREE = combo_degree.get()
        CONTACT_NO = entry5.get()
        # create cursor
        c = conn.cursor()

        query = 'insert into tbl_student(student_id,studnet_name,address,degree, contact_number) values(%s, %s, %s,%s, %s)'
        values = (STUDENT_ID, STUDENT_NAME, ADDRESS, DEGREE, CONTACT_NO)
        c.execute(query, values)
        # commit changes
        conn.commit()

        SHOW_info()

        # close connection
        conn.close()
    except ValueError as error:
        print(error)

def clear_info():
    entry1.delete(0,END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    combo_degree.delete(0,END)
    entry5.delete(0, END)



def SHOW_info():
    try:
        # connecting to database
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='student'
        )
        # create cursor
        c = conn.cursor()
        # delete treeview data
        treeview_data = treeview.get_children()
        for i in treeview_data:
            treeview.delete(i)

        c.execute('SELECT * from tbl_student')
        records = c.fetchall()
        for record in records:
            treeview.insert('', 0, values=record)

        # commit changes
        conn.commit()
        # close connection
        conn.close()
        return
    except mysql.connector.Error as error:
        print(error)

def UPDATE_info():
    try:
        # connecting to database
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='student'
        )
        # create cursor
        c = conn.cursor()
        STUDENT_ID = entry1.get()
        STUDENT_NAME = entry2.get()
        ADDRESS = entry3.get()
        DEGREE = combo_degree.get()
        CONTACT_NO = entry5.get()
        query = 'update tbl_student set studnet_name=%s,address=%s,degree=%s,contact_number=%s where student_id=%s'
        values = (STUDENT_NAME, ADDRESS, DEGREE, CONTACT_NO, STUDENT_ID)
        c.execute(query, values)
        # commit changes
        conn.commit()
        clear_info()
        SHOW_info()
        # close connection
        conn.close()
        return

    except ValueError as error:
        print(error)

    except mysql.connector.Error as error:
        print(error)

def DELETE_info():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='student'
        )
        # create cursor
        c = conn.cursor()
        query = 'delete from tbl_student where student_id=%s'
        values = (pointer(),)
        c.execute(query, values)
        # commit changes
        conn.commit()
        # close connection
        conn.close()
        SHOW_info()
        clear_info()

        return

    except mysql.connector.Error as error:
        print(error)


def pointer():
    try:
        clear_info()
        point = treeview.focus()
        content = treeview.item(point)
        row = content['values']
        entry1.insert(0, row[0])
        entry2.insert(0, row[1])
        entry3.insert(0, row[2])
        combo_degree.insert(0, row[3])
        entry5.insert(0, row[4])
        return row[0]
    except IndexError:
        pass


def bubble_sort(alist):
    order = combo.get()
    print(order)
    if order == 'STUDENT_ID':
        column = 0
    elif order == 'STUDENT_NAME':
        column = 1
    elif order == 'ADDRESS':
        column = 2
    elif order == 'DEGREE':
        column = 3
    else:
        column = 4

    for i in range(len(alist) - 1, 0, -1):
        for j in range(0, i):
            if alist[j + 1][column] > alist[j][column]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]

    return alist


def sort():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='student'
        )
        # create cursor
        c = conn.cursor()
        query = 'select * from tbl_student'
        c.execute(query)
        result = c.fetchall()

        bubble_sort(result)

        treeview.delete(*treeview.get_children())

        for row in result:
            treeview.insert('', 0, value=row)

    except mysql.connector.Error as error:
        print(error)


def SEARCH_info(list=None):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='student'
        )
        # create cursor
        c = conn.cursor()

        if not list:
            query = 'select * from tbl_student'
            c.execute(query)
            result = c.fetchall()
        else:
            result = list

        target = search_entry.get()
        list_of_found_item = []
        for item in result:
            if target in item:
                list_of_found_item.append(item)

        treeview.delete(*treeview.get_children())

        for row in list_of_found_item:
            treeview.insert('', 0, value=row)

        if not list_of_found_item:
            messagebox.showinfo('Not found', "Student is not found.")

        return list_of_found_item

    except mysql.connector.Error as error:
        print(error)


# creating buttons
add_button = Button(button_frame,text='ADD',padx=5,font='TimesNewRoman 12',width=8,command=ADD_info)
show_button = Button(button_frame,text='SHOW',padx=5,font='TimesNewRoman 12',width=8,command=SHOW_info)
update_button = Button(button_frame,text='UPDATE',padx=5,font='TimesNewRoman 12',width=8,command=UPDATE_info)
delete_button = Button(button_frame,text='DELETE',padx=5,font='TimesNewRoman 12',width=8,command=DELETE_info)
search_button = Button(root,text='SEARCH',padx=5,font='TimesNewRoman 10',width=8,command=SEARCH_info)
clear_button = Button(button_frame,text='clear',padx=5,font='TimesNewRoman 12',width=8,command=clear_info)
sort_btn = Button(root,text='SORT',padx=5,font='TimesNewRoman 10',width=8,command=sort)

# griding buttons
add_button.grid(row=0, column=0,padx=10,ipadx=15)
show_button.grid(row=0, column=1,padx=10,ipadx=15)
update_button.grid(row=0, column=2,padx=10,ipadx=15)
delete_button.grid(row=0, column=3,padx=10,ipadx=15)
clear_button.grid(row=0, column=4,padx=10,ipadx=15)
search_button.place(x=490,y=200)
sort_btn.place(x=490,y=140)

# creating a treeview
treeview = ttk.Treeview(root,column=('student_id','student_name','address','degree','contact_no'))
treeview.place(x=70,y=400,width=680,height=240)

# heading of column
treeview.heading('student_id', text='student_id')
treeview.heading('student_name', text='student_name')
treeview.heading('address', text='address')
treeview.heading('degree', text='degree')
treeview.heading('contact_no', text='contact_no')

treeview.column('#0',width=20)
treeview.column('student_id', width=10,anchor='center')
treeview.column('student_name', width=30,anchor='center')
treeview.column('address', width=30,anchor='center')
treeview.column('degree', width=30,anchor='center')
treeview.column('contact_no', width=30,anchor='center')
treeview['show']='headings'
treeview.bind('<ButtonRelease-1>', lambda e: pointer())


if __name__ == '__main__':
    root.mainloop()
