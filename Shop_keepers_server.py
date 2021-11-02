
import sqlite3 as sq
import socket as soc
def get_orders(city,shop):
    conn = sq.connect('Orders_data.db')
    c = conn.cursor()
    print(shop)
    if city == 'Hyderabad':

        c.execute('SELECT * FROM Hyderabad_orders WHERE NAME = (?)',(shop,))
        data = c.fetchall()


        return data

    if city == 'Bangalore':

        c.execute('SELECT * FROM Bangalore_orders WHERE NAME = (?)',(shop,))
        data = c.fetchall()


        return data

    if city == 'Chennai':

        c.execute('SELECT * FROM Chennai_orders WHERE NAME = (?)',(shop,))
        data = c.fetchall()


        return data

    if city == 'Mumbai':

        c.execute('SELECT * FROM Mumbai_orders WHERE NAME = (?)',(shop,))
        data = c.fetchall()


        return data

    if city == 'Kolkata':

        c.execute('SELECT * FROM Kolkata_orders WHERE NAME = (?)',(shop,))
        data = c.fetchall()


        return data


server = soc.socket()
host = soc.gethostname()
port = 6666

server.bind((host,port))
server.listen(100)

while(1):
    c, addr = server.accept()
    city = c.recv(1024)
    city = city.decode()



    details = city.split(',')
    city = details[0]
    shop = details[1]
    data = get_orders(city,shop)
    print(data)

    orders = data[0][1]
    address = data[0][2]
    cost = data[0][3]

    print(cost)

    c.send(str(orders).encode())
    c.send(str(address).encode())
    c.send(str(cost).encode())

    c.close()