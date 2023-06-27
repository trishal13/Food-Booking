#-----------------------------FOOD BOOKING CODE------------------------------#

import os
from dotenv import load_dotenv
import random
import mysql.connector as sql

load_dotenv()

mycon=sql.connect(host='localhost',user=os.getenv('username'),passwd=os.getenv('password'),charset='utf8',database='FOOD_BOOKING')
cursor=mycon.cursor()

def NEW_CUSTOMER():          #-----SIGN IN-----#
    p=input("PROCEED [y] / [n] : ")
    if p=='N' or p=='n':
        print('-'*40)
        q=int(input("NEW USER [1] / ALREADY REGISTERED USER [2] : "))
        NEW_OR_NOT(q)
    elif p=='Y' or p=='y':
        print()
        print("CREATE AN ACCOUNT NOW !!")
        name=input("NAME : ")
        email=input("E-MAIL ID : ")
        phone=input("MOBILE NUMBER : ")
        add=input("ADDRESS : ")
        id=input("SET USERNAME : ")
        passwd=input("SET PASSWORD : ")
        id_detail="SELECT * FROM CUSTOMER WHERE ID='{}'".format(id)
        cursor.execute(id_detail)
        data=cursor.fetchall()
        if data==[]:
            c_detail="INSERT INTO CUSTOMER(NAME,EMAIL,PHONE,ADDRESS,ID,PASSWORD) VALUES('{}','{}','{}','{}','{}','{}')".format(name,email,phone,add,id,passwd)
            cursor.execute(c_detail)
            mycon.commit()
            print()
            print("NOW YOU CAN RUN THIS PROGRAM AGAIN AND LOGIN.")
            mycon.close()
        else:
            print()
            print("USERNAME ALREADY IN USE.")
            print('-'*40)
            M_CHOICE()
    else:
        print('-'*40)
        NEW_CUSTOMER()
    
def U_CUSTOMER(a,b):          #-----UPDATING CUSTOMER DETAILS-----#
    cursor.execute("SELECT * FROM CUSTOMER")
    data=cursor.fetchall()
    n=len(data)
    for i in range(n):
        t=data[i]
        if a==t[0]:
            id=input("USERNAME : ")
            u_detail="UPDATE CUSTOMER SET NAME='{}' WHERE NAME='{}' AND ID='{}'".format(b,a,id)
            cursor.execute(u_detail)
            mycon.commit()
            print()
            print("YOUR NAME IS UPDATED.")
            print()
        elif a==t[1]:
            id=input("USERNAME : ")
            u_detail="UPDATE CUSTOMER SET EMAIL='{}' WHERE EMAIL='{}' AND ID='{}'".format(b,a,id)
            cursor.execute(u_detail)
            mycon.commit()
            print()
            print("YOUR E-MAIL ID IS UPDATED.")
            print()
        elif a==t[2]:
            id=input("USERNAME : ")
            u_detail="UPDATE CUSTOMER SET PHONE='{}' WHERE PHONE='{}' AND ID='{}'".format(b,a,id)
            cursor.execute(u_detail)
            mycon.commit()
            print()
            print("YOUR MOBILE NUMBER IS UPDATED.")
            print()
        elif a==t[3]:
            id=input("USERNAME : ")
            u_detail="UPDATE CUSTOMER SET ADDRESS='{}' WHERE ADDRESS='{}' AND ID='{}'".format(b,a,id)
            cursor.execute(u_detail)
            mycon.commit()
            print()
            print("YOUR ADDRESS IS UPDATED.")
            print()
        elif a==t[4]:
            u_detail="UPDATE CUSTOMER SET ID='{}' WHERE ID='{}'".format(b,a)
            cursor.execute(u_detail)
            mycon.commit()
            u_detail="UPDATE ORDERS SET CID='{}' WHERE CID='{}'".format(b,a)
            cursor.execute(u_detail)
            mycon.commit()
            print()
            print("YOUR USERNAME IS UPDATED.")
            print()
        elif a==t[5]:
            id=input("USERNAME : ")
            u_detail="UPDATE CUSTOMER SET PASSWORD='{}' WHERE PASSWORD='{}' AND ID='{}'".format(b,a,id)
            cursor.execute(u_detail)
            mycon.commit()
            print()
            print("YOUR PASSWORD IS UPDATED.")
            print()
        
