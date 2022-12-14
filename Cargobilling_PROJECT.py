import os
'''import matplotlib.pyplot as plt'''
import sys
sys.path.append('Users\manmo\AppData\Local\Programs\Python\Python38\lib\site-packages\mysql\connector\cursor.py')
import mysql.connector
#Create connection object
mycon=mysql.connector.connect(user='root',passwd='2357',host='localhost',database='CargoDB')
#Check connection
if mycon.is_connected():
    print("**Successfully conneceted to database**")
else:
    print("**error connecting to database**")

cur=mycon.cursor(buffered=True)





#creating table1

cur.execute("create table if not exists Customers(C_Id int auto_increment primary key,C_Name char(25) not null,C_Address char(25),C_City char(15),P_Code char(10),D_Code char(10),Weight numeric(20,2),Rate_P numeric(20,2),Rate_D numeric(20,2),Amount numeric(20,2),GST_18_per numeric(20,2),Total_Amount numeric(20,2))")
    
r1=("Bombino Express Pvt Ltd","A 127 Mahipal Pur","Delhi","CG","AS",110,220,50,24250,4365,28615)
r2=("Excel Worldwide Logistics","Z 23 Swami Ananda Marg","Chennai","PE","EU",120,240,70,28870,5196.6,34066.6)
r3=("Asia Express","390 Connaught Place","Banglore","EX","US",130,260,90,33890,6100.2,39990.2)
r4=("World Express Pvt Ltd","309 BHIKAJI CAMA PLACE","Mumbai","CU","AF",150,230,120,36120,6501.6,42621.6)
r5=("SJSB Airlogistics","390 Ashok Vihar","Delhi","EX","US",132,260,90,43890,6100.2,49990.2)
r6=("AABB Express","190 Connaught Place","Delhi","PE","AF",130,240,120,31320,5637.6,36957.6)
r7=("ASTAR Express","290 Krishna Colony","Banglore","PE","AF",140,240,120,33720,6069.6,39789.6)
r8=("Wow World Airlogistic","5390 Netaji Subhash Place","Delhi","CG","EU",150,220,70,33070,5952.6,39022.6)
st="insert into Customers(C_Name,C_Address,C_City,P_Code,D_Code,Weight,Rate_P,Rate_D,Amount,GST_18_per,Total_Amount) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
cur.executemany(st,[r1,r2,r3,r4,r5,r6,r7,r8])

#creating table2
cur.execute("create table if not exists product(P_Code char(10) not null,P_Name char(10) not null,Rate_P numeric(20,2))")
r1=("PE","Perishable",240)
r2=("CG","Cargo",220)
r3=("Cu","Courier",230)
r4=("EX","Express",260)
st="insert into Product(P_Code,P_Name,Rate_P) values(%s,%s,%s)"
cur.executemany(st,[r1,r2,r3,r4])
  


#creating table3
cur.execute("create table if not exists destination(D_Code char(10)not null,D_Name char(10) not null,Rate_D numeric(20,2))")
r1=("AS","Asia",50)
r2=("EU","Europe",70)
r3=("US","USA",90)
r4=("AF","Africa",120)
st="insert into Destination(D_Code,D_Name,Rate_D) values(%s,%s,%s)"
cur.executemany(st,[r1,r2,r3,r4])



#to input data
def adddata():
    name=input("enter customer name")
    add=input("enter customer address")
    city=input("enter customer city")
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost', user='root', passwd='2357', database='cargodb')
    mysql1="select * from product"
    cur.execute(mysql1)
    d=cur.fetchall()
    print("**displaying data in the product**")
    for i in d:
        print(i)
    pc=input("enter p_code from above records :")
    t1=(pc,)
    mysql2="select * from destination"
    cur.execute(mysql2)
    d=cur.fetchall()
    print("**displaying data in the destination**")
    for i in d:
        print(i)
    dc=input("enter d_code from above records:")
    t2=(dc,)
    Wt=float(input("enter weight of goods"))
    sql3="select Rate_P from product where P_Code=%s"
    cur.execute(sql3,t1)
    b=[]
    a=cur.fetchone()
    for i in range(0,len(a)):
        b.append(a[i])
    RP=b[0]
    sql4="select Rate_D from destination where D_Code=%s"
    cur.execute(sql4,t2)
    c=[]
    e=cur.fetchone()
    for i in range(0,len(e)):
        c.append(e[i])
    RD=c[0]

    Amt=int(Wt)*int(RP)+int(RD)
    GST=Amt*18/100
    TA=Amt+GST
    st="insert into Customers(C_Name,C_Address,C_City,P_Code,D_Code,Weight,Rate_P,Rate_D,Amount,GST_18_per,Total_Amount) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    r5=(name,add,city,pc,dc,Wt,RP,RD,Amt,GST,TA)
    cur.execute(st,r5)
    mycon.commit()




