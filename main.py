
import tkinter as tk
from tkinter import messagebox
import socket as sk
from functools import partial

s = sk.socket()
host  = sk.gethostname()
port = 5555

s.connect((host, port))

def order(shop_name):
    print(shop_name)
    def get_total():

        total_veg = (int(ev1.get()) * int(c_veg[0])) + (int(ev2.get()) * int(c_veg[1])) + (int(ev3.get()) * int(c_veg[2])) + (int(ev4.get()) * int(c_veg[3])) + (int(ev5.get()) * int(c_veg[4])) + (int(ev6.get()) * int(c_veg[5])) +(int(ev7.get()) * int(c_veg[6]))
        total_fru = (int(ef1.get()) * int(cost_fru[0])) + (int(ef2.get()) * int(cost_fru[1])) + (int(ef3.get()) * int(cost_fru[2])) + (int(ef4.get()) * int(cost_fru[3])) + (int(ef5.get()) * int(cost_fru[4])) + (int(ef6.get()) * int(cost_fru[5])) + (int(ef7.get()) * int(cost_fru[6]))
        total_sna = (int(esna1.get()) * int(cost_sna[0])) + (int(esna2.get()) * int(cost_sna[1])) + (int(esna3.get()) * int(cost_sna[2])) + (int(esna4.get()) * int(cost_sna[3])) + (int(esna5.get()) * int(cost_sna[4])) + (int(esna6.get()) * int(cost_sna[5]))

        total = (total_sna+total_fru+total_veg)

        total_num_lable = tk.Label(select_gros_f, text = '       Rs. '+str(total) + '         ',font = ('helvetica',20)).place(x = 1050, y = 500)

    def complete_order(v,f,sna):
        #get shop and city name as input
        #connect to server
        #send data

        s.send((shop_name).encode())

        quantity_veg = ev1.get() + ' '+ ev2.get() + ' ' + ev3.get() + ' ' + ev4.get() +' ' +  ev5.get() +' ' + ev6.get() + ' ' + ev7.get() + " "
        quantity_fru = ef1.get() + ' '+ ef2.get() + ' ' + ef3.get() + ' ' + ef4.get()+ ' ' + ef5.get()+ ' ' + ef6.get() + ' ' + ef7.get() + " "
        quantity_sna = esna1.get() + ' ' + esna2.get() + ' ' + esna3.get() + ' ' + esna4.get()+ ' '  + esna5.get()+ ' ' + esna6.get() + ' '
        s.send((quantity_veg + quantity_fru + quantity_sna).encode())

        u_name = name_ent.get()
        u_addr = addr_en.get("1.0",tk.END)
        u_ph = ph_ent.get()

        s.send((u_name + ' ' + u_addr + ' ' + u_ph).encode())

        total_veg = (int(ev1.get()) * int(c_veg[0])) + (int(ev2.get()) * int(c_veg[1])) + (
                    int(ev3.get()) * int(c_veg[2])) + (int(ev4.get()) * int(c_veg[3])) + (
                                int(ev5.get()) * int(c_veg[4])) + (int(ev6.get()) * int(c_veg[5])) + (
                                int(ev7.get()) * int(c_veg[6]))
        total_fru = (int(ef1.get()) * int(cost_fru[0])) + (int(ef2.get()) * int(cost_fru[1])) + (
                    int(ef3.get()) * int(cost_fru[2])) + (int(ef4.get()) * int(cost_fru[3])) + (
                                int(ef5.get()) * int(cost_fru[4])) + (int(ef6.get()) * int(cost_fru[5])) + (
                                int(ef7.get()) * int(cost_fru[6]))
        total_sna = (int(esna1.get()) * int(cost_sna[0])) + (int(esna2.get()) * int(cost_sna[1])) + (
                    int(esna3.get()) * int(cost_sna[2])) + (int(esna4.get()) * int(cost_sna[3])) + (
                                int(esna5.get()) * int(cost_sna[4])) + (int(esna6.get()) * int(cost_sna[5]))

        total = (total_sna + total_fru + total_veg)

        total = str(total)

        s.send(total.encode())


        s.close()

        messagebox.showinfo("Success", "We have recieved your Order")


    new_win = tk.Tk()
    new_win.geometry('1500x750')

    select_l = tk.Label(new_win,text = 'Select Items:').place(x = 200,y = 30)

    select_gros_f = tk.Frame(new_win,width = 1480, height = 700,bg = 'White')
    select_gros_f.place(x = 10, y = 80)

    # veg

    veg_f = tk.Frame(select_gros_f,width = 390, height = 350, highlightbackground = 'black',highlightthickness = 2)
    veg_f.place(x = 10, y = 10)



    veg_t = tk.Label(veg_f,text = "Vegetables  :- ").place(x = 10, y = 10)

    veg_l = ['Tomoto', 'Potato', 'Drum Sticks', 'Ladies Finger', 'spinach','Beans','Peas']
    c_veg = ['17','25', '5', '40', '20', '20','30']


    v1 = tk.Label(veg_f,text = veg_l[0]).place(x = 10, y = 50)
    cv1 = tk.Label(veg_f, text = c_veg[0]+'Rs/kg').place(x = 150,y = 50)
    ev1 = tk.Entry(veg_f)
    ev1.insert('end', '0')
    ev1.place(x = 250, y = 50)

    v2 = tk.Label(veg_f, text=veg_l[1]).place(x=10, y=100)
    cv2 = tk.Label(veg_f, text=c_veg[1]+'Rs/kg').place(x=150, y=100)
    ev2 = tk.Entry(veg_f)
    ev2.insert('end', '0')
    ev2.place(x=250, y=100)

    v3 = tk.Label(veg_f, text=veg_l[2]).place(x=10, y=150)
    cv3 = tk.Label(veg_f, text=c_veg[2]+'Rs/Pc').place(x=150, y=150)
    ev3 = tk.Entry(veg_f)
    ev3.insert('end', '0')
    ev3.place(x=250, y=150)

    v4 = tk.Label(veg_f, text=veg_l[3]).place(x=10, y=200)
    cv4 = tk.Label(veg_f, text=c_veg[3]+'Rs/kg').place(x=150, y=200)
    ev4 = tk.Entry(veg_f)
    ev4.insert('end', '0')
    ev4.place(x=250, y=200)

    v5 = tk.Label(veg_f, text=veg_l[4]).place(x=10, y=250)
    cv5 = tk.Label(veg_f, text=c_veg[4]+'Rs/Pc').place(x=150, y=250)
    ev5 = tk.Entry(veg_f)
    ev5.insert('end', '0')
    ev5.place(x=250, y=250)

    v6 = tk.Label(veg_f, text=veg_l[5]).place(x=10, y=300)
    cv6 = tk.Label(veg_f, text=c_veg[5]+'Rs/kg').place(x=150, y=300)
    ev6 = tk.Entry(veg_f)
    ev6.insert('end', '0')
    ev6.place(x=250, y=300)

    v7 = tk.Label(veg_f, text=veg_l[6]).place(x=10, y=350)
    cv7 = tk.Label(veg_f, text=c_veg[6]+'Rs/kg').place(x=150, y=350)
    ev7 = tk.Entry(veg_f)
    ev7.insert('end', '0')
    ev7.place(x=250, y=350)

    #fru
    fruit_f = tk.Frame(select_gros_f, width=390, height=350, highlightbackground='black', highlightthickness=2)
    fruit_f.place(x=450, y=10)




    fruit_t = tk.Label(fruit_f, text="Fruits  :- ").place(x=10, y=10)

    fru_l = ['Apples', 'Bananas', 'Mangoes', 'Grapes', 'Oranges', 'Strawberry', 'Watermelon']
    cost_fru = ['25', '20', '30', '25', '30', '50', '30']

    f1 = tk.Label(fruit_f, text=fru_l[0]).place(x=10, y=50)
    cf1 = tk.Label(fruit_f, text= cost_fru[0]+'Rs/kg').place(x=150, y=50)
    ef1 = tk.Entry(fruit_f)
    ef1.insert('end', '0')
    ef1.place(x=250, y=50)

    f2 = tk.Label(fruit_f, text=fru_l[1]).place(x=10, y=100)
    cf2 = tk.Label(fruit_f, text=cost_fru[1]+'Rs/kg').place(x=150, y=100)
    ef2 = tk.Entry(fruit_f)
    ef2.insert('end', '0')
    ef2.place(x=250, y=100)

    f3 = tk.Label(fruit_f, text=fru_l[2]).place(x=10, y=150)
    cf3 = tk.Label(fruit_f, text=cost_fru[2]+'Rs/kg').place(x=150, y=150)
    ef3 = tk.Entry(fruit_f)
    ef3.insert('end', '0')
    ef3.place(x=250, y=150)

    f4 = tk.Label(fruit_f, text=fru_l[3]).place(x=10, y=200)
    cf4 = tk.Label(fruit_f, text=cost_fru[3]+'Rs/kg').place(x=150, y=200)
    ef4 = tk.Entry(fruit_f)
    ef4.insert('end', '0')
    ef4.place(x=250, y=200)

    f5 = tk.Label(fruit_f, text=fru_l[4]).place(x=10, y=250)
    cf5 = tk.Label(fruit_f, text=cost_fru[4]+'Rs/kg').place(x=150, y=250)
    ef5 = tk.Entry(fruit_f)
    ef5.insert('end', '0')
    ef5.place(x=250, y=250)

    f6 = tk.Label(fruit_f, text=fru_l[5]).place(x=10, y=300)
    cf6 = tk.Label(fruit_f, text=cost_fru[5]+'Rs/kg').place(x=150, y=300)
    ef6 = tk.Entry(fruit_f)
    ef6.insert('end', '0')
    ef6.place(x=250, y=300)

    f7 = tk.Label(fruit_f, text=fru_l[6]).place(x=10, y=350)
    cf7 = tk.Label(fruit_f, text=cost_fru[6]+'Rs/Pc').place(x=150, y=350)
    ef7 = tk.Entry(fruit_f)
    ef7.insert('end', '0')
    ef7.place(x=250, y=350)

    #sna

    sna_f = tk.Frame(select_gros_f, width=390, height=350, highlightbackground='black', highlightthickness=2)
    sna_f.place(x=890, y=10)

    sna_t = tk.Label(sna_f, text="Snacks  :- ").place(x=10, y=10)

    sna_l = ['Lays', 'Kurkure', 'Bingo Chips', 'Chocos', 'Dairy Milk', '5 Star']
    cost_sna = ['10', '10', '10', '10', '20', '20']

    sna1 = tk.Label(sna_f, text=sna_l[0]).place(x=10, y=50)
    csna1 = tk.Label(sna_f, text='Rs.'+cost_sna[0]).place(x=150, y=50)
    esna1 = tk.Entry(sna_f)
    esna1.insert('end', '0')
    esna1.place(x=250, y=50)

    sna2 = tk.Label(sna_f, text=sna_l[1]).place(x=10, y=100)
    csna2 = tk.Label(sna_f, text='Rs.'+cost_sna[1]).place(x=150, y=100)
    esna2 = tk.Entry(sna_f)
    esna2.insert('end', '0')
    esna2.place(x=250, y=100)

    sna3 = tk.Label(sna_f, text=sna_l[2]).place(x=10, y=150)
    csna3 = tk.Label(sna_f, text='Rs.'+cost_sna[2]).place(x=150, y=150)
    esna3 = tk.Entry(sna_f)
    esna3.insert('end', '0')
    esna3.place(x=250, y=150)

    sna4 = tk.Label(sna_f, text=sna_l[3]).place(x=10, y=200)
    csna4 = tk.Label(sna_f, text='Rs.'+cost_sna[3]).place(x=150, y=200)
    esna4 = tk.Entry(sna_f)
    esna4.insert('end', '0')
    esna4.place(x=250, y=200)

    sna5 = tk.Label(sna_f, text=sna_l[4]).place(x=10, y=250)
    csna5 = tk.Label(sna_f, text='Rs.'+cost_sna[4]).place(x=150, y=250)
    esna5 = tk.Entry(sna_f)
    esna5.insert('end', '0')
    esna5.place(x=250, y=250)

    sna6 = tk.Label(sna_f, text=sna_l[5]).place(x=10, y=300)
    csna6 = tk.Label(sna_f, text='Rs.'+ cost_sna[5]).place(x=150, y=300)
    esna6 = tk.Entry(sna_f)
    esna6.insert('end', '0')
    esna6.place(x=250, y=300)




    #uder_details

    name_l = tk.Label(select_gros_f,text = 'Name:-').place(x = 50, y = 500)
    name_ent = tk.Entry(select_gros_f)
    name_ent.place(x = 120, y = 500)

    ph_l = tk.Label(select_gros_f, text='Phone no.:-').place(x=50, y=525)
    ph_ent = tk.Entry(select_gros_f)
    ph_ent.place(x=120, y=525)

    addr_l = tk.Label(select_gros_f, text = 'Address:-').place(x = 50, y = 550)
    addr_en = tk.Text(select_gros_f,width = 50, height = 3)
    addr_en.place(x = 120, y = 550)



    #total

    total_label = tk.Label(select_gros_f, text = 'Total',font = ('helvetica',20),fg = 'RED').place(x = 900, y = 500)
    total_button = tk.Button(select_gros_f,text = 'Calculate Total',command= get_total)
    total_button.place(x = 1050, y = 600)
    complete_order_with_arg = partial(complete_order,veg_l, fru_l, sna_l)
    order_button = tk.Button(select_gros_f,text = 'Confirm Order',command = complete_order_with_arg)
    order_button.place(x = 1200, y = 600)



    new_win.mainloop()

