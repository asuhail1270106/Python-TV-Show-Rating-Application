# Programmed by Abdullah Suhail
# tvApplication.py
# 04/21/2018
# ITMD 413 Spring 2018 - Final Project
# Professor James Papademas
# This program will allow users to view and rate television shows
# from a database called shows.db using a GUI interface

# the tkinter GUI toolkit allows for the creation of a GUI interface
# the messagebox module lets us create message boxes!
# import the myDatabase file to use the functions defined in it
# import the time module so you can get date and time
from tkinter import *
from tkinter import messagebox
from rating_chart import *
import time


# function that works with radio buttons to display confirmation message
def rating_desc():
    showrating = str(rating.get())  # grab rating showname based on user input and use it
    showratingint = 0
    if showrating == 'the greatest':
        showratingint = 5
    elif showrating == 'one of the best':
        showratingint = 4
    elif showrating == 'pretty amazing':
        showratingint = 3
    elif showrating == 'not bad':
        showratingint = 2
    elif showrating == 'sub par':
        showratingint = 1
    selection = ('So, you think this TV show is ' + showrating + '?')
    show_ratinglabel1.config(text=selection)
    show_ratinglabel1.pack(side=TOP)
    show_ratingavg.pack(side=BOTTOM)
    show_ratingavglabel1.pack(side=BOTTOM, fill=X)
    show_ratingavglabel.pack(side=BOTTOM, fill=X)
    updateShowrating(showratingint, showname)  # update function for show rating
    messagebox.showinfo('You Rated!',
                        'Thanks for rating ' + showname + '!\n'
                        'I appreciate your time in trying out my app!\n'
                        'Have a great day!')


# function to display information upon selection of a listbox item
def click(evt):
    global showname  # global variable that represents show name
    w = evt.widget
    index = int(w.curselection()[0])
    showname = str(w.get(index))
    show_descbox.delete(1.0, END)
    # not my finest moment, manually reshaping string to display show name w/out extra stuff
    HERE = str(selectShowdesc(showname))
    WE = HERE.replace('(', '')
    GO = WE.replace('\'', '')
    AGAIN = GO.replace(',', '')
    MAN = AGAIN.replace(')', '')
    desc = MAN.replace('\"', '')
    show_descbox.insert(END, desc)  # insert shownames into listbox
    # the following lines replace the show poster picture based on which show you're looking at
    show_image.configure(image='')
    var = showname
    image = PhotoImage(file=var + '.png')
    show_image.configure(image=image)
    show_image.image = image
    show_image.pack(side=TOP)
    # the radio buttons reset when you click on another show
    show_ratingbutton1.deselect()
    show_ratingbutton2.deselect()
    show_ratingbutton3.deselect()
    show_ratingbutton4.deselect()
    show_ratingbutton5.deselect()
    # remove the rating label when selecting new show
    show_ratinglabel1.pack_forget()


# function to remove file from cwd
def deleteFile(file):
    try:
        os.remove(file)
    except Error as e:
        print('Error with file: ', e)


# function to display shows from the DB in listbox
def setList():
    global contacts
    shows = selectShows()
    # Delete all elements from the listbox just in case
    show_name.delete(0, END)
    # Insert each name from the list to end of show_name listbox
    for name in shows:
        OH = str(name)
        MY = OH.replace('(', '')
        GOD = MY.replace('\'', '')
        SERIOUSLY = GOD.replace(',', '')
        KMN = SERIOUSLY.replace('\"', '')
        show = KMN.replace(')', '')
        show_name.insert(END, show)


