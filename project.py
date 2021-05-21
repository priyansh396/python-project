import random
import datetime
name=[]
phone_no=[]
address=[]
check_in=[]
check_out=[]
room=[]
price=[]
rc=[]
p=[]
room_no=[]
custid=[]
day=[]
i=0
def Home():
    print("\t\t WELCOME TO HOTEL GRANDE\n")
    print("\t\t\t 1 Bookings\n")
    print("\t\t\t 2 Rooms\n")
    print("\t\t\t 3 Room_Service\n")
    print("\t\t\t 4 Payment_Method\n")
    print("\t\t\t 5 Records\n")
    print("\t\t\t 0 Exit\n")

    ch=int(input("->"))

    if ch==1:
        print(" ")
        Bookings()
    elif ch==2:
        print(" ")
        Rooms()
    elif ch==3:
        print(" ")
        Room_Service()
    elif ch==4:
        print(" ")
        Payment_Method()
    elif ch==5:
        print(" ")
        Records()
    else:
        Exit()
def date(c):
    if c[2]>=2020 and c[2]<=2021:
        if c[1]!=0 and c[1]<=12:
            if c[1]==2 and c[0]!=0 and c[0]<=31:
                if c[2]%4==0 and c[0]<=29:
                    pass
                elif c[0]<29:
                    pass
                else:
                    print("Invalid Date\n")
                    name.pop(i)
                    phone_no.pop(i)
                    address.pop(i)
                    check_in.pop(i)
                    check_out.pop(i)
                    Bookings()
            elif c[1]<=7 and c[1]%2 !=0 and c[0]<=31:
                pass
            elif c[1]<=7 and c[1]%2==0 and c[0]<=30 and c[1]!=2:
                pass
            elif c[1]>=8 and c[1]%2==0 and c[0]<=31:
                pass
            elif c[1]>=8 and c[1]%2!=0 and c[0]<=31:
                pass
            
            else:
                print("Invalid Date\n")
                name.pop(i)
                phone_no.pop(i)
                address.pop(i)
                check_in.pop(i)
                check_out.pop(i)
                Bookings()
                
        else:
            print("Invalid Date\n")
            name.pop(i)
            phone_no(i)
            address.pop(i)
            check_in.pop(i)
            check_out.pop(i)
            Bookings()
def Bookings():
        global i
        print("Booking Rooms")
        print(" ")

        while 1:
            n=str(input("Name: "))
            p1=str(input("Phone no.: "))
            a=str(input("Address: "))

            if n!="" and p1!="" and a!="":
                name.append(n)
                address.append(a)
                break
            else:
                print("\tName,Phone no. and Address cannot be empty!")
        cii=str(input("Check_In: "))
        check_in.append(cii)
        cii=cii.split('/')
        ci=cii
        ci[0]=int(ci[0])
        ci[1]=int(ci[1])
        ci[2]=int(ci[2])
        date(ci)
        coo=str(input("Check-Out:"))
        check_out.append(coo)
        coo=coo.split('/')
        co=coo
        co[0]=int(co[0])
        co[1]=int(co[1])
        co[2]=int(co[2])
        if co[1]<ci[1] and co[2]<ci[2]:
            print("\n\tErr..!\n\tCheck-Out date must come after Check_In\n")
            name.pop(i)
            address.pop(i)
            check_in.pop(i)
            check_out.pop(i)
            Bookings()
        elif co[1]==ci[1] and co[2]>=ci[2] and co[0]<=ci[0]:
            print("\n\tErr..!\n\tCheck-Out date must come after Check-In\n")
            name.pop(i)
            address.pop(i)
            check_in.pop(i)
            check_out.pop(i)
            Bookings()
        else:
            pass
        date(co)
        d1=datetime.datetime(ci[2],ci[1],ci[0])
        d2=datetime.datetime(co[2],co[1],co[0])
        d=(d2-d1).days
        day.append(d)

        print("----Select Room Type----")
        print(" 1. Single Room")
        print(" 2. Double Room")
        print(" 3. Triple Room")
        print(" 4. Quad Room")
        print(" 5. Maharaja Suite")
        print(" 6. Penthouse Suite")
        print(("\t\tPress 0 for Room Prices"))

        ch=int(input("->"))

        if ch==0:
            print("1. Single Room -Rs.1500")
            print("2. Double Room -Rs.2500")
            print("3. Triple Room -Rs.3500")
            print("4. Quad Room -Rs.4200")
            print("5. Maharaja Suite -Rs.11000")
            print("6. Penthouse Suite -Rs.25000")
            ch=int(input("->"))
        if ch==1:
            room.append('Single Room')
            print("Room type-Single Room")
            price.append(1500)
            print("Price-1500")
        elif ch==2:
            room.append('Double Room')
            print("Room Type-Double Room")
            price.append(2500)
            print("Price-2500")
        elif ch==3:
            room.append('Triple Room')
            print("Room Type-Triple Room")
            price.append(3500)
            print("Price-3500")
        elif ch==4:
            room.append('Quad Room')
            print("Room Type-Quad Room")
            price.append(4200)
            print("Price-4200")
        elif ch==5:
            room.append('Maharaja Suite')
            print("Room Type-Maharaja Suite")
            price.append(11000)
            print("Price-11000")
        elif ch==6:
            room.append('Penthouse Suite')
            print("Room Type-Penthouse Suite")
            price.append(25000)
            print("Price-25000")
        else:
            print("Wrong choice!")
#generating room no.and customer id
        rn=random.randrange(25)+250
        cid=random.randrange(25)+10
#checking if the id and room no not alloted already
        while rn in room_no or cid in custid:
            rn=random.randrange(40)+250
            cid=random.randrange(40)+10
        rc.append(0)
        p.append(0)
        if p1 not in phone_no:
            phone_no.append(p1)
        elif p1 in phone_no:
            for n in range(0,i):
                if p1==phone_no[n]:
                    if p[n]==1:
                        phone_no.append(p1)
        elif p1 in phone_no:
            for n in range(0,i):
                if p1==phone_no[n]:
                    if p[n]==0:
                        print("\tPhone number already exists and payment not made!")
                        name.pop(i)
                        address.pop(i)
                        check_in.pop(i)
                        check_out.pop(i)
                        Bookings()
        print("")
        print("\t\t\t     Room Booked Successfully    \n")
        print("Room No. - ",rn)
        print("Customer ID - ",cid)
        room_no.append(rn)
        custid.append(cid)
        i=i+1
        n=int(input("0-Back\n ->"))
        if n==0:
            Home()
        else:
            Exit()
def Rooms():
    print("             Hotel Rooms Information       ")
    print("")
    print("Single Room")
    print("------------------------------------")
    print("Room amenities include:single bed,television,telephone,AC,")
    print("Cupboard,coffee table,sofa and attached washroom with hot/cold water.\n")
    print("Double Room")
    print("------------------------------------")
    print("Room amenities include:double bed,television,telephone,AC,")
    print("Cupboard,coffee table,sofa and attached washroom with hot/cold water.\n")
    print("Triple Room")
    print("------------------------------------")
    print("Room amenities include:triple bed,television,telephone,AC,")
    print("2 Cupboards,coffee table,sofa and attached washroom with hot/cold water.\n")
    print("Quad Room")
    print("------------------------------------")
    print("Room amenities include:2 double bed,television,telephone,AC,")
    print("3 Cupboards,coffee table,sofa and attached washroom with hot/cold water.\n")
    print("Maharaja Suite")
    print("------------------------------------")
    print("Room amenities include:king size bed,television,telephone,AC,valet service,butler")
    print("personal kitchen,24hrs housekeeping service,3 Cupboards,coffee table,sofa and attached washroom with hot/cold water.\n")
    print("Penthouse Suite")
    print("------------------------------------")
    print("Room amenities include:king size bed,television,telephone,AC,valet service,butler")
    print("personal terrace&kitchen,24hrs housekeeping service and room service,3 Cupboards,coffee table,sofa and attached washroom with hot/cold water.\n")
    print()
    n=int(input("0-Back\n ->"))
    if n==0:
        Home()
    else:
        Exit()
def Room_Service():
    ph=int(input("Customer ID:"))
    global i
    f=0
    r=0
    for n in range(0,i):
        if custid[n]==ph and p[n]==0:
            f=1
            print("---------------------------------------")
            print("                Hotel Grande")
            print("---------------------------------------")
            print("                  Menu Card")
            print("---------------------------------------")
            print("\n BEVERAGES                              26 Dal Fry................ 140.00") 
            print("----------------------------------      27 Dal Makhani............ 150.00") 
            print(" 1  Regular Tea............. 20.00      28 Dal Tadka.............. 150.00") 
            print(" 2  Masala Tea.............. 25.00") 
            print(" 3  Coffee.................. 25.00      BREADS") 
            print(" 4  Cold Drink.............. 25.00     ----------------------------------") 
            print(" 5  Bread Butter............ 30.00      29 Plain Roti.............. 15.00") 
            print(" 6  Bread Jam............... 30.00      30 Butter Roti............. 15.00") 
            print(" 7  Veg. Sandwich........... 50.00      31 Tandoori Roti........... 20.00") 
            print(" 8  Veg. Toast Sandwich..... 50.00      32 Butter Naan............. 20.00") 
            print(" 9  Cheese Toast Sandwich... 70.00") 
            print(" 10 Grilled Sandwich........ 70.00      RICE")  
            print("                                       ----------------------------------") 
            print(" SOUPS                                  33 Plain Rice.............. 90.00") 
            print("----------------------------------      34 Jeera Rice.............. 90.00") 
            print(" 11 Tomato Soup............ 110.00      35 Veg Pulao.............. 110.00") 
            print(" 12 Hot & Sour............. 110.00      36 Peas Pulao............. 110.00") 
            print(" 13 Veg. Noodle Soup....... 110.00") 
            print(" 14 Sweet Corn............. 110.00      SOUTH INDIAN") 
            print(" 15 Veg. Munchow........... 110.00     ----------------------------------") 
            print("                                        37 Plain Dosa............. 100.00") 
            print(" MAIN COURSE                            38 Onion Dosa............. 110.00") 
            print("----------------------------------      39 Masala Dosa............ 130.00") 
            print(" 16 Shahi Paneer........... 110.00      40 Paneer Dosa............ 130.00") 
            print(" 17 Kadai Paneer........... 110.00      41 Rice Idli.............. 130.00") 
            print(" 18 Handi Paneer........... 120.00      42 Sambhar Vada........... 140.00") 
            print(" 19 Palak Paneer........... 120.00") 
            print(" 20 Chilli Paneer.......... 140.00      ICE CREAM") 
            print(" 21 Matar Mushroom......... 140.00     ----------------------------------") 
            print(" 22 Mix Veg................ 140.00      43 Vanilla................. 60.00") 
            print(" 23 Jeera Aloo............. 140.00      44 Strawberry.............. 60.00") 
            print(" 24 Malai Kofta............ 140.00      45 Pineapple............... 60.00") 
            print(" 25 Aloo Matar............. 140.00      46 Butter Scotch........... 60.00")
            print(" WINES                                                                   ")
            print("----------------------------------                                       ")
            print(" 47 White Wine..................750.00                                       ")
            print(" 48 Red Wine....................850.00                                       ")
            print(" 49 Rose Wine...................750.00                                       ")
            print(" 50 Dessert Wine................900.00                                       ")
            print(" 51 Champagne..................1100.00                                       ")
            print("\n                HOPE YOU ENJOYED YOUR MEAL             ")
            print("Press 0 - to end ")
            ch=1
            while(ch!=0):

                ch=int(input(" -> "))
                if ch==1 or ch==31 or ch==32:
                    rs=20
                    r=r+rs 
                elif ch<=4 and ch>=2: 
                    rs=25
                    r=r+rs 
                elif ch<=6 and ch>=5: 
                    rs=30
                    r=r+rs 
                elif ch<=8 and ch>=7: 
                    rs=50
                    r=r+rs 
                elif ch<=10 and ch>=9: 
                    rs=70
                    r=r+rs 
                elif (ch<=17 and ch>=11) or ch==35 or ch==36 or ch==38: 
                    rs=110
                    r=r+rs 
                elif ch<=19 and ch>=18: 
                    rs=120
                    r=r+rs 
                elif (ch<=26 and ch>=20) or ch==42: 
                    rs=140
                    r=r+rs 
                elif ch<=28 and ch>=27: 
                    rs=150
                    r=r+rs 
                elif ch<=30 and ch>=29: 
                    rs=15
                    r=r+rs 
                elif ch==33 or ch==34: 
                    rs=90
                    r=r+rs 
                elif ch==37: 
                    rs=100
                    r=r+rs 
                elif ch<=41 and ch>=39: 
                    rs=130
                    r=r+rs 
                elif ch<=46 and ch>=43: 
                    rs=60
                    r=r+rs 
                elif ch<=47 and ch>=51:
                    rs=1100
                    r=r+rs
                elif ch==0:
                    pass
                else:
                    print("Wrong Choice!")
                    
            print("Total Bill: ",r)
            r=r+rc.pop(n)
            rc.append(r)
        else:
            pass
    if f==0:
        print("Not a Valid Customer ID")
    n=int(input("0-Back\n->"))
    if n==0:
        Home()
    else:
         Exit()
         
