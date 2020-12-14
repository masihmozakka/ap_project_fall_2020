import tkinter as tk
import sqlite3
import db
import table
import addresrv

root = tk.Tk()
root.geometry("600x400")

class RemoveReservationApplication(tk.Frame):

    def __init__(self, connection, cursor, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.connection = connection
        self.cursor = cursor
        
    def createWidgets(self):
        vcmd = (self.register(self.on_validation_num),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.reservation = tk.Label(self, text="Reservation number: ")
        self.reservation.pack(side="top") 
        self.e_reservation = tk.Entry(self, validate="key", validatecommand=vcmd)
        self.e_reservation.pack(side="top")

        self.LOGIN = tk.Button(self, text = 'Submit', fg="green", command=self.setCredentials )
        self.LOGIN.pack(side="bottom")

        self.QUIT = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.QUIT.pack(side="bottom")

    def on_validation_num(self, d, i, P, s, S, v, V, W):
        # Disallow anything but numbers
        if S.isdigit():
            return True
        else:
            self.bell()
            return False
    
    def setCredentials(self):
        reservationnumber = self.e_reservation.get()
        db.remove_passenger_info(reservationnumber, self.cursor, self.connection)
        self.master.destroy()

class ShowSingleBusReservationApplication(tk.Frame):

    def __init__(self, connection, cursor, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.connection = connection
        self.cursor = cursor
        
    def createWidgets(self):
        vcmd = (self.register(self.on_validation_num),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.bus = tk.Label(self, text="bus number: ")
        self.bus.pack(side="top")
        self.e_bus = tk.Entry(self, validate="key", validatecommand=vcmd)
        self.e_bus.pack(side="top")
        bus = self.e_bus.get()

        self.LOGIN = tk.Button(self, text = 'Submit', fg="green", command=self.setCredentials )
        self.LOGIN.pack(side="bottom")

        self.QUIT = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.QUIT.pack(side="bottom")

    def on_validation_num(self, d, i, P, s, S, v, V, W):
        # Disallow anything but numbers
        if S.isdigit():
            return True
        else:
            self.bell()
            return False
    
    def setCredentials(self):
        businfo = self.e_bus.get()
        
        data = []
        temp = []
        for row in self.cursor.execute('SELECT * FROM reservationinfo WHERE busno=? ORDER BY reservationnumber', 
                                        (businfo,)):
            temp = []
            for i in row:
                temp.append(i)
            data.append(temp)
            
    
        table.create_table(self.connection, self.cursor, data,  key='reservation')
        self.master.destroy()

class RemoveBusApplication(tk.Frame):

    def __init__(self, connection, cursor, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.connection = connection
        self.cursor = cursor
        
    def createWidgets(self):
        vcmd = (self.register(self.on_validation_num),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.reservation = tk.Label(self, text="Bus number: ")
        self.reservation.pack(side="top") 
        self.e_reservation = tk.Entry(self, validate="key", validatecommand=vcmd)
        self.e_reservation.pack(side="top")

        self.LOGIN = tk.Button(self, text = 'Submit', fg="green", command=self.setCredentials )
        self.LOGIN.pack(side="bottom")

        self.QUIT = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.QUIT.pack(side="bottom")

    def on_validation_num(self, d, i, P, s, S, v, V, W):
        # Disallow anything but numbers
        if S.isdigit():
            return True
        else:
            self.bell()
            return False
    
    def setCredentials(self):
        reservationnumber = self.e_reservation.get()
        db.remove_bus_info(reservationnumber, self.cursor, self.connection)
        self.master.destroy()

class AddNewBusApplication(tk.Frame):

    def __init__(self, connection, cursor, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.connection = connection
        self.cursor = cursor
        
    def createWidgets(self):
        vcmd = (self.register(self.on_validation_num),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        vcma = (self.register(self.on_validation_alpha),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        
        vcmal = (self.register(self.on_validation_alnum),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        
        self.busno = tk.Label(self, text="Bus number: ")
        self.busno.pack(side="top") 
        self.e_busno = tk.Entry(self, validate="key", validatecommand=vcmd)
        self.e_busno.pack(side="top")

        self.drivername = tk.Label(self, text="Name of driver: ")
        self.drivername.pack(side="top")
        self.e_drivername = tk.Entry(self, validate="key", validatecommand=vcma)
        self.e_drivername.pack(side="top")

        self.departuretime = tk.Label(self, text="Departure time: ")
        self.departuretime.pack(side="top")
        self.e_departuretime = tk.Entry(self, validate="key", validatecommand=vcmal)
        self.e_departuretime.pack(side="top")

        self.arrivaltime = tk.Label(self, text="Arrival time: ")
        self.arrivaltime.pack(side="top")
        self.e_arrivaltime = tk.Entry(self, validate="key", validatecommand=vcmal)
        self.e_arrivaltime.pack(side="top")

        self.origin = tk.Label(self, text="Origin: ")
        self.origin.pack(side="top")
        self.e_origin = tk.Entry(self, validate="key", validatecommand=vcmal)
        self.e_origin.pack(side="top")

        self.destination = tk.Label(self, text="Destination: ")
        self.destination.pack(side="top")
        self.e_destination = tk.Entry(self, validate="key", validatecommand=vcmal)
        self.e_destination.pack(side="top")
                
        self.capacity = tk.Label(self, text="Capacity: ")
        self.capacity.pack(side="top")
        self.e_capacity = tk.Entry(self, validate="key", validatecommand=vcmd)
        self.e_capacity.pack(side="top")

        self.LOGIN = tk.Button(self, text = 'Submit', fg="green", command=self.setCredentials )
        self.LOGIN.pack(side="bottom")

        self.QUIT = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.QUIT.pack(side="bottom")

    def on_validation_num(self, d, i, P, s, S, v, V, W):
        # Disallow anything but numbers
        if S.isdigit():
            return True
        else:
            self.bell()
            return False

    def on_validation_alpha(self, d, i, P, s, S, v, V, W):
        # Disallow anything but numbers letters
        if S.isalpha() or S == ' ':
            return True
        else:
            self.bell()
            return False

    def on_validation_alnum(self, d, i, P, s, S, v, V, W):
        # Disallow anything butletters
        if S.isalnum() or S == ' ' or S == ':':
            return True
        else:
            self.bell()
            return False
    
    def setCredentials(self):
        busnumber = self.e_busno.get()
        driver_name = self.e_drivername.get()
        arrival_time = self.e_arrivaltime.get()
        departure_time = self.e_departuretime.get()
        destination = self.e_destination.get()
        origin = self.e_origin.get()
        capacity = self.e_capacity.get()

        set_bus = (busnumber, driver_name, origin, destination, departure_time, arrival_time, capacity, 0)
        db.add_new_bus(set_bus, self.cursor, self.connection)
        self.master.destroy()

class Application(tk.Frame):
    def __init__(self, connection, cursor, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.quit_button()
        self.create_bus_info()
        self.show_avail_buses()
        self.show_reserve()
        self.remove_bus()
        self.remove_passenger()
        self.show_unavail_buses()
        self.show_singlebus_reserve()

        self.connection = connection
        self.cursor = cursor

    def remove_passenger(self):
        self.bus_info = tk.Button(self, width=25, height=3)
        self.bus_info["text"] = "Remove Reservation"
        self.bus_info["command"] = self.remove_resrv
        self.bus_info.pack(side="left")

    def remove_bus(self):
        self.bus_info = tk.Button(self, width=25, height=3)
        self.bus_info["text"] = "Remove Bus"
        self.bus_info["command"] = self.remove_businfo
        self.bus_info.pack(side="left")

    def quit_button(self):
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="top")

    def create_bus_info(self):
        self.bus_info = tk.Button(self, width=25, height=3)
        self.bus_info["text"] = "Add New Bus"
        self.bus_info["command"] = self.new_bus
        self.bus_info.pack(side="top")

    def show_reserve(self):
        self.show_resrv = tk.Button(self, width=25, height=3)
        self.show_resrv["text"] = "Show Reservation Information"
        self.show_resrv["command"] = self.show_info
        self.show_resrv.pack(side="top")

    def show_singlebus_reserve(self):
        self.show_resrv = tk.Button(self, width=25, height=3)
        self.show_resrv["text"] = "Show Reservations of a single bus"
        self.show_resrv["command"] = self.show_inbus_info
        self.show_resrv.pack(side="top")

    def show_avail_buses(self):
        self.show_buses = tk.Button(self, width=25, height=3)
        self.show_buses["text"] = "Show Available Buses"
        self.show_buses["command"] = self.show_bus_info
        self.show_buses.pack(side="top")

    def show_unavail_buses(self):
        self.show_buses = tk.Button(self, width=25, height=3)
        self.show_buses["text"] = "Show Unavailable Buses"
        self.show_buses["command"] = self.show_unavail_buses_info
        self.show_buses.pack(side="top")
    
    def new_bus(self):
        root2  = tk.Toplevel()
        root2.geometry("400x400")
        buildApp = AddNewBusApplication(self.connection, self.cursor, master=root2)

    def add_resrv(self):
        root2  = tk.Toplevel()
        root2.geometry("400x400")
        buildApp = addresrv.AddNewReservation(self.connection, self.cursor, master=root2)
    
    def show_info(self):
        data = []
        temp = []
        for row in self.cursor.execute('SELECT * FROM reservationinfo ORDER BY reservationnumber'):
            temp = []
            for i in row:
                temp.append(i)
            data.append(temp)
        table.create_table(self.connection, self.cursor, data,  key='reservation')
        
    def show_inbus_info(self):
        root2  = tk.Toplevel()
        root2.geometry("400x400")
        buildApp = ShowSingleBusReservationApplication(self.connection, self.cursor, master=root2)

    def show_bus_info(self):
        data = []
        temp = []
        for row in self.cursor.execute('SELECT * FROM busindex WHERE capacity > occupied ORDER BY busno'):
            temp = []
            for i in row:
                temp.append(i)
            data.append(temp)
            
        table.create_table(self.connection, self.cursor, data,  key='bus')

    def show_unavail_buses_info(self):
        data = []
        temp = []
        for row in self.cursor.execute('SELECT * FROM busindex WHERE capacity = occupied ORDER BY busno'):
            temp = []
            for i in row:
                temp.append(i)
            data.append(temp)
            
        table.create_table(self.connection, self.cursor, data,  key='bus')
    def remove_resrv(self):
        root2  = tk.Toplevel()
        root2.geometry("400x400")
        buildApp = RemoveReservationApplication(self.connection, self.cursor, master=root2)
    
    def remove_businfo(self):
        root2  = tk.Toplevel()
        root2.geometry("400x400")
        buildApp = RemoveBusApplication(self.connection, self.cursor, master=root2)

#INIT DB WITH TEST VALUES
conn = sqlite3.connect('bus.db')
c = conn.cursor()
db.init_db(c)
c.execute('SELECT * FROM reservationinfo WHERE reservationnumber=?', (0,))
row = c.fetchone()
if row == None:
    c.execute("INSERT INTO reservationinfo VALUES (?, ?, ?, ?)", ('0', 'test passenger', '0', '0'))

c.execute('SELECT * FROM busindex WHERE busno=?', (0,))
row = c.fetchone()
if row == None:
    c.execute("INSERT INTO busindex VALUES (?, ?, ?, ?, ?, ?, ?, ?)", ('0', 'test driver', 'test origin',
            'test destination', '0:0', '99:99', '99', '98'))
    c.execute("INSERT INTO busindex VALUES (?, ?, ?, ?, ?, ?, ?, ?)", ('1', 'test driver', 'test origin',
            'test destination', '0:0', '99:99', '99', '99'))
    c.execute("INSERT INTO busindex VALUES (?, ?, ?, ?, ?, ?, ?, ?)", ('2', 'test driver', 'test origin',
            'test destination', '0:0', '99:99', '99', '98'))
app = Application(conn, c, master=root)
app.mainloop()