# function that builds the tv application GUI interface
def buildFrame():
    # these variables are being used outside this function so they're global
    global show_name, show_descbox, show_image, show_ratinglabel, show_ratinglabel1, rating, show_ratingavg
    global show_ratingavglabel, show_ratingavglabel1
    global show_ratingbutton1, show_ratingbutton2, show_ratingbutton3, show_ratingbutton4, show_ratingbutton5
    root = Tk()
    # change window title
    root.title("Television Show Rating App")
    root.configure(background='#ECCBEE')
    root.minsize(1450, 680)
    # resize the window to a better fit in order to show all buttons

    # the following are frames that widgets will be put into
    topframe = Frame(root)
    topframe.pack(fill=X, pady=15)
    leftframe = Frame(root)
    leftframe.pack(side=LEFT, fill=BOTH, padx=25, pady=25)
    leftframe2 = Frame(root, width=675)
    leftframe2.pack(side=LEFT, fill=BOTH, padx=25, pady=25)
    rightframe = Frame(root)
    rightframe.pack(side=RIGHT, fill=BOTH, padx=25, pady=25)

    # TV app main label
    show_desclabel = Label(topframe, text="The TV Show Rating Application!!!", bg='#27E195', fg='black', font=('Book Antiqua', 35))
    show_desclabel.pack(fill=X)

    # list box items in leftframe
    scroll = Scrollbar(leftframe)
    scroll.pack(side=RIGHT, fill=Y)
    show_namelabel = Label(leftframe, text="TV Show List", bg='blue', fg='white', font=('Book Antiqua', 14))
    show_namelabel.pack(side=TOP, fill=X)
    show_name = Listbox(leftframe, yscrollcommand=scroll.set, font=('Nyala', 16), selectmode=SINGLE)
    show_name.config(width=0)
    show_name.bind('<<ListboxSelect>>', click)
    show_name.pack(side=LEFT, fill=BOTH, expand=TRUE)
    scroll.config(command=show_name.yview)

    # textbox and picture label that are both put into leftframe2
    show_desclabel = Label(leftframe2, text="TV Show Description", bg='red', fg='white', font=('Book Antiqua', 14))
    show_desclabel.pack(side=TOP, fill=X)
    show_descbox = Text(leftframe2, wrap=WORD, font=('Nyala', 16), height=10)
    show_descbox.pack(side=TOP, fill=X)
    show_imagelabel = Label(leftframe2, text="TV Show Poster",  bg='green', fg='white', font=('Book Antiqua', 14))
    show_imagelabel.pack(side=TOP, fill=X)
    image = PhotoImage(file='welcome.png')
    show_image = Label(leftframe2, image=image)
    show_image.image = image
    show_image.pack(side=TOP)

    # the radio buttons for rating shows are placed here in rightframe
    show_ratinglabel = Label(rightframe, width=25, text="TV Show Rating System", bg='orange', fg='white',
                             font=('Book Antiqua', 14))
    show_ratinglabel.pack(side=TOP, fill=X)
    rating = StringVar()
    show_ratingbutton1 = Radiobutton(rightframe, text="The Greatest!", variable=rating, value='the greatest',
                                     command=rating_desc, tristatevalue=0, font=('Nyala', 16))
    show_ratingbutton1.pack()
    show_ratingbutton2 = Radiobutton(rightframe, text="One of the best!", variable=rating, value='one of the best',
                                     command=rating_desc, tristatevalue=0, font=('Nyala', 16))
    show_ratingbutton2.pack()
    show_ratingbutton3 = Radiobutton(rightframe, text="Pretty Amazing!", variable=rating, value='pretty amazing',
                                     command=rating_desc, tristatevalue=0, font=('Nyala', 16))
    show_ratingbutton3.pack()
    show_ratingbutton4 = Radiobutton(rightframe, text="Not Bad.", variable=rating, value='not bad',
                                     command=rating_desc, tristatevalue=0, font=('Nyala', 16))
    show_ratingbutton4.pack()
    show_ratingbutton5 = Radiobutton(rightframe, text="Sub par.", variable=rating, value='sub par',
                                     command=rating_desc, tristatevalue=0, font=('Nyala', 16))
    show_ratingbutton5.pack()
    show_ratinglabel1 = Label(rightframe, fg='white', bg='#9F3CA4', font=('Book Antiqua', 11))

    show_ratingavglabel = Label(rightframe, fg='black', bg='#E1E153', text='Click for average show rating!',
                                font=('Book Antiqua', 14))
    show_ratingavglabel1 = Label(rightframe, fg='black', bg='#F9FF71', text='Chart will open in browser!',
                                font=('Book Antiqua', 13))
    show_ratingavg = Button(rightframe, fg='white', bg='#0C4946', text='Rating Average', font=('Nyala', 16),
                            command=displayRating)

    return root


# all functions are executed since this is the main py file
root = buildFrame()
createDB()
createTable()
insertShows()
setList()
root.mainloop()
deleteShows()
deleteFile('rating_chart.svg')

# After the loop has ended, auxiliary information is provided
print ("Abdullah Suhail, Final Project")
print (time.strftime("%m/%d/%Y"))
print (time.strftime("%I:%M:%S"))

