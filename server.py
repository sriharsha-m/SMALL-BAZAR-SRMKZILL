
import sqlite3 as sq
import socket as soc

def selected_city(city_selected):





    conn = sq.connect('data.db')

    c = conn.cursor()

    if city_selected == 'Hyderabad':

        c.execute('SELECT NAME FROM Hyderabad')
        names = c.fetchall()
        c.execute('SELECT LOCALITY FROM Hyderabad')
        loc = c.fetchall()
        conn.commit()
        conn.close()

        names_str = ''
        loc_str = ''
        for name in names:
            names_str = names_str + name[0] + ","

        for lo in loc:
            loc_str = loc_str + lo[0] + ','

        ret_l = [names_str, loc_str]
        return ret_l

    if city_selected == 'Bangalore':

        c.execute('SELECT NAME FROM Bangalore')
        names = c.fetchall()
        c.execute('SELECT LOCALITY FROM Bangalore')
        loc = c.fetchall()
        conn.commit()
        conn.close()

        names_str = ''
        loc_str = ''
        for name in names:
            names_str = names_str + name[0] + ","

        for lo in loc:
            loc_str = loc_str + lo[0] + ','

        ret_l = [names_str, loc_str]
        return ret_l

    if city_selected == 'Chennai':

        c.execute('SELECT NAME FROM Chennai')
        names = c.fetchall()
        c.execute('SELECT LOCALITY FROM Chennai')
        loc = c.fetchall()
        conn.commit()
        conn.close()

        names_str = ''
        loc_str = ''
        for name in names:
            names_str = names_str + name[0] + ","

        for lo in loc:
            loc_str = loc_str + lo[0] + ','

        ret_l = [names_str, loc_str]
        return ret_l

    if city_selected == 'Mumbai':

        c.execute('SELECT NAME FROM Mumbai')
        names = c.fetchall()
        c.execute('SELECT LOCALITY FROM Mumbai')
        loc = c.fetchall()
        conn.commit()
        conn.close()

        names_str = ''
        loc_str = ''
        for name in names:
            names_str = names_str + name[0] + ","

        for lo in loc:
            loc_str = loc_str + lo[0] + ','

        ret_l = [names_str, loc_str]
        return ret_l

    if city_selected == 'Kolkata':

        c.execute('SELECT NAME FROM Kolkata')
        names = c.fetchall()
        c.execute('SELECT LOCALITY FROM Kolkata')
        loc = c.fetchall()
        conn.commit()
        conn.close()

        names_str = ''
        loc_str = ''
        for name in names:
            names_str = names_str + name[0] + ","

        for lo in loc:
            loc_str = loc_str + lo[0] + ','

        ret_l = [names_str, loc_str]
        return ret_l

def store_order(city,store,orders,addr,cost):

    if city == "Hyderabad":
        conn = sq.connect('Orders_data.db')
        c = conn.cursor()
        c.execute('INSERT INTO Hyderabad_orders (NAME,ORDERS,ADDR,COST) VALUES (?,?,?,?)',(store,orders,addr,cost))
        conn.commit()
        conn.close()

    if city == "Bangalore":
        conn = sq.connect('Orders_data.db')
        c = conn.cursor()
        c.execute('INSERT INTO Bangalore_orders (NAME,ORDERS,ADDR,COST) VALUES (?,?,?,?)',(store,orders,addr,cost))
        conn.commit()
        conn.close()

    if city == "Chennai":
        conn = sq.connect('Orders_data.db')
        c = conn.cursor()
        c.execute('INSERT INTO Chennai_orders (NAME,ORDERS,ADDR,COST) VALUES (?,?,?,?)',(store,orders,addr,cost))
        conn.commit()
        conn.close()

    if city == "Mumbai":
        conn = sq.connect('Orders_data.db')
        c = conn.cursor()
        c.execute('INSERT INTO Mumbai_orders (NAME,ORDERS,ADDR,COST) VALUES (?,?,?,?)',(store,orders,addr,cost))
        conn.commit()
        conn.close()

    if city == "Kolkata":
        conn = sq.connect('Orders_data.db')
        c = conn.cursor()
        c.execute('INSERT INTO Kolkata_orders (NAME,ORDERS,ADDR,COST) VALUES (?,?,?,?)',(store,orders,addr,cost))
        conn.commit()
        conn.close()

server = soc.socket()
host = soc.gethostname()
port = 5555

server.bind((host,port))
server.listen(100)

while(1):
    c, addr = server.accept()
    print(addr,'connected')
    city = c.recv(1024)
    city = city.decode()

    data= selected_city(city)

    shopes = data[0]
    loc = data[1]

    c.send(shopes.encode())
    c.send(loc.encode())

    shop = c.recv(1024)
    shop = shop.decode()

    order = c.recv(1024)
    order = order.decode()

    u_addr = c.recv(1024)
    u_addr = u_addr.decode()

    cost = c.recv(1024)
    cost = cost.decode()
    store_order(city,shop,order,u_addr,cost)