def selected_city():

    shops_frame = tk.Frame(root,width = 490, height = 450, bg = '#E7A18D')
    shops_frame.place(x = 10, y = 100)

    shops_l = tk.Label(shops_frame, text='Shops in your Area: ')
    shops_l.place(x=200, y=10)

    city_selected = city.get()



    s.send(city_selected.encode())
    shopes_names_server = s.recv(1024)

    loc = s.recv(1024)
    shopes_names_server = shopes_names_server.decode()
    loc = loc.decode()


    shopes_names_server = shopes_names_server.split(',')
    shopes_names_server.pop()

    loc = loc.split(',')
    loc.pop()

    j = 0
    for i,name in enumerate(shopes_names_server):
        names_f = tk.Frame(shops_frame,width = 487,height = 70,highlightthickness = 2,highlightbackground = 'black',bg = '#E7A18D')
        names_f.place(x = 0, y = 30 + (70*i))

        name_l = tk.Label(names_f,text = name,bg = '#E7A18D')
        name_l.place(x = 60, y = 10)

        loc_l = tk.Label(names_f,text = loc[j],bg = '#E7A18D')
        loc_l.place(x = 60, y = 30)
        j=+1

        order_with_in = partial(order,shopes_names_server[i])
        ord_but = tk.Button(names_f,text = "Order From Here",command = order_with_in)
        ord_but.place(x = 350, y = 20)


