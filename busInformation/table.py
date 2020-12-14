import tkinter as tk
import addresrv
class Table(tk.Frame): 
      
    def __init__(self, connection, cursor, data, key, master=None): 
        tk.Frame.__init__(self, master)
        self.master = master
        self.data = data
        self.key = key
        self.connection = connection
        self.cursor = cursor
        self.total_rows = len(data)
        self.total_columns = len(data[0])
        self.createWidgets()
        
    def createWidgets(self):
        if self.key == 'bus':
            columns = ['bus number', 'driver', 'origin', 'destination', 'departure', 'arrival',
                        'capacity', 'occupied']
        if self.key == 'reservation':
            columns = ['reservation number', 'passenger name', 'bus number', 'seat number']
        count = 0
        width = {'bus':10, 'reservation':25}
        for i in columns:
            self.e = tk.Entry(self.master, width=width[self.key], fg='red', 
                               font=('Arial',16,'bold'))
            self.e.grid(row=0, column=count) 
            self.e.insert('end', i) 
            count += 1
        for i in range(self.total_rows):
        
            for j in range(self.total_columns):
                self.e = tk.Entry(self.master, width=width[self.key], fg='blue', 
                               font=('Arial',16,'bold'))
                self.e.grid(row=i+1, column=j) 
                self.e.insert('end', self.data[i][j])
            if self.key == 'bus':
                self.b = tk.Button(self.master, width=12, height=2)
                self.b["text"] = "Add Reservation"
                self.b["command"] = self.add_resrv
                self.b.grid(row=i+1, column=j+1) 
    
    def add_resrv(self):
        root2  = tk.Toplevel()
        root2.geometry("400x400")
        buildApp = addresrv.AddNewReservation(self.connection, self.cursor, master=root2)
        
def create_table(connection, cursor, data, key):
    if data == []:
        return 'no data to show'
    root = tk.Tk()
    root.geometry("1200x600")
    app = Table(connection, cursor, data, key, master=root)
    app.mainloop()

def destroy_table(app):
    app.master_destroy()