def C_UPDATE():          #-----UPDATE CUSTOMER DETAILS-----#
    print()
    print("1. NAME")
    print("2. E-MAIL ID")
    print("3. MOBILE NUMBER")
    print("4. ADDRESS")
    print("5. USERNAME")
    print("6. PASSWORD")
    a=input("WHAT DO YOU WANT TO UPDATE : ")
    if a=='1':
        old_name=input("CURRENT NAME : ")
        new_name=input("NEW NAME : ")
        n_detail="SELECT NAME FROM CUSTOMER WHERE NAME='{}'".format(old_name)
        cursor.execute(n_detail)
        data=cursor.fetchall()
        if data==[]:
            print()
            print("INVALID NAME.")
            print()
        else:     
            U_CUSTOMER(old_name,new_name)
    elif a=='2':
        old_email=input("CURRENT E-MAIL ID : ")
        new_email=input("NEW E-MAIL ID : ")
        e_detail="SELECT EMAIL FROM CUSTOMER WHERE EMAIL='{}'".format(old_email)
        cursor.execute(e_detail)
        data=cursor.fetchall()
        if data==[]:
            print()
            print("INVALID E-MAIL ID.")
            print()
        else:     
            U_CUSTOMER(old_email,new_email)
    elif a=='3':
        old_phone=(input("CURRENT MOBILE NUMBER : "))
        new_phone=(input("NEW MOBILE NUMBER : "))
        p_detail="SELECT PHONE FROM CUSTOMER WHERE PHONE='{}'".format(old_phone)
        cursor.execute(p_detail)
        data=cursor.fetchall()
        if data==[]:
            print()
            print("INVALID MOBILE NUMBER.")
            print()
        else:     
            U_CUSTOMER(old_phone,new_phone)
    elif a=='4':
        old_add=input("CURRENT ADDRESS : ")
        new_add=input("NEW ADDRESS : ")
        a_detail="SELECT ADDRESS FROM CUSTOMER WHERE ADDRESS='{}'".format(old_add)
        cursor.execute(a_detail)
        data=cursor.fetchall()
        if data==[]:
            print()
            print("INVALID ADDRESS.")
            print()
        else:     
            U_CUSTOMER(old_add,new_add)
    elif a=='5':
        old_id=input("CURRENT USERNAME : ")
        new_id=input("NEW USERNAME : ")
        un_detail="SELECT ID FROM CUSTOMER WHERE ID='{}'".format(old_id)
        cursor.execute(un_detail)
        data=cursor.fetchall()
        if data==[]:
            print()
            print("INVALID USERNAME.")
            print()
        else:     
            U_CUSTOMER(old_id,new_id)
    elif a=='6':
        old_passwd=input("CURRENT PASSWORD : ")
        new_passwd=input("NEW PASSWORD : ")
        pw_detail="SELECT PASSWORD FROM CUSTOMER WHERE PASSWORD='{}'".format(old_passwd)
        cursor.execute(pw_detail)
        data=cursor.fetchall()
        if data==[]:
            print()
            print("INVALID PASSWORD.")
            print()
        else:     
            U_CUSTOMER(old_passwd,new_passwd)
    else:
        print()
        print("INVALID INPUT.")
        print() 
        C_MENU()
        q=input("WHAT TO DO : ")
        C_OPTIONS(q) 

def C_DETAILS():          #-----CUSTOMER DETAILS-----#
    cursor.execute("SELECT * FROM CUSTOMER")
    data=cursor.fetchall()
    if data==[]:
        print()
        print("NO CUSTOMERS.")
        print()
    else:
        for i in data:
            print()
            print(i)
            print()
            
def O_CANCEL(a):          #-----ORDER CANCELLING-----#
    cursor.execute("SELECT * FROM ORDERS WHERE OID={}".format(a))
    data=cursor.fetchall()
    if data==[]:
        print()
        print("INVALID ORDER ID.")
        print()
    else:
        t=data[0]
        i_order="INSERT INTO CANCELLED_ORDERS VALUES('{}','{}',{},'{}','{}')".format(t[0],t[1],t[2],t[3],t[4])
        cursor.execute(i_order)
        mycon.commit()
        c_order="DELETE FROM ORDERS WHERE OID={}".format(a)
        cursor.execute(c_order)
        mycon.commit()
        print()
        print("YOUR ORDER HAS BEEN CANCELLED.")
        print()
            
def CANCELLED_ORDERS():          #-----CANCELLED ORDERS-----#
    cursor.execute("SELECT * FROM CANCELLED_ORDERS")
    data=cursor.fetchall()
    if data==[]:
        print()
        print("NO CANCELLED ORDERS.")
        print()
    else:
        for i in data:
            print()
            print(i)
            print()
        
