import tkinter.messagebox, socket
from pymongo import MongoClient
class  client_cript:
    def __init__(self):
        self.cluster = MongoClient("") #Add your cluster here
        self.database_name = "" #Add your database name here
        self.collection_name = "" #Add your database collection name here
        self.db = self.cluster[self.database_name]
        self.collection = self.db[self.collection_name]
        self.ip = socket.gethostbyname(socket.gethostname())
        found = self.collection.find_one({"device": f"{self.ip}"})
        if found == None:
            print(self.ip)
            tkinter.messagebox.showerror("membership", f"{self.ip}")
            exit()
        else:
            print(self.ip)
            input("exit: ")
if __name__ == "__main__":
    client_cript()