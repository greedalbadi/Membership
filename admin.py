from tkinter import *
import tkinter.messagebox, datetime
from pymongo import MongoClient
class admin_main:
    def __init__(self):
        def f1():
            admin_main.add_device(self)
        def f2():
            admin_main.remove_device(self)
        def f3():
            admin_main.remove_all_devices(self)
        self.cluster = MongoClient("")#Add your cluster here
        self.database_name = ""#Add your database name here
        self.collection_name = ""#Add your database collection name here
        self.db = self.cluster[self.database_name]
        self.collection = self.db[self.collection_name]
        self.root = Tk()
        self.root.title("Membership")
        self.root.configure(bg="black")
        self.root.geometry('250x230')
        self.ip_input = Entry(self.root, width=22)
        self.b1 = Button(self.root, text='Activate',foreground='green', width=18, bg="black", command=f1)
        self.b2 = Button(self.root, text='Deactivate', foreground='red', width=18, bg="black", command=f2)
        self.b3 = Button(self.root, text='Deactivate All', foreground='purple', width=18, bg="black", command=f3)
        self.ip_input.place(x=55, y=70)
        self.b1.place(x=55, y=100)
        self.b2.place(x=55, y=130)
        self.b3.place(x=55, y=160)
        self.root.mainloop()
    def add_device(self):
            try:
                found = self.collection.find_one({"device": self.ip_input.get()})
                if found == None:
                    data = {"device": self.ip_input.get()}
                    self.collection.insert_one(data)
                    tkinter.messagebox.showinfo("membership", f"Device activated {self.ip_input.get()}")
                else:
                    tkinter.messagebox.showerror("membership", "This Device is already activated")
            except Exception as e:
                tkinter.messagebox.showerror("membership", f"Adding error: {e}")
    def save_data(self):
        file = open(f"{self.ip_input.get()}.txt", "w")
        date = datetime.datetime.now()
        data = f"date: {date}\nip: {self.ip_input.get()}"
        file.write(data)
    def remove_device(self):
        found = self.collection.find_one({"device": self.ip_input.get()})
        if found == None:
            tkinter.messagebox.showerror("membership", f"{self.ip_input.get()} Device does not exist in the database")
        else:
            try:
                s = self.collection.delete_many({"_id": found["_id"]})
                print(s)
                tkinter.messagebox.showinfo("membership", f"Device removed {self.ip_input.get()}")
            except Exception as e:
                tkinter.messagebox.showerror("membership", f"Deleting error: {e}")
    def remove_all_devices(self):
        try:
            res = tkinter.messagebox.askquestion("database", "Are you sure you want deactivate all devices ")
            if res == "yes":
                self.collection.delete_many({})
                tkinter.messagebox.showinfo("database", "you deactivated all devices")
        except:
            tkinter.messagebox.showerror("database", "clearing error")

if __name__ == '__main__':
    admin_main()