def O_ENTRY():          #-----PLACE ORDER-----#
    c_id=input("USERNAME : ")
    id_check="SELECT * FROM CUSTOMER WHERE ID='{}'".format(c_id)
    cursor.execute(id_check)
    data=cursor.fetchall()
    if data==[]:
        print()
        print("INVALID USERNAME.")
        print()
    else:
        o_date=input("DATE (DD) : ")
        o_month=input("MONTH (MM) : ")
        o_year=input("YEAR (YYYY) : ")
        date=o_date+":"+o_month+":"+o_year
        o_restaurant=input("RESTAURANT : ")
        o_food=input("FOOD : ")
        print()
        print("YOUR ORDER HAS BEEN PLACED SUCCESSFULLY !!!")
        o_id=str(random.randint(0,1000000000))
        o_id_check="SELECT * FROM ORDERS WHERE OID='{}'".format(o_id)
        cursor.execute(o_id_check)
        data=cursor.fetchall()
        while data!=[]:
            o_id=str(random.randint(0,1000000000))
        else:
            print()
            print("ORDER ID : ",o_id)
            print()
            o_detail="INSERT INTO ORDERS(CID,RESTAURANT,OID,DATE,FOOD) VALUES('{}','{}','{}','{}','{}')".format(c_id,o_restaurant,o_id,date,o_food)
            cursor.execute(o_detail)
            mycon.commit()
            
def O_DETAILS():          #-----ORDER DETAILS-----#
    cursor.execute("SELECT * FROM ORDERS")
    data=cursor.fetchall()
    if data==[]:
        print()
        print("NO ORDERS.")
        print()
    else:
        for i in data:
            print()
            print(i)
            print()
        
def O_UPDATE(x):          #-----UPDATE ORDER-----#
    o_detail="SELECT * FROM ORDERS WHERE OID='{}'".format(x)
    cursor.execute(o_detail)
    data=cursor.fetchall()
    if data==[]:
        print()
        print('INVALID ORDER ID.')
        print()
    else:
        print()
        print("CURRENT ORDER : ")
        print()
        print(data)
        U_ORDER(x)
    
def U_ORDER(x):          #-----UPDATING ORDER-----#
    print()
    print("RESTAURANT [1] / DATE[2] / FOOD [3]")
    ch=input("WHAT DO YOU WANT TO UPDATE : ")
    if ch=='1':
        old_restaurant=input("CURRENT RESTAURANT : ")
        new_restaurant=input("NEW RESTAURANT : ")
        o_detail="SELECT * FROM ORDERS WHERE RESTAURANT='{}' AND OID='{}'".format(old_restaurant,x)
        cursor.execute(o_detail)
        data=cursor.fetchall()
        if data==[]:
            print()
            print("INVALID RESTAURANT.")
            print()
        else:
            u_detail="UPDATE ORDERS SET RESTAURANT='{}' WHERE RESTAURANT='{}' AND OID='{}'".format(new_restaurant,old_restaurant,x)
            cursor.execute(u_detail)
            mycon.commit()
            print()
            print("YOUR ORDER IS UPDATED.")
            print()
    elif ch=='2':
        old_date=input("CURRENT DATE (DD) : ")
        old_month=input("CURRENT MONTH (MM) : ")
        old_year=input("CURRENT YEAR (YYYY) : ")
        o_date=old_date+':'+old_month+':'+old_year
        new_date=input("NEW DATE (DD) : ")
        new_month=input("NEW MONTH (MM) : ")
        new_year=input("NEW YEAR (YYYY) : ")
        n_date=new_date+':'+new_month+':'+new_year
        o_detail="SELECT * FROM ORDERS WHERE DATE='{}' AND OID='{}'".format(o_date,x)
        cursor.execute(o_detail)
        data=cursor.fetchall()
        if data==[]:
            print()
            print("INVALID DATE.")
            print()
        else:
            u_detail="UPDATE ORDERS SET DATE='{}' WHERE DATE='{}' AND OID='{}'".format(n_date,o_date,x)
            cursor.execute(u_detail)
            mycon.commit()
            print()
            print("YOUR ORDER IS UPDATED.")
            print()
    elif ch=='3':
        old_food=input("CURRENT FOOD : ")
        new_food=input("NEW FOOD : ")
        o_detail="SELECT * FROM ORDERS WHERE FOOD='{}' AND OID='{}'".format(old_food,x)
        cursor.execute(o_detail)
        data=cursor.fetchall()
        if data==[]:
            print()
            print("INVALID FOOD.")
            print()
        else:
            u_detail="UPDATE ORDERS SET FOOD='{}' WHERE FOOD='{}' AND OID='{}'".format(new_food,old_food,x)
            cursor.execute(u_detail)
            mycon.commit()
            print()
            print("YOUR ORDER IS UPDATED.")
            print()
    else:
        print()
        print("INVALID INPUT.")
        print()

