from tkinter import *
from tkinter.ttk import *
from web_scraping import scraping 

window = Tk()
window.title('Product Tracker') 
window.geometry('1920x1080') 

class gui_maker():

    def add(self):
        website = my_combobox.get()
        url = url_entry.get()
        sc = scraping()
        title, price = sc.get_details(url, website)
        
    def show_data(self):
        

    def add_window(self):
        add_window = Tk()
        add_window.title('Add')
        add_window.geometry('1920x1080')

        lbl_url = Label(add_window, text='Enter URL', font=(40))
        lbl_combo = Label(add_window, text='Select Website', font=(40))
        global url_entry
        url_entry = Entry(add_window, textvariable=StringVar(), width=50, font=(40))
        lbl_url.place(x=500, y=300)
        
        url_entry.place(x=600, y=300)
        lbl_combo.place(x=590, y=400)
        global my_combobox
        my_combobox = Combobox(add_window, textvariable = StringVar(),  font=(40),
                                values=["Amazon", "Flipkart", "Shopclues", "Alibaba"], state='readonly')
        my_combobox.place(x=730, y=400)
        my_combobox.current(0)

        Button(add_window, text='ADD PRODUCT', width=30, command=lambda : self.add()).place(x=650, y=500)
        Button(add_window, text='BACK', width=30, command=lambda : self.add()).place(x=650, y=550)
        add_window.mainloop()
        

f = gui_maker()
b1 = Button(window, text='Add',  width=30,command=lambda: f.add_window())
b1.place(x=650, y=400)
b2 = Button(window, text='Fetch',  width=30)
b2.place(x=650, y=200)
b3 = Button(window, text='Delete',  width=30)
b3.place(x=650, y=150)
window.mainloop()  