root = tk.Tk()

root.geometry('500x600')
root.config(bg = 'BLACK')
head = tk.Label(root,text = "Shop_Groceries.com",bg = "Black", fg = "White",font = ('Comic Sans MS',20)).place(x = 120, y = 20)
location_frame = tk.Frame(root,width = 480,height =450,bg = '#E7A18D')
location_frame.place(x = 10, y= 100)


city_l = tk.Label(location_frame,text = 'Select City',font = ('Comic Sans MS',12),bg = '#E7A18D')
city_l.place(x = 200, y = 10)
city = tk.StringVar()
hyd = tk.Radiobutton(location_frame,text = 'Hyderabad',variable = city,value = 'Hyderabad',command = selected_city,font = ('Comic Sans MS',9),bg = '#E7A18D')
hyd.place(x = 70, y = 50)

che = tk.Radiobutton(location_frame,text = 'Chennai',variable = city,value = 'Chennai',command = selected_city,font = ('Comic Sans MS',9),bg = '#E7A18D')
che.place(x = 210, y = 50)

bng = tk.Radiobutton(location_frame,text = 'Bangalore',variable = city,value = 'Bangalore',command = selected_city,font = ('Comic Sans MS',9),bg = '#E7A18D')
bng.place(x = 325,y = 50)

mum = tk.Radiobutton(location_frame,text = 'Mumbai',variable = city,value = 'Mumbai',command = selected_city,font = ('Comic Sans MS',9),bg = '#E7A18D')
mum.place(x = 150, y = 100)

koc = tk.Radiobutton(location_frame,text = 'Kolkata',variable = city,value = 'Kolkata',command = selected_city,font = ('Comic Sans MS',9),bg = '#E7A18D')
koc.place(x = 270, y = 100)




root.mainloop()