def C_DELETE():          #-----DELETE ACCOUNT-----#
    c_id=input("USERNAME : ")
    c_passwd=input("PASSWORD : ")
    c_detail="SELECT * FROM CUSTOMER WHERE ID='{}' AND PASSWORD='{}'".format(c_id,c_passwd)
    cursor.execute(c_detail)
    data=cursor.fetchall()
    if data==[]:
        print()
        print("INVALID ID / PASSWORD.")
        C_PROCEED()
    else:
        for i in data:
            i_delete="INSERT INTO DELETE_ACCOUNT VALUES('{}','{}','{}','{}','{}','{}')".format(i[0],i[1],i[2],i[3],i[4],i[5])
            cursor.execute(i_delete)
            mycon.commit()
            c_delete="DELETE FROM CUSTOMER WHERE ID='{}' AND PASSWORD='{}'".format(c_id,c_passwd)
            cursor.execute(c_delete)
            mycon.commit()
            print()
            print("ACCOUNT DELETED.")
        print("-"*40)
        M_CHOICE()
            
def DELETED_ACCOUNTS():          #-----DELETED ACCOUNTS-----#
    cursor.execute("SELECT * FROM DELETE_ACCOUNT")
    data=cursor.fetchall()
    if data==[]:
        print()
        print("NO DELETED ACCOUNTS.")
        print()
    else:
        for i in data:
            print()
            print(i)
            print()
        
def C_ORDERS():          #-----CUSTOMER ORDERS-----#
    c_id=input("USERNAME : ")
    cursor.execute("SELECT * FROM CUSTOMER WHERE ID='{}'".format(c_id))
    data=cursor.fetchall()
    if data==[]:
        print()
        print("INVALID USERNAME.")
        print() 
        C_MENU()
        q=int(input("WHAT TO DO : "))
        C_OPTIONS(q) 
    else:
        cursor.execute("SELECT * FROM ORDERS WHERE CID='{}'".format(c_id))
        data=cursor.fetchall()
        if data==[]:
            print()
            print("YOU HAVE NOT ORDERED ANYTHING YET.")
            print()
        else:
            for i in data:    
                print()
                print(i)
                print()
                
def C_SELECT():          #-----SELECT CUSTOMER-----#
    id=input("CUSTOMER ID : ")
    c_select="SELECT * FROM CUSTOMER WHERE ID='{}'".format(id)
    cursor.execute(c_select)
    data=cursor.fetchall()
    if data==[]:
        print()
        print("NO CUSTOMER WITH ID :",id)
        print()
    else:
        print()
        print(data)
        print()

def O_SELECT():          #-----ORDER SELECT-----#
    print()
    print("CUSTOMER'S ORDER [1] / SPECIFIC ORDER [2]")
    k=input("CHOICE : ")
    if k=='1':
        id=input("CUSTOMER ID : ")
        o_select="SELECT * FROM ORDERS WHERE CID='{}'".format(id)
        cursor.execute(o_select)
        data=cursor.fetchall()
        if data==[]:
            print()
            print("NO ORDERS OF CUSTOMER WITH CUSTOMER ID :",id)
            print()
        else:
            for i in data:
                print()
                print(i)
                print()
    elif k=='2':
        o_id=input("ORDER ID : ")
        o_select="SELECT * FROM ORDERS WHERE OID='{}'".format(o_id)
        cursor.execute(o_select)
        data=cursor.fetchall()
        if data==[]:
            print()
            print("NO ORDERS WITH ORDER ID :",o_id)
            print()
        else:
            print()
            print(data)
            print()
    else:
        print()
        print("INVALID CHOICE")
        print()
        
def SEND_MESSAGE():          #-----SEND MESSAGE-----#
    id=input("CUSTOMER ID : ")
    id_check="SELECT * FROM CUSTOMER WHERE ID='{}'".format(id)
    cursor.execute(id_check)
    data=cursor.fetchall()
    if data==[]:
        print()
        print("INVALID CUSTOMER ID.")
        print()
    else:
        date=input("DATE (DD) : ")
        month=input("MONTH (MM) : ")
        year=input("YEAR (YYYY) : ")
        n_date=date+':'+month+':'+year
        message=input("TYPE MESSAGE : ")
        notification=message+" DATE : "+n_date
        s_message="INSERT INTO MESSAGE VALUES('{}','{}')".format(id,notification)
        cursor.execute(s_message)
        mycon.commit()
        print()
        print("MESSAGE SENT SUCCESSFULLY.")
        print()
        
def SENT_MESSAGE():          #-----SENT MESSAGE-----#
    s_message="SELECT * FROM MESSAGE"
    cursor.execute(s_message)
    data=cursor.fetchall()
    if data==[]:
        print()
        print("NO SENT MESSAGE.")
        print()
    else:
        for i in range(len(data)):            
            print('-'*40)
            print(i+1,".",data[i][0],":",data[i][1])
            print()
        
