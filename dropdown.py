#from graphs import close_, high_, low_, open_
from tkinter import *
import re
def dropdown_stock():
    option = ''
    root = Tk()
    root.title('Choose a Stock')
    root.geometry('500x500')
    def show():
        input_label = Label(root, text=clicked.get()).pack()
    stocks_list = ['TCS',
                'TECHM',
                'LTI',
                'INFY',
                'HCLTECH',
                'REDINGTON',
                'MINDTREE',
                'QUESS',
                'WIPRO',
                'MPHASIS']
    clicked = StringVar(root)
    clicked.set(stocks_list[0])
    #global company
    attributes = ['Open',
                  'Close',
                  'High',
                  'Low',
                  'Volume',
                  'All']
    attribute_clicked = StringVar(root)
    attribute_clicked.set(attributes[0])

    def choosen(value):
        global option
        option = value
       #root.destroy()
    attribute = attribute_clicked.get()
    company = clicked.get()
    '''def choose_graph(attribute,company):
        if attribute == 'Open':
            open_(company)
        elif attribute == 'Close':
            close_(company)
        elif attribute == 'High':
            high_(company)
        else:
            low_(company)'''
    def done(values):
        _ = values
        root.destroy()
    drop = OptionMenu(root, clicked, *stocks_list,command = choosen )
    drop.pack()
    #input_button = Button(root, text='Show Selection', command = show).pack()
    #drop.bind('<Return>', (lambda close: root.destroy()))
    drop2 = OptionMenu(root,attribute_clicked,*attributes, '''command = done''')
    drop2.pack()
# trying a slider to get number of days
    '''def slider_input():
        return val.get()
    val = IntVar()
    hor_slider = Scale(root,variable = val ,from_ = 0, to_ = 200, orient = HORIZONTAL)
    hor_slider.pack()
    days_input = slider_input()'''



    dayss = StringVar()
    e = Entry(root, width = 50,textvariable=dayss)
    e.pack()
    e.focus_set()
    e.insert(0, 'Enter the number of days: ')
    def input_click():
        input_label = Label(root, text = e.get())
        input_label.pack()
    input_button = Button(root, text = 'Enter the number of days', command = input_click)
    input_button.pack()
    e.bind('<Return>',(lambda event: root.destroy() ))
    root.mainloop()
    for_days = dayss.get()
    for_days = re.findall('\s+[0-9]+',for_days)
    for_days = for_days[0].lstrip()

    root.mainloop()
    return clicked.get(), attribute_clicked.get(), for_days

'''from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
def plot():
    fig = Figure(figsize = (5,5), dpi = 100)
    company = dropdown_stock()
    y = open_(company)'''
'''e = Entry(root,width = 50)
e.pack()
e.insert(0,"Enter the number of Days you want the predicted prices for: ")
e.get()
def days_input():
    input_days = Label(root, text = 'Stock prediction'+e.get())
    input_days.pack()
input_days_button = Button(root,text = 'Enter the number of days',command = days_input)'''
