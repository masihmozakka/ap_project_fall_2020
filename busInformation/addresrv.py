import db
import tkinter as tk
class AddNewReservation(tk.Frame):

    def __init__(self, connection, cursor, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.connection = connection
        self.cursor = cursor
        
    def createWidgets(self):
        vcmd = (self.register(self.onValidate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
    
        vcma = (self.register(self.on_validation_alpha),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        
        vcmal = (self.register(self.on_validation_alnum),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        
        self.reservationnumber = tk.Label(self, text="Reservation number: ")
        self.reservationnumber .pack(side="top") 
        self.e_reservationnumber  = tk.Entry(self, validate="key", validatecommand=vcmd)
        self.e_reservationnumber .pack(side="top")

        self.passerngername = tk.Label(self, text="Name of passenger: ")
        self.passerngername.pack(side="top")
        self.e_passerngername = tk.Entry(self, validate="key", validatecommand=vcma)
        self.e_passerngername.pack(side="top")

        self.busno = tk.Label(self, text="Bus number: ")
        self.busno.pack(side="top")
        self.e_busno = tk.Entry(self, validate="key", validatecommand=vcmal)
        self.e_busno.pack(side="top")

        self.seatno = tk.Label(self, text="Seat number: ")
        self.seatno.pack(side="top")
        self.e_seatno = tk.Entry(self, validate="key", validatecommand=vcmal)
        self.e_seatno.pack(side="top")

        self.LOGIN = tk.Button(self, text = 'Submit', fg="green", command=self.setCredentials )
        self.LOGIN.pack(side="bottom")

        self.QUIT = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.QUIT.pack(side="bottom")

        
        
        self.text = tk.Text(self, height=10, width=40)
        self.text.pack(side="bottom", fill="both", expand=True)

    def onValidate(self, d, i, P, s, S, v, V, W):

        if P == '':
            return True
        
        if P.isdigit():
            if db.passenger_lookup_reservation_number(int(P), self.cursor, self.connection) == None:
                return True
            else:
                self.text.insert('end', P + ' :selected reservation is already taken\n')
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
        rn = self.e_reservationnumber.get()
        sn = self.e_seatno.get()
        bn = self.e_busno.get()
        pn = self.e_passerngername.get()

        set_reserve = (rn, pn, bn, sn)
        db.add_new_reserve(set_reserve, self.cursor, self.connection)
        self.master.destroy()