def VIEW_MESSAGE():          #-----VIEW NOTIFICATIONS-----#
    id=input("USERNAME : ")
    id_check="SELECT * FROM CUSTOMER WHERE ID='{}'".format(id)
    cursor.execute(id_check)
    data=cursor.fetchall()
    if data==[]:
        print()
        print("INVALID USERNAME.")
        print()
    else:
        v_message="SELECT MESSAGE FROM MESSAGE WHERE ID='{}'".format(id)
        cursor.execute(v_message)
        data=cursor.fetchall()
        if data==[]:
            print()
            print("NO NOTIFICATIONS.")
            print()
        else:
            n=len(data)
            for i in range(n):
                print('-'*40)
                print(i+1,".",data[i][0])
                print()

def C_VALIDITY():          #-----CUSTOMER VALIDITY-----#
    id=input("CUSTOMER ID : ")
    id_check="SELECT * FROM CUSTOMER WHERE ID='{}'".format(id)
    cursor.execute(id_check)
    data=cursor.fetchall()
    if data==[]:
        print()
        print("NO CUSTOMER WITH CUSTOMER ID :",id)
        print()
    else:
        print()
        print(data)
        if data[0][6]==None:
            t=data[0]
            validity=input("VALID[1] / INVALID[2] : ")
            if validity=='1':
                d_valid="DELETE FROM CUSTOMER WHERE ID='{}'".format(id)
                cursor.execute(d_valid)
                mycon.commit()
                i_valid="INSERT INTO CUSTOMER VALUES('{}','{}','{}','{}','{}','{}','{}')".format(t[0],t[1],t[2],t[3],t[4],t[5],'VALID')
                cursor.execute(i_valid)
                mycon.commit()
                print()
                print("CUSTOMER STATUS UPDATED.")
                print()
            elif validity=='2':
                d_valid="DELETE FROM CUSTOMER WHERE ID='{}'".format(id)
                cursor.execute(d_valid)
                mycon.commit()
                i_valid="INSERT INTO CUSTOMER VALUES('{}','{}','{}','{}','{}','{}','{}')".format(t[0],t[1],t[2],t[3],t[4],t[5],'INVALID')
                cursor.execute(i_valid)
                mycon.commit()
                print()
                print("CUSTOMER STATUS UPDATED.")
                print()
            else:
                print()
                print("INVALID INPUT.")
                print()
        else:
            old_validity=input("CURRENT VALIDITY : ")
            new_validity=input("NEW VALIDITY : ")
            v_check="SELECT STATUS FROM CUSTOMER WHERE ID='{}' AND STATUS='{}'".format(id,old_validity)
            cursor.execute(v_check)
            data=cursor.fetchall()
            if data==[]:
                print()
                print("NO CUSTOMER WITH ID :",id,"AND STATUS :",old_validity)
                print()            
            else:
                u_valid="UPDATE CUSTOMER SET STATUS='{}' WHERE ID='{}' AND STATUS='{}'".format(new_validity,id,old_validity)
                cursor.execute(u_valid)
                mycon.commit()
                print()
                print("CUSTOMER STATUS UPDATED.")
                print()

def O_VALIDITY():          #-----ORDER VALIDITY-----#
    o_id=input("ORDER ID : ")
    check="SELECT * FROM ORDERS WHERE OID='{}'".format(o_id)
    cursor.execute(check)
    data=cursor.fetchall()
    if data==[]:
        print()
        print("NO ORDERS WITH ORDER ID :",o_id)
        print()
    else:
        print()
        print(data)
        if data[0][5]==None:
            t=data[0]
            status=input("STATUS : ")
            d_valid="DELETE FROM ORDERS WHERE OID='{}'".format(o_id)
            cursor.execute(d_valid)
            mycon.commit()
            i_valid="INSERT INTO ORDERS VALUES('{}','{}','{}','{}','{}','{}')".format(t[0],t[1],t[2],t[3],t[4],status)
            cursor.execute(i_valid)
            mycon.commit()
            print()
            print("ORDER STATUS UPDATED.")
            print()
        else:
            old_validity=input("CURRENT VALIDITY : ")
            new_validity=input("NEW VALIDITY : ")
            v_check="SELECT STATUS FROM ORDERS WHERE OID='{}' AND STATUS='{}'".format(o_id,old_validity)
            cursor.execute(v_check)
            data=cursor.fetchall()
            if data==[]:
                print()
                print("NO ORDERS WITH ID :",id,"AND STATUS :",old_validity)
                print()            
            else:
                u_valid="UPDATE ORDERS SET STATUS='{}' WHERE OID='{}' AND STATUS='{}'".format(new_validity,o_id,old_validity)
                cursor.execute(u_valid)
                mycon.commit()
                print()
                print("ORDER STATUS UPDATED.")
                print()
    
