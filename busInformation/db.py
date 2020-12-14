import sqlite3

def add_new_bus(record, c, conn):
    c.execute('SELECT * FROM busindex WHERE busno=?', (record[0],))
    row = c.fetchone()
    if row == None:
        c.execute("INSERT INTO busindex VALUES (?, ?, ?, ?, ?, ?, ?, ?)", record)
    else:
        print("bus already in database, delete before reassigning new index")

    conn.commit()

def add_new_reserve(record, c, conn):
    c.execute('SELECT * FROM reservationinfo WHERE reservationnumber=?', (record[0],))
    row = c.fetchone()
    if row == None:
        c.execute('SELECT * FROM busindex WHERE busno=?', (record[0],))
        row = c.fetchone()
        if row == None:
            print("bus not in database, cannot add reservation")
            return False
        elif row[-1] == row[-2]:
            print("bus full, cannot add new passenger")
            return False
        else:
            c.execute("INSERT INTO reservationinfo VALUES (?, ?, ?, ?)", record)
            c.execute('SELECT * FROM busindex WHERE busno=?', (record[0],))
            row2 = c.fetchone()
            c.execute('DELETE FROM busindex WHERE busno=?', (record[0],))
            add_new_bus((row2[0], row2[1], row2[2], row2[3], row2[4], row2[5], row2[6], row2[7] + 1), c, conn)
            return True
    else:
        print("passenger already in database, delete before reassigning new reservation")
        return False

    conn.commit()

def passenger_lookup_reservation_number(num, c, conn):
    c.execute('SELECT * FROM reservationinfo WHERE reservationnumber=?', (num,))
    row = c.fetchone()
    return row

def remove_passenger_info(num, c, conn):
    c.execute('DELETE FROM reservationinfo WHERE reservationnumber=?', (num,))
    conn.commit()

def remove_bus_info(num, c, conn):
    c.execute('DELETE FROM reservationinfo WHERE busno=?', (num,))
    c.execute('DELETE FROM busindex WHERE busno=?', (num,))
    conn.commit()

def close_conn(conn):
    conn.close()

def init_db(c):
    try:
        c.execute('''CREATE TABLE busindex
                    (busno real, driver text, origin text, destination text, departure text, arrival text,
                    capacity real, occupied real)''')

        c.execute('''CREATE TABLE reservationinfo
                    (reservationnumber real, passengername text, busno real, seatno real)''')

    except sqlite3.OperationalError:
        pass
