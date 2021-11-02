from tkinter import *
import socket as soc

veg_l = ['Tomoto', 'Potato', 'Drum Sticks', 'Ladies Finger', 'spinach','Beans','Peas']
fru_l = ['Apples', 'Bananas', 'Mangoes', 'Grapes', 'Oranges', 'Strawberry', 'Watermelon']
sna_l = ['Lays', 'Kurkure', 'Bingo Chips', 'Chocos', 'Dairy Milk', '5 Star']

def get_orders():

    city = city_en.get()
    shop = shop_en.get()
    print(shop,city)

    s = soc.socket()
    host = soc.gethostname()
    port = 6666
    s.connect((host,port))
    s.send(city.encode() + ",".encode())
    s.send(shop.encode())

    orders = s.recv(2028)
    orders = orders.decode()

    addr = s.recv(1024)
    addr = addr.decode()



    l = Label(fr,text = 'Tomoto\n'+ 'Potato\n '+ 'Drum Sticks \n' + 'Ladies Finger \n'+ 'spinach \n'+'Beans \n'+ 'Peas \n' + 'Apples \n' +'Bananas \n'+ 'Mangoes \n'+ 'Grapes \n'+ 'Oranges \n'+ 'Strawberry \n'+ 'Watermelon \n' + 'Lays \n' + 'Kurkure \n' +  'Bingo Chips \n' +  'Chocos \n'+ 'Dairy Milk \n' + '5 Star',bg ='#5DE5D2' )
    l.place(x = 10,y = 40)

    ll = Label(fr,text = orders,bg = '#5DE5D2').place(x = 270, y = 40)

    lll = Label(fr,text = addr,bg = '#5DE5D2').place(x = 550, y = 40)




root=Tk()
root.geometry('1000x1000')
root.title("Shop Keeper")
root.config(bg="black")
fr=Frame(root,width=1230,height=600,bg="#5DE5D2")
fr.place(x=25,y=30)

lh=Label(fr,text="ORDER LIST",bg="#5DE5D2",font=("aerial",16))
lh.place(x=10,y=10)
lh=Label(fr,text="QUANTITY",bg="#5DE5D2",font=("aerial",16))
lh.place(x=300,y=10)
lh=Label(fr,text="ADDRESS",bg="#5DE5D2",font=("aerial",16))
lh.place(x=550,y=10)



city_l = Label(root,text = "Enter  City").place(x = 100, y = 650)
shop_n = Label(root,text = 'Enter Store Name').place(x = 300, y = 650)
city_en = Entry(root)
city_en.place(x = 100, y = 700)

shop_en = Entry(root)
shop_en.place(x = 300, y = 700)

but = Button(root,text = 'Get Orders',command = get_orders)
but.place(x = 500, y = 700)

root.mainloop()