def M_MENU():          #-----MANAGEMENT MENU-----#
    print("1. CUSTOMER DETAILS")
    print("2. ORDERS")
    print("3. SELECT CUSTOMER")
    print("4. SELECT ORDER")
    print("5. CANCELLED ORDERS")
    print("6. DELETED ACCOUNTS")
    print("7. SEND MESSAGE")
    print("8. SENT MESSAGES")
    print("9. CUSTOMER VALIDITY")
    print("10. ORDER STATUS")
    print("11. LOG OUT")

def M_BACK():          #-----MANAGEMENT BACK-----#
    print('-'*40)
    M_MENU()
    q=input("WHAT TO DO : ")
    M_OPTIONS(q)

def M_PROCEED():          #-----MANAGEMENT PROCEED-----#
    print('-'*40)
    M_MENU()
    a=input("ANYTHING MORE : ")
    M_OPTIONS(a)

def M_OPTIONS(q):          #-----MANAGEMENT OPTIONS-----#
    if q=='1':
        p=input("PROCEED [y] / [n] : ")
        if p=='n' or p=='N':
            M_BACK()
        elif p=='y' or p=='Y':
            C_DETAILS()
            M_PROCEED()
        else:
            print('-'*40)
            M_OPTIONS('1')
    elif q=='2':
        p=input("PROCEED [y] / [n] : ")
        if p=='n' or p=='N':
            M_BACK()
        elif p=='y' or p=='Y':
            O_DETAILS()
            M_PROCEED()
        else:
            print('-'*40)
            M_OPTIONS('2')
    elif q=='3':
        p=input("PROCEED [y] / [n] : ")
        if p=='n' or p=='N':
            M_BACK()
        elif p=='y' or p=='Y':
            C_SELECT()
            M_PROCEED()
        else:
            print('-'*40)
            M_OPTIONS('3')
    elif q=='4':
        p=input("PROCEED [y] / [n] : ")
        if p=='n' or p=='N':
            M_BACK()
        elif p=='y' or p=='Y':
            O_SELECT()
            M_PROCEED()
        else:
            print('-'*40)
            M_OPTIONS('4')
    elif q=='5':
        p=input("PROCEED [y] / [n] : ")
        if p=='n' or p=='N':
            M_BACK()
        elif p=='y' or p=='Y':
            CANCELLED_ORDERS()
            M_PROCEED()
        else:
            print('-'*40)
            M_OPTIONS('5')
    elif q=='6':
        p=input("PROCEED [y] / [n] : ")
        if p=='n' or p=='N':
            M_BACK()
        elif p=='y' or p=='Y':
            DELETED_ACCOUNTS()
            M_PROCEED()
        else:
            print('-'*40)
            M_OPTIONS('6')
    elif q=='7':
        p=input("PROCEED [y] / [n] : ")
        if p=='n' or p=='N':
            M_BACK()
        elif p=='y' or p=='Y':
            SEND_MESSAGE()
            M_PROCEED()
        else:
            print('-'*40)
            M_OPTIONS('7')
    elif q=='8':
        p=input("PROCEED [y] / [n] : ")
        if p=='n' or p=='N':
            M_BACK()
        elif p=='y' or p=='Y':
            SENT_MESSAGE()
            M_PROCEED()
        else:
            print('-'*40)
            M_OPTIONS('8')
    elif q=='9':
        p=input("PROCEED [y] / [n] : ")
        if p=='n' or p=='N':
            M_BACK()
        elif p=='y' or p=='Y':
            C_VALIDITY()
            M_PROCEED()
        else:
            print('-'*40)
            M_OPTIONS('9')
    elif q=='10':
        p=input("PROCEED [y] / [n] : ")
        if p=='n' or p=='N':
            M_BACK()
        elif p=='y' or p=='Y':
            O_VALIDITY()
            M_PROCEED()
        else:
            print('-'*40)
            M_OPTIONS(10)
    elif q=='11':
        print()
        print("SUCCESSFULLY LOGGED OUT.")
        print('-'*40)
        M_CHOICE()
    else:
        print()
        print("INVALID INPUT.")
        b=input("Enter only from 1-11 : ")
        M_OPTIONS(b)
        
def C_MENU():          #-----CUSTOMER MENU-----#
    print("1. PLACE ORDER")
    print("2. YOUR ORDERS")
    print("3. CANCEL ORDER")
    print("4. UPDATE ORDER")
    print("5. UPDATE YOUR DETAILS")
    print("6. DELETE ACCOUNT")
    print("7. NOTIFICATIONS")
    print("8. LOG OUT")