def Payment_Method():
    ph=str(input("Phone Number:"))
    global i
    f=0
    for n in range(0,i):
        if ph==phone_no[n]:
        
             if p[n]==0:
                 f=1
                 print("Payment")
                 print("----------------------")
                 print("Payment Mode")

                 print(" 1.Credit/Debit Card")
                 print(" 2.Paytm/Google pay/Phone pe")
                 print(" 3.Cash")
                 x=int(input("-> "))
                 print("\n Amount: ",(price[n]*day[n])+rc[n])
                 print("\n             Pay for Hotel Grande")
                 print(" (y/n)")
                 ch=str(input("->"))

                 if ch=="y" or ch=="y":
                     print("\n\n-------------------------")
                     print("            Hotel Grande")
                     print("-----------------------------")
                     print("                Bill")
                     print("-----------------------------")
                     print("Name: ",name[n],"\t\n Phone No.: ",phone_no[n],"\t\n Address:",address[n],"\t")
                     print("\n Check-in: ",check_in[n],"\t\n Check-out: ",check_out[n],"\t")
                     print("\n Room Type: ",room[n],"\t\n Room Charges: ",price[n]*day[n],"\t")
                     print("Restaurant Charges: \t",rc[n])
                     print("------------------------------")
                     print("\n Total Amount: ",(price[n]*day[n])+rc[n],"\t")
                     print("---------------------------------")
                     print("              Thank You")
                     print("              Visit Again!:)")
                     print("---------------------------------\n")
                     p.pop(n)
                     p.insert(n,1)

                     room_no.pop(n)
                     custid.pop(n)
                     room_no.insert(n,0)
                     custid.insert(n,0)
                     
        else:
            for j in range(n+1,i):
                      if ph==phone_no[j]:
                          if p[j]==0:
                              pass
                            
                          else:
                              f=1
                              print("\n\tPayment has been made!)\n\n")
                                
                                 
    if f==0:
        print("Invalid Customer Id")
    n=int(input("0-Back\n->"))
    if n==0:
        Home()
    else:
        Exit()
def Records():
    #check that the record exists or not
    if phone_no!=[]:
        print("         Hotel Records   \n")
        print(" |NAME   |PHONE NO.      |ADDRESS    |CHECK-IN        |CHECK-OUT     |ROOM TYPE      |PRICE   |")
        print("--------------------------------------------------------------------------------------------------------------------")
        for n in range(0,i):
            print("|", name[n],"\t|",phone_no[n],"\t|",address[n],"\t|",check_in[n],"\t|",check_out[n],"\t|",room[n],"\t|",price[n])
        print("-------------------------------------------------------------------------------------------------------------------")
    else:
        print("No Records Found")
    n=int(input("0-Back\n ->"))
    if n==0:
        Home()
    else:
        Exit()
Home()

    
                              
                              
                     
                           
                      
    
            
            
            
                        
            
        
            
            
            
        