#Update RECORDS
def updatedata():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost', user= 'root', passwd= '2357', database='cargodb')
   
    mycur=mycon.cursor()
    name=input("Enter the customer name:")

    t1=(name,)
    mysql_display="select * from customers where C_Name=%s"
    mycur.execute(mysql_display,t1)
    record=mycur.fetchall()
    if record!=[]:
        add=input("enter customer address")
        city=input("enter customer city")
        mysql_1="select * from product"
        cur.execute(mysql_1)
        d=cur.fetchall()
        print("**displaying data in the product**")
        for i in d:
            print(i)
        pc=input("enter p_code from above records :")
        t1=(pc,)
        mysql_2="select * from destination"
        cur.execute(mysql_2)
        d=cur.fetchall()
        print("**displaying data in the destination**")
        for i in d:
            print(i)
        dc=input("enter d_code from above records:")
        t2=(dc,)
        Wt=float(input("enter weight of goods"))
        import mysql.connector
        mycon=mysql.connector.connect(host='localhost', user= 'root', passwd= '2357', database='cargodb')
        mycur=mycon.cursor()
        sql_3="select Rate_P from product where P_Code=%s"
        cur.execute(sql_3,t1)
        b=[]
        a=cur.fetchone()
        for i in range(0,len(a)):
            b.append(a[i])
        RP=b[0]
        sql_4="select Rate_D from destination where D_Code=%s"
        cur.execute(sql_4,t2)
        c=[]
        e=cur.fetchone()
        for i in range(0,len(e)):
            c.append(e[i])
        RD=c[0]
        Amt=int(Wt)*int(RP)+int(RD)

        GST=Amt*18/100
        TA=Amt+GST


        mycon=mysql.connector.connect(host='localhost', user='root', passwd='2357', database='cargodb')
        mycur=mycon.cursor()
        sql="update customers set C_Address=%s,C_City=%s,P_Code=%s,D_Code=%s,Weight=%s,Rate_P=%s,Rate_D=%s,Amount=%s,GST_18_per=%s,Total_Amount=%s where C_Name=%s"
        t1=(add,city,pc,dc,Wt,RP,RD,Amt,GST,TA,name)
        mycur.execute(sql,t1)
        mycon.commit()
        mycon.close()

    else:
        print("Record not found")
        
    
    
    
#to delete data    
def deldata():
    
        import mysql.connector
        mycon=mysql.connector.connect(host='localhost', user='root', passwd='2357', database='cargodb')
        
        mycur=mycon.cursor()
        CID=int(input("Enter the customer id:"))
        t1=(CID,)
        
        mysql_delete="delete from customers where C_Id=%s"
        mycur.execute(mysql_delete,t1)
        mycon.commit()
        x=mycur.rowcount
        if x==1:
            print("Record deleted successfully")
        else:
            print("Record not found")
       
        mycon.close()

#to search the data
def searchdata():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost', user='root', passwd='2357', database='cargodb')
   
    mycur=mycon.cursor()
    C_Id=int(input("Enter customer id:"))
    t1=(C_Id,)
    mysql_search="select * from customers where C_Id=%s"
    mycur.execute(mysql_search,t1)
    record=mycur.fetchall()
    
    if record==[]:
        print("Record not found")
    else:
        for x in record:
            C_Id=x[0]
            C_Name=x[1]
            C_Address=x[2]
            print("Customer Id:",x[0])
            print("Customer Name:",x[1])
            print("Customer Address:",x[2])
            
    mycon.close()
# To show all records
def displayrecords():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost', user='root', passwd='2357', database='cargodb')
   
    mycur=mycon.cursor()
    mysql_display="select * from Customers"
    cur.execute(mysql_display)
    d=cur.fetchall()
    print("**displaying data in the Customers**")
    for i in d:
        print(i)


#To graphically represent product preference of Customers
def bargraph():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost', user='root', passwd='2357', database='cargodb')
    mycur=mycon.cursor()
    
    st1="select P_Code,P_Name from product order by P_Code"
    cur.execute(st1)
    d=cur.fetchall()
    Product=[]
    for i in d:
        Product.append(i[1])

    st2="select count(*) from customers group by P_Code order by P_Code"
    cur.execute(st2)
    e=cur.fetchall()
    Customer=[]
    for i in e:
        Customer.append(i[0])
    plt.figure(figsize=(12,6))
    c=['royalblue','cyan','lightsalmon','lightcoral','aquamarine']
    plt.bar(Product,Customer,color=c,width=0.3)
    plt.title("Customers' preference of types of product ")
    plt.xlabel("Type of Product")
    plt.ylabel("Number of Customers")
    plt.grid(color = 'black', alpha = 0.3, linestyle = '--', linewidth = 2)
    plt.xticks(rotation=90)
    plt.show()
        