def C_BACK():          #-----CUSTOMER BACK-----#
    print('-'*40) 
    C_MENU()
    q=input("WHAT TO DO : ")
    C_OPTIONS(q) 
    
def C_PROCEED():          #-----CUSTOMER PROCEED-----#
    print('-'*40)
    C_MENU()
    a=input("ANYTHING MORE : ")
    C_OPTIONS(a)
    
def C_OPTIONS(q):          #-----CUSTOMER OPTIONS-----#
    if q=='1':
        p=input("PROCEED [y] / [n] : ")
        if p=='n' or p=='N':
            C_BACK()
        elif p=='y' or p=='Y':
           O_ENTRY()
           C_PROCEED()
        else:
            print('-'*40)
            C_OPTIONS('1')
    elif q=='2':
        p=input("PROCEED [y] / [n] : ")
        if p=='n' or p=='N':
            C_BACK()
        elif p=='y' or p=='Y':
           C_ORDERS()
           C_PROCEED()
        else:
            print('-'*40)
            C_OPTIONS('2')
    elif q=='3':
        p=input("PROCEED [y] / [n] : ")
        if p=='n' or p=='N':
            C_BACK()
        elif p=='y' or p=='Y':
           o_id=input("ORDER ID : ")
           O_CANCEL(o_id)
           C_PROCEED()
        else:
            print('-'*40)
            C_OPTIONS('3')
    elif q=='4':
        p=input("PROCEED [y] / [n] : ")
        if p=='n' or p=='N':
            C_BACK()
        elif p=='y' or p=='Y':
           o_id=input("ORDER ID : ")
           O_UPDATE(o_id)
           C_PROCEED()
        else:
            print('-'*40)
            C_OPTIONS('4')
    elif q=='5':
        p=input("PROCEED [y] / [n] : ")
        if p=='n' or p=='N':
            C_BACK()
        elif p=='y' or p=='Y':
           C_UPDATE()
           C_PROCEED()
        else:
            print('-'*40)
            C_OPTIONS('5')
    elif q=='6':
        p=input("PROCEED [y] / [n] : ")
        if p=='n' or p=='N':
            C_BACK()
        elif p=='y' or p=='Y':
           C_DELETE()
        else:
            print('-'*40)
            C_OPTIONS('6')
    elif q=='7':
        p=input("PROCEED [y] / [n] : ")
        if p=='n' or p=='N':
            C_BACK()
        elif p=='y' or p=='Y':
           VIEW_MESSAGE()
           C_PROCEED()
        else:
            print('-'*40)
            C_OPTIONS('7')
    elif q=='8':
        print()
        print("SUCCESSFULLY LOGGED OUT.")
        print('-'*40)
        M_CHOICE()
    else:
        print()
        print("INVALID INPUT.")
        b=input("Enter only from 1-8 : ")
        C_OPTIONS(b)

def MANAGEMENT():          #-----MANAGEMENT SYSTEM-----#
    m_id=input("USERNAME : ")
    m_passwd=input("PASSWORD : ")
    cursor.execute("SELECT * FROM MANAGEMENT WHERE ID='{}' AND PASSWORD='{}'".format(m_id,m_passwd))
    data=cursor.fetchall()
    if data==[]:
        print()
        print("INVALID ID/PASSWORD.")
        print('-'*40)
        M_CHOICE()
    else:
        st="SELECT NAME FROM MANAGEMENT WHERE ID='{}'".format(m_id)
        cursor.execute(st)
        data=cursor.fetchall()
        print()
        print("WELCOME",data[0][0])
        print('-'*40)        
        print()
        M_MENU()
        q=input("WHAT TO DO : ")
        M_OPTIONS(q)