#To graphically represent destination preference of Customers
def piechart():
    st3="select D_Code,D_Name from destination order by D_Code"
    cur.execute(st3)
    d=cur.fetchall()
    Destination=[]
    for i in d:
        Destination.append(i[1])
    st4="select count(*) from customers group by D_Code order by D_Code"
    cur.execute(st4)
    e=cur.fetchall()
    Customer=[]
    for i in e:
        Customer.append(i[0])
    explode = (0.1, 0.0, 0.2, 0.3)
    colors = ['yellowgreen', 'lightgreen', 'darkgreen', 'gold', 'red', 'lightsalmon', 'darkred']
    plt.pie(Customer, explode=explode, labels=Destination, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.legend()
    plt.show()
   
#to generate the bill
def reportgen():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost', user='root', passwd='2357', database='cargodb')
    mycur=mycon.cursor()
    C_Id=int(input("Enter the customer id:"))
    t1=(C_Id,)
    mysql_display="select * from customers where C_Id=%s"
    mycur.execute(mysql_display,t1)
    record=mycur.fetchall()
#to find the bill generated date and due date.
    from datetime import date, timedelta
    day=date.today()+timedelta(7)
    day1=date.today()+timedelta(15)
    if record==[]:
        print("Record not found")
    else:
        for x in record:
            C_Id=x[0]
            C_Name=x[1]
            C_Address=x[2]
            
            P_Code=x[4]
            D_Code=x[5]
            Weight=x[6]
            Rate_P=x[7]
            Rate_D=x[8]
            Amount=x[9]
            GST_18_per=x[10]
            Total_Amount=x[11]
            print("")
            print("")
            print("")
            print("-------------------------------------------------------------")
            print("******************Pacific Cargo Shipment**************")
            print("******************DELHI*******************")
            print("**************Email:Pacific_Cargo_Shipmentbilling@gmail.com*********** ")
            print("**************Telephone No.:01123965784******************")
            print("")
            print("=============================================================\n")
            print(" CUSTOMER INFORMATION   ")
            print(" CUSTOMER ID:",C_Id)
            print(" NAME:",C_Name)
            print(" ADDRESS:",C_Address,"\n\n")
            print("=============================================================\n")
            print(" PRODUCT CODE:",P_Code)
            print(" DESTINATION CODE:",D_Code)
            print(" WEIGHT IN Kg ",Weight)
            print(" RATE OF PRODUCT PER Kg",Rate_P)
            print(" DELIVERY CHARGES: Rs",Rate_D)
            print(" AMOUNT: Rs",Amount)
            print(" GST: Rs",GST_18_per)
            print("=============================================================\n")
            print(" TOTAL AMOUNT: Rs",Total_Amount)
            print(" BILL GENERATED ON:",date.today(),"\n")
            print("Please pay the dues within 7 days of bill generated date to avoid any inconvenience \n")
            print("=============================================================")            

            

 #__main__ Starts__From__Here
while True:
    print("\n\t********************WELCOME TO PACIFIC CARGO SHIPMENT BILLING SYSTEM*****************\n")
    print("\t\t\t******************MAIN MENU*********************\n")
    print("\t\tPRESS:1 for Inserting Record ")
    print("\t\tPRESS:2 for Updating Record")
    print("\t\tPRESS:3 for Deleting Record")
    print("\t\tPRESS:4 for Searching Record")
    print("\t\tPRESS:5 for Displaying Records")
    print("\t\tPRESS:6 for Graphical representation of products preferred by customers")
    print("\t\tPRESS:7 for Graphical representation of destinations preferred by customers\n")
    print("\t\tPRESS:8 for Generating Bill\n")
    print("\t\tPRESS:9 for Quit\n")
    choice = input("What would you like choose: ")
    if choice == '1':
        adddata()
    elif choice == '2':
        updatedata()
    elif choice == '3':
        deldata()
    elif choice == '4':
        searchdata()
    elif choice == '5':
        displayrecords()
    elif choice == '6':
        bargraph()
    elif choice == '7':
        piechart()
    elif choice == '8':
        reportgen()
    
    elif choice not in ['1','2','3','4','5','6','7','8']:
        break
    
#while-end 
#mainprogram ends


mycon.commit()
mycon.close()

print("*************************************************THE END!*****************************************************************************")





    
    