def CUSTOMER():          #-----CUSTOMER LOGIN-----#
    p=input("PROCEED [y] / [n] : ")
    if p=='N' or p=='n':
        print('-'*40)
        q=input("NEW USER [1] / ALREADY REGISTERED USER [2] : ")
        NEW_OR_NOT(q)
    elif p=='y' or p=='Y':
        print()
        print("LOG IN [1] / FORGOT PASSWORD [2] / FORGOT USERNAME [3]")
        g=input("CHOICE : ")
        if g=='1':
            c_id=input("USERNAME : ")
            c_passwd=input("PASSWORD : ")
            cursor.execute("SELECT * FROM CUSTOMER WHERE ID='{}' AND PASSWORD='{}'".format(c_id,c_passwd))
            data=cursor.fetchall()
            if data==[]:
                print()
                print("INVALID ID/PASSWORD.")
                print('-'*40)
                M_CHOICE()
            elif data[0][6]=='INVALID':
                print()
                print("YOUR THIS ACCOUNT DETAILS WERE INVALID SO THIS ACCOUNT CANNOT BE USED NOW.")
                print('-'*40)
                M_CHOICE()
            else:
                st="SELECT NAME FROM CUSTOMER WHERE ID='{}'".format(c_id)
                cursor.execute(st)
                data=cursor.fetchall()
                print()
                print("WELCOME",data[0][0])
                print('-'*40)
                C_MENU()
                q=input("WHAT TO DO : ")
                C_OPTIONS(q)
        elif g=='2':
            f_email=input("E-MAIL ID : ")
            f_phone=input("MOBILE NUMBER : ")
            f_detail="SELECT PASSWORD FROM CUSTOMER WHERE EMAIL='{}' AND PHONE='{}'".format(f_email,f_phone)
            cursor.execute(f_detail)
            data=cursor.fetchall()
            if data==[]:
                print()
                print("INVALID E-MAIL ID / MOBILE NUMBER.")
                print('-'*40)
                M_CHOICE()
            else:
                new_passwd=input("NEW PASSWORD : ")
                f_update="UPDATE CUSTOMER SET PASSWORD='{}' WHERE EMAIL='{}' AND PHONE='{}'".format(new_passwd,f_email,f_phone)
                cursor.execute(f_update)
                mycon.commit()
                print()
                print("YOUR PASSWORD IS UPDATED.")
                print()
                print("NOW YOU CAN RUN THIS PROGRAM AGAIN AND LOGIN.")
        elif g=='3':
            f_email=input("E-MAIL ID : ")
            f_phone=input("MOBILE NUMBER : ")
            f_detail="SELECT ID FROM CUSTOMER WHERE EMAIL='{}' AND PHONE='{}'".format(f_email,f_phone)
            cursor.execute(f_detail)
            data=cursor.fetchall()
            if data==[]:
                print()
                print("INVALID E-MAIL ID / MOBILE NUMBER.")
                print('-'*40)
                M_CHOICE()
            else:
                new_id=input("NEW USERNAME : ")
                f_update="UPDATE CUSTOMER SET ID='{}' WHERE EMAIL='{}' AND PHONE='{}'".format(new_id,f_email,f_phone)
                cursor.execute(f_update)
                mycon.commit()
                o_cid="SELECT ID FROM CUSTOMER WHERE EMAIL='{}' AND PHONE='{}'".format(f_email,f_phone)
                cursor.execute(o_cid)
                data=cursor.fetchall()
                if data==[]:
                    pass
                else:
                    cid_update="UPDATE ORDERS SET CID='{}' WHERE CID='{}'".format(data[0][0],new_id)
                    cursor.execute(cid_update)
                    mycon.commit()
                print()
                print("YOUR USERNAME IS UPDATED.")
                print()
                print("NOW YOU CAN RUN THIS PROGRAM AGAIN AND LOGIN.")
        else:
            print()
            print("INVALID CHOICE.")
            print('-'*40)
            M_CHOICE()
    else:
        print('-'*40)
        CUSTOMER()

def NEW_OR_NOT(q):          #-----NEW USER OR ALREADY REGISTERED USER-----#
    if q=='1':
        NEW_CUSTOMER()
    elif q=='2':
        CUSTOMER()
    else:
        print()
        print("INVALID INPUT.")
        q=input("Enter only 1/2 : ")
        NEW_OR_NOT(q)

def MAIN(ch):          #-----MAIN-----#
    if ch=='1':
        p=input("PROCEED [y] / [n] : ")
        if p=='N' or p=='n':
            print('-'*40)
            M_CHOICE()
        elif p=='y' or p=='Y':
            q=input("NEW USER [1] / ALREADY REGISTERED USER [2] : ")
            NEW_OR_NOT(q)
        else:
            print('-'*40)
            MAIN('1')
    elif ch=='2':
        p=input("PROCEED [y] / [n] : ")
        if p=='N' or p=='n':
            print('-'*40)
            M_CHOICE()
        elif p=='y' or p=='Y':
            MANAGEMENT()
        else:
            print('-'*40)
            MAIN('2')
    elif ch=='3':
        print()
        print('*'*65)
        print("                       (: THANK YOU :)")
        print('*'*65)
    else:
        print()
        print("INVALID INPUT.")
        ch=input("Enter only 1/2/3 : ")
        MAIN(ch)

def M_CHOICE():          #-----MENU CHOICE-----#-
    ch=input("CUSTOMER [1] / MANAGEMENT [2] / EXIT [3] : ")
    MAIN(ch)

print()          #-----PROGRAM START-----#
print('='*65)
print("|                     FOOD BOOKING                              |")
print('='*65)
e=input("loading.......\ press enter to continue ")
if e=="":
    M_CHOICE()
else:
    M_CHOICE()

#------------------------------------END-------------------------------------#                          