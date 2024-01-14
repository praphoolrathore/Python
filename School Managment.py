def create_attendence_table():
    try:
        import mysql.connector as sqltor
        mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
        mycursor=mydb.cursor()
        sql2='select count(*) from student'
        mycursor.execute(sql2)
        c=[]
        for x in mycursor:
            c.append(int(x[0]))
        b=c[0]
        sql='select sclass from student'
        mycursor.execute(sql)
        a=[]
        for x in mycursor:
            a.append(x[0])
        for i in range(b):
            rec3='show tables'
            mycursor.execute(rec3)
            l=[]
            for x in mycursor:
                l.append(x[0])
            database='attendence_class_'+a[i]+''
            if search(l,database):
                print("")
            else:
                rec1='create table attendence_class_'+a[i]+' (adno char(10),rollno char(10),sname char(30),attendence char(4),attendence_date char(25),stu_ID char(30))'
                mycursor.execute(rec1)
            mydb.commit()
        mycursor.close()
    except sqltor.Error as error:
        print("Failed to insert record into table {}".format(error))
    finally:
        if (mydb.is_connected()):
            mydb.close()
            print("   ")

def Show_Attendence():
    try:
        import mysql.connector as sqltor
        mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
        mycursor=mydb.cursor()
        s_class=input("Enter class : ")
        rec1=('select * from attendence_class_'+s_class+'')
        val=(s_class)
        mycursor.execute(rec1,val)
        for(adno,rollno,sname,attendence,attendence_date,stu_ID) in mycursor:
                print("----------------------------------------")
                print("Admission No.         : ",adno)
                print("Roll No.               : ",rollno)
                print("Student Name         : ",sname)
                print("Attendence            : ",attendence)
                print("Date of atendence    : ",attendence_date)
                print("Student ID            : ",stu_ID)
                print("----------------------------------------")
        mycursor.close()
    except sqltor.Error as error:
        print("Failed to show record from table {}".format(error))
    finally:
        if (mydb.is_connected()):
            mydb.close()
            print("   ")
            print("BYE BYE")

def Search_Attendence():
    print("To search attendence details -->")
    print("")
    try:
        import mysql.connector as sqltor
        mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
        mycursor=mydb.cursor()
        s_class=input("Enter class whose attendence details to be search : ")
        date=input("Enter date ( ex- 07dec2020 [ NO SPACE ALLOWED ] ) : ")
        rec=('select * from attendence_class_'+s_class+''+date+'')
        mycursor.execute(rec)
        for(adno,rollno,sname,attendence,attendence_date,stu_ID) in mycursor:
                print("----------------------------------------")
                print("Admission No.         : ",adno)
                print("Roll No.               : ",rollno)
                print("Student Name         : ",sname)
                print("Attendence            : ",attendence)
                print("Date of atendence     : ",attendence_date)
                print("Student ID            : ",stu_ID)
                print("----------------------------------------")
        mycursor.close()
    except sqltor.Error as error:
        print("Failed to show record from table {}".format(error))
    finally:
        if (mydb.is_connected()):
            mydb.close()
            print("   ")
         
def Atten_Records():
    print("")
    try:
        import mysql.connector as sqltor
        mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
        mycursor=mydb.cursor()
        s_class=input("Enter class whose attendence to be taken : ")
        date=input("Enter date (ex- 07dec2020 [NO SPACE ALLOWED]) : ")
        
        rec3='update attendence_class_'+s_class+' set attendence_date="'+date+'";'
        mycursor.execute(rec3)
        mydb.commit()
        rec='create table if not exists attendence_class_'+s_class+''+date+' select * from attendence_class_'+s_class+''
        mycursor.execute(rec)
        rec1='select count(*) from attendence_class_'+s_class+''
        mycursor.execute(rec1)
        a=[]
        for x in mycursor:
            a.append(x[0])
        for i in range(a[0]):
            rec1='select * from attendence_class_'+s_class+''+date+''
            d=[]
            c=[]
            mycursor.execute(rec1)
            for b in mycursor:
                c.append(b[1])
                d.append(b[2])
            print("------------------------------------")
            print("Roll no. : ",c[i])
            print("Name     : ",d[i])
            n=input("Enter Attendence(P/A) : ")
            print('')
            rec1='update attendence_class_'+s_class+''+date+' set attendence=%s where rollno=%s;'
            val1=(n,c[i])
            mycursor.execute(rec1,val1)
            mydb.commit()
    except sqltor.Error as error:
        print("Failed to insert record into table {}".format(error))
    finally:
        if (mydb.is_connected()):
            mydb.close()
            print("   ")
            print("ATTENDENCE COMPLETED")

    
def Add_Stu_Records():
    print("Enter your details -->")
    print("")
    try:
        import mysql.connector as sqltor
        mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
        mycursor=mydb.cursor()
    
        adno=input("Enter Admission No              : ")
        rollno=input("Enter Roll no.                    : ")
        s_name=input('Enter student name              : ')
        address=input('Enter Address                   : ')
        stream=input('Enter Stream                    : ')
        s_class=input("Enter class                      : ")
        fee_deposited=input("Fee deposited                    : ")
        stu_ID=input('Enter student ID to login       : ')
        stu_password=input('Enter student password to login : ')

        sql="insert into student(adno,rollno,sname,address,stream,sclass,stu_ID,stu_password) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(adno,rollno,s_name,address,stream,s_class,stu_ID,stu_password)
        mycursor.execute(sql,val)
        rec1="insert into fee(adno,sname,sclass,fee_deposited,stu_ID) values(%s,%s,%s,%s,%s)"
        val1=(adno,s_name,s_class,fee_deposited,stu_ID)
        mycursor.execute(rec1,val1)
        mydb.commit()
        rec3='show tables'
        mycursor.execute(rec3)
        l=[]
        for x in mycursor:
            l.append(x[0])
        database='attendence_class_'+s_class+''
        if search(l,database):
            print("")
        else:
            create_attendence_table()

        rec2='insert into attendence_class_'+s_class+'(adno,rollno,sname,attendence,attendence_date,stu_ID) values(%s,%s,%s,null,null,%s)'
        val2=(adno,rollno,s_name,stu_ID)
        mycursor.execute(rec2,val2)
        mydb.commit()
        print("Record successfully added")
        mycursor.close()
    except sqltor.Error as error:
        print("Failed to insert record into table {}".format(error))
    finally:
        if (mydb.is_connected()):
            mydb.close()
            print("   ")
            print("BYE BYE")

def Show_Stu_Details():
    print("To show student details -->")
    print("")
    try:
        import mysql.connector as sqltor
        mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
        mycursor=mydb.cursor()
        rec=('select * from student')
        mycursor.execute(rec)
        for(adno,rollno,s_name,address,stream,s_class,stu_ID,stu_password) in mycursor:
                print("----------------------------------------")
                print("Admission No.     : ",adno)
                print("Roll No.           : ",rollno)
                print("Student Name     : ",s_name)
                print("Address            : ",address)
                print("Stream             : ",stream)
                print("Class               : ",s_class)
                print('Student ID        : ',stu_ID)
                print('Student Password  : ',stu_password)
                print("----------------------------------------")
        mycursor.close()
    except sqltor.Error as error:
        print("Failed to show record from table {}".format(error))
    finally:
        if (mydb.is_connected()):
            mydb.close()
            print("   ")
            print("BYE BYE")

def Search_Stu_Details():
    print("To search student details -->")
    print("")
    try:
        import mysql.connector as sqltor
        mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
        mycursor=mydb.cursor()
        temp_adno=input("Enter Admission Number to be search : ")
        rec=('select * from student where adno="'+temp_adno+'";')
        mycursor.execute(rec)
    
        for(adno,rollno,s_name,address,stream,s_class,stu_ID,stu_password) in mycursor:
            print("----------------Show_Stu_Details()------------------------")
            print("Admission No.     : ",adno)
            print("Roll No.           : ",rollno)
            print("Student Name     : ",s_name)
            print("Address            : ",address)
            print("Stream             : ",stream)
            print("Class               : ",s_class)
            print('Student ID        : ',stu_ID)
            print('Student Password  : ',stu_password)
            print("----------------------------------------")
        mycursor.close()
    except sqltor.Error as error:
        print("Failed to search record from table {}".format(error))
    finally:
        if (mydb.is_connected()):
            mydb.close()
            print("   ")
            print("BYE BYE")

def Delete_Stu_Details():
    print("To delete student record -->")
    print("")
    try:
        import mysql.connector as sqltor
        mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
        mycursor=mydb.cursor()
        temp_adno=input("Enter Student Admission Number to be deleted : ")
        s_class=input("Enter class whose records to be deleted : ")
        rec=('delete from student where adno="'+temp_adno+'";')
        mycursor.execute(rec)
        rec2=('delete from fee where adno="'+temp_adno+'";')
        mycursor.execute(rec2)
        rec3=('delete from attendence_class_'+s_class+' where adno="'+temp_adno+'"')
        mycursor.execute(rec3)
        mydb.commit()
        print("  ")
        print("Record successfully deleted")
        mycursor.close()
    except sqltor.Error as error:
        print("Failed to delete record from table {}".format(error))
    finally:
        if (mydb.is_connected()):
            mydb.close()
            print("   ")
            print("BYE BYE")

def Edit_Stu_Details():
    print("To edit students details -->")
    print("")
    try:
        import mysql.connector as sqltor
        mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
        mycursor=mydb.cursor()

        temp_adno=input("Enter Student Admission Number whose details to be updated : ")
        rollno=input("Enter Student Roll Number whose details to be updated : ")
        print("----Input new data  ----")
        print("")
        s_name=input('Enter student name     : ')
        address=input('Enter Address          : ')
        stream=input('Enter Stream           : ')
        s_class=input("Enter class             : ")
        rec2="update student set sname=%s,address=%s,stream=%s,sclass=%s where adno=%s"
        val=(s_name,address,stream,s_class,temp_adno)
        mycursor.execute(rec2,val)
        rec3='update attendence_class_'+s_class+' set sname=%s,attendence=null,attendence_date=null where adno=%s'
        val1=(s_name,temp_adno)
        mycursor.execute(rec3,val1)
        rec4="update fee set sname=%s,sclass=%s where adno=%s"
        val2=(s_name,s_class,temp_adno)
        mycursor.execute(rec4,val2)
        mydb.commit()
        print("")
        print("Record updated")

        mycursor.close()
    except sqltor.Error as error:
        print("Failed to update record into table {}".format(error))
    finally:
        if (mydb.is_connected()):
            mydb.close()
            print("   ")
            print("BYE BYE")

def Fee_Deposit():
    print("To deposit fee you are welcome -->")
    print("")
    try:
        import mysql.connector as sqltor
        mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
        mycursor=mydb.cursor()

        adno=input("Enter admission no. whose fees to be deposit     : ")
        s_class=input("Enter student class whose fees to be deposit     : ")
        fee_deposited=input("Enter amount to deposit                          : ")
        j=[]
        print("")
        print("1. Add(in previous deposit fee)")
        print("2. Replace(by computing total itself)")
        print("")
        f=int(input("Do you want to add or replace fee : "))
        if f==1:
            sql='select fee_deposited from fee where adno="'+adno+'"'
            mycursor.execute(sql)
            for x in mycursor:
                j.append(int(x[0]))
                g=int(fee_deposited)+j[0]
                d=str(g)
                rec1=('update fee set fee_deposited="'+d+'" where adno="'+adno+'";')
                mycursor.execute(rec1)
        else:
            rec=('update fee set fee_deposited="'+fee_deposited+'" where adno="'+adno+'";')
            mycursor.execute(rec)
        mydb.commit()
        mycursor.close()
        print(" ")
        print("FEES DEPOSITED")
    except sqltor.Error as error:
        print("Failed to update fee into record {}".format(error))
    finally:
        if (mydb.is_connected()):
            mydb.close()
            print("")
            print("BYE BYE")
  
def Fee_Details():
    print("To show fee details -->")
    print("")
    try:
        import mysql.connector as sqltor
        mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
        mycursor=mydb.cursor()

        rec=('select * from fee')
        mycursor.execute(rec)
        for(adno,s_name,s_class,fee_deposited,stu_ID) in mycursor:
                print("----------------------------------------")
                print("Admission No.   : ",adno)
                print("Student Name   : ",s_name)
                print("Class             : ",s_class)
                print("Fee Deposited   : ",fee_deposited)
                print("Student ID      : ",stu_ID)
                print("----------------------------------------")
        mycursor.close()
    except sqltor.Error as error:
        print("Failed to show record from table {}".format(error))
    finally:
        if (mydb.is_connected()):
            mydb.close()
            print("")
            print("BYE BYE")

def Search_Fee_Details():
    print("To search fee details -->")
    print("")
    try:
        import mysql.connector as sqltor
        mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
        mycursor=mydb.cursor()
        temp_adno=input("Enter Admission Number whose fees to be search : ")
        rec=('select * from fee where adno="'+temp_adno+'";')
        mycursor.execute(rec)
    
        for(adno,s_name,s_class,fee_deposited,stu_ID) in mycursor:
                print("----------------------------------------")
                print("Admission No.   : ",adno)
                print("Student Name   : ",s_name)
                print("Class             : ",s_class)
                print("Fee Deposited   : ",fee_deposited)
                print("Student ID            : ",stu_ID)
                print("----------------------------------------")
        mycursor.close()
    except sqltor.Error as error:
        print("Failed to search record from table {}".format(error))
    finally:
        if (mydb.is_connected()):
            mydb.close()
            print("   ")
            print("BYE BYE")


def Add_Teach_Records():
    print("Enter your details -->")
    print("")
    try:
        import mysql.connector as sqltor
        mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
        mycursor=mydb.cursor()
    
        emp_ID=input("Enter employee ID (used in login also)     : ")
        DOJ=input("Enter Date of joining(xx/xx/xxxx)         : ") 
        name=input('Enter teachers name                        : ')
        designation=input("Enter teachers designation                  : ")
        tclass=input("Enter class to be taken by the teacher    : ")
        teacher_password=input('Enter teachers password to login          : ')
        sql="insert into teachers(emp_ID,DOJ,name,designation,class,teacher_password) values(%s,%s,%s,%s,%s,%s)"
        val=(emp_ID,DOJ,name,designation,tclass,teacher_password)
        mycursor.execute(sql,val)
        mydb.commit()
        print("")
        print("Record successfully added")
        mycursor.close()
    except sqltor.Error as error:
        print("Failed to insert record into table {}".format(error))
    finally:
        if (mydb.is_connected()):
            mydb.close()
            print("")
            print("BYE BYE")

def Show_Teach_Details():
    print("To show teachers details -->")
    print("")
    try:
        import mysql.connector as sqltor
        mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
        mycursor=mydb.cursor()
        rec=('select * from teachers')
        mycursor.execute(rec)
        for(emp_ID,DOJ,name,designation,tclass,teacher_password) in mycursor:
                print("---------------------------------------------")
                print("EMP I'D             : ",emp_ID)
                print("Teachers Name      : ",name)
                print("Designation          : ",designation)
                print("Class alloted         : ",tclass)
                print("Teacher's password  : ",teacher_password)
                print("---------------------------------------------")
        mycursor.close()
    except sqltor.Error as error:
        print("Failed to show record from table {}".format(error))
    finally:
        if (mydb.is_connected()):
            mydb.close()
            print("")
            print("BYE BYE")

def Search_Teach_Details():
    print("To search teachers details -->")
    print("")
    try:
        import mysql.connector as sqltor
        mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
        mycursor=mydb.cursor()
        temp_emp_ID=input("Enter teachers employee ID  to be search : ")
        rec=('select * from teachers where emp_ID="'+temp_emp_ID+'";')
        mycursor.execute(rec)
    
        for(emp_ID,DOJ,name,designation,tclass,teacher_password) in mycursor:
                print("---------------------------------------------")
                print("EMP I'D            : ",emp_ID)
                print("Teachers Name     : ",name)
                print("Designation         : ",designation)
                print("Class alloted        : ",tclass)
                print("Teacher's password  : ",teacher_password)
                print("---------------------------------------------")
        mycursor.close()
    except sqltor.Error as error:
        print("Failed to search record from table {}".format(error))
    finally:
        if (mydb.is_connected()):
            mydb.close()
            print("")
            print("BYE BYE")
            
def Student(ID,b):
    try:
        import mysql.connector as sqltor
        mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
        mycursor=mydb.cursor()
        rec='update teachers_entry set student_data="'+time.var+'" where emp_ID="'+ID+'" and s_no="'+b+'"'
        mycursor.execute(rec)
        mydb.commit()
    except sqltor.Error as error:
        print("Failed to search record from table {}".format(error))
    finally:
        if (mydb.is_connected()):
            mydb.close()
    while True:
            print(" ")
            print(" ")
            print("     **********  Student Data Menu  ********** ")
            print(" ")
            print("1: To Add Student Record")
            print("2: To Show Student Details")
            print("3: To Search Student Record")
            print("4: To Delete Student Record")
            print("5: To Edit Student Record")
            print("6: Exit ")
            print(" ")
            print(" ")

            choice=int(input("Enter your Choice (1-6) : "))
            print("")
            if choice==1:
                Add_Stu_Records()
            elif choice==2:
                Show_Stu_Details()
            elif choice==3:
                Search_Stu_Details()
            elif choice==4:
                Delete_Stu_Details()
            elif choice==5:
                Edit_Stu_Details()
            elif choice==6:
                print('')
                break
            else:
                print("ERROR-- Invalid Choice")
                conti=input("Press any key to return : ")
                continue


def Attendence(ID,b):
    try:
        import mysql.connector as sqltor
        mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
        mycursor=mydb.cursor()
        rec='update teachers_entry set attendence_data="'+time.var+'" where emp_ID="'+ID+'" and s_no="'+b+'"'
        mycursor.execute(rec)
        mydb.commit()
    except sqltor.Error as error:
        print("Failed to search record from table {}".format(error))
    finally:
        if (mydb.is_connected()):
            mydb.close()
    while True:
            print(" ")
            print(" ")
            print("     **********   Attendence Menu   ********** ")
            print(" ")
            print("1: To Take Attendence")
            print("2: To show Attendence")
            print("3: To search Attendence")
            print("4: Exit")
            print(" ")
            print(" ")

            choice=int(input("Enter your Choice (1-4) : "))
            print("")
            if choice==1:
                Atten_Records()
            elif choice==2:
                Show_Attendence()
            elif choice==3:
                Search_Attendence()
            elif choice==4:
                print('')
                break
            else:
                print("ERROR-- Invalid Choice")
                conti=input("Press any key to return : ")
                continue
            
def Teacher(ID,b):
    try:
        import mysql.connector as sqltor
        mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
        mycursor=mydb.cursor()
        rec='update teachers_entry set teachers_data="'+time.var+'" where emp_ID="'+ID+'" and s_no="'+b+'"'
        mycursor.execute(rec)
        mydb.commit()
    except sqltor.Error as error:
        print("Failed to search record from table {}".format(error))
    finally:
        if (mydb.is_connected()):
            mydb.close()
    while True:
                print(" ")
                print("")
                print("     **********  Teachers Data Menu  ********** ")
                print(" ")
                print("1: To Add Teachers Record")
                print("2: To Show Teachers Details")
                print("3: To Search Teachers Record")
                print("4: Exit ")
                print(" ")
                print(" ")

                choice=int(input("Enter your Choice (1-4) : "))
                print("")
                if choice==1:
                    Add_Teach_Records()
                elif choice==2:
                    Show_Teach_Details()
                elif choice==3:
                    Search_Teach_Details()
                elif choice==4:
                    print('')
                    break
                else:
                    print("ERROR-- Invalid Choice")
                    conti=input("Press any key to return : ")
                    continue
                    

def Fee(ID,b):
    try:
        import mysql.connector as sqltor
        mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
        mycursor=mydb.cursor()
        rec='update teachers_entry set fee_details="'+time.var+'" where emp_ID="'+ID+'" and s_no="'+b+'"'
        mycursor.execute(rec)
        mydb.commit()
    except sqltor.Error as error:
        print("Failed to search record from table {}".format(error))
    finally:
        if (mydb.is_connected()):
            mydb.close()
    while True:
            print(" ")
            print(" ")
            print("     **********  Students Fee Menu  ********** ")
            print(" ")
            print("1: To Deposit Fee")
            print("2: For Fee Details")
            print("3: To Search fee details")
            print("4: Exit")
            print(" ")
            print(" ")

            choice=int(input("Enter your Choice (1-4) : "))
            print("")
            if choice==1:
                Fee_Deposit()
            elif choice==2:
                Fee_Details()
            elif choice==3:
                Search_Fee_Details()
            elif choice==4:
                print('')
                break
            else:
                print("ERROR-- Invalid Choice")
                conti=input("Press any key return : ")
                continue
def ex_teach_record():
                import mysql.connector as sqltor
                mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
                mycursor=mydb.cursor()
                sql2=("insert into teachers values('123456','10/01/2021','xyz','pqr','12','abc')")
                mycursor.execute(sql2)
                mydb.commit()
                mydb.close()
                    
def ex_stu_record():
                import mysql.connector as sqltor
                mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
                mycursor=mydb.cursor()
                sql2=("insert into student values('00001','01','jkl','mno','pqr','12','123456','abc')")
                rec=("insert into fee values('00001','jkl','12','3200','123456')")
                mycursor.execute(sql2)
                mycursor.execute(rec)
                mydb.commit()
                mydb.close()
                    
def Log_Stu_Details(ID,b):
        try:
            import mysql.connector as sqltor
            mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
            mycursor=mydb.cursor()
            rec='update student_entry set student_details="'+time.var+'" where stu_ID="'+ID+'" and s_no ="'+b+'"'
            print('aaa')
            mycursor.execute(rec)
            print('abb')
            mydb.commit()
            print('acc')
            sql2='select adno,rollno,sname,address,stream,sclass from student where stu_ID="'+ID+'";'
            mycursor.execute(sql2)
            for(adno,rollno,s_name,address,stream,s_class,) in mycursor:
                print("----------------Show Student Details------------------------")
                print("Admission No.     : ",adno)
                print("Roll No.           : ",rollno)
                print("Student Name     : ",s_name)
                print("Address            : ",address)
                print("Stream             : ",stream)
                print("Class               : ",s_class)
                print("----------------------------------------")
            mycursor.close()
        except sqltor.Error as error:
            print("Failed to insert record into table {}".format(error))
        finally:
            if (mydb.is_connected()):
                mydb.close()
                print("   ")
                
def Log_Atten_Details(ID,b):
        try:
            import mysql.connector as sqltor
            mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
            mycursor=mydb.cursor()
            rec1='update student_entry set attendence_details="'+time.var+'" where stu_ID="'+ID+'" and s_no="'+b+'"'
            mycursor.execute(rec1)
            mydb.commit()
            s_class=input("Enter class whose attendence details to be displayed : ")
            date=input("Enter date ( ex- 07dec2020 [ NO SPACE ALLOWED ] ) : ")
            rec=('select sname,attendence,attendence_date from attendence_class_'+s_class+''+date+' where stu_ID="'+ID+'";')
            mycursor.execute(rec)
            for(sname,attendence,attendence_date) in mycursor:
                    print("----------------------------------------")
                    print("Student Name         : ",sname)
                    print("Attendence            : ",attendence)
                    print("Date of atendence     : ",attendence_date)
                    print("----------------------------------------")
            mycursor.close()
        except sqltor.Error as error:
            print('')
            print("NO RECORD FOUND........".format(error))
        finally:
            if (mydb.is_connected()):
                mydb.close()
                print("   ")

def Log_Fee_Details(ID,b):
        try:
            import mysql.connector as sqltor
            mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
            mycursor=mydb.cursor()
            rec1='update student_entry set fee_details="'+time.var+'" where stu_ID="'+ID+'" and s_no="'+b+'"'
            mycursor.execute(rec1)
            mydb.commit()
            rec=('select sname,sclass,fee_deposited from fee where stu_ID="'+ID+'";')
            mycursor.execute(rec)
            for(s_name,s_class,fee_deposited) in mycursor:
                    print("----------------------------------------")
                    print("Student Name   : ",s_name)
                    print("Class             : ",s_class)
                    print("Fee Deposited   : ",fee_deposited)
                    print("----------------------------------------")
            mycursor.close()
        except sqltor.Error as error:
            print("Failed to insert record into table {}".format(error))
        finally:
            if (mydb.is_connected()):
                mydb.close()
                print("   ")
def time():
        import datetime
        time.var=datetime.datetime.now().strftime("%Y-%m-%d,%H:%M") #format is important ("%Y-%m-%d,%H:%M")

def stu_leaving_time(ID,b):
    try:
        import mysql.connector as sqltor
        mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
        mycursor=mydb.cursor()
        rec='update student_entry set leaving_time="'+time.var+'" where stu_ID="'+ID+'" and s_no="'+b+'"'
        mycursor.execute(rec)
        mydb.commit()
    except sqltor.Error as error:
        print("Failed to search record from table {}".format(error))
    finally:
        if (mydb.is_connected()):
            mydb.close()
            
def teach_leaving_time(ID,b):
    try:
        import mysql.connector as sqltor
        mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
        mycursor=mydb.cursor()
        rec='update teachers_entry set leaving_time="'+time.var+'" where emp_ID="'+ID+'" and s_no="'+b+'"'
        mycursor.execute(rec)
        mydb.commit()
    except sqltor.Error as error:
        print("Failed to search record from table {}".format(error))
    finally:
        if (mydb.is_connected()):
            mydb.close()
           
def Teachers_Login(ID,passwd):
    try:
        import mysql.connector as sqltor
        mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
        mycursor=mydb.cursor()
        rec6="create table if not exists teachers_entry(s_no char(20),emp_ID char(20),entry_time char(20),leaving_time char(20),student_data char(20),attendence_data char(20),fee_details char(20),teachers_data char(20))"
        mycursor.execute(rec6)
        rec1="select count(*) from teachers_entry"
        mycursor.execute(rec1)
        for x in mycursor:
            a=x[0]
            b=str(a+1)
        rec=('insert into teachers_entry values("'+b+'","'+ID+'","'+time.var+'",null,null,null,null,null)')
        mycursor.execute(rec)
        mydb.commit()
    except sqltor.Error as error:
        print("Failed to search record from table {}".format(error))
    finally:
        if (mydb.is_connected()):
            mydb.close()
    while True:
            print("")
            print("     *************     K.V 2 - Terachers MAIN MENU      *************")
            print(" ")
            print("")
            print("1: Student data")
            print("2: Attendence")
            print("3: Fee Details")
            print("4: Teachers Data")
            print("5: Exit")
            print(" ")
    
            choice=int(input(" Enter the Choice (1-5): "))
            time()
            if choice==2:
                Attendence(ID,b)
            elif choice==1:
                Student(ID,b)
            elif choice==3:
                Fee(ID,b)
            elif choice==4:
                Teacher(ID,b)
            elif choice==5:
                teach_leaving_time(ID,b)
                break
            else :
                print("ERROR-- Invalid Choice")
                conti=input("Press any key to return : ")
                continue
    
def Students_Login(ID,passwd):
    try:
        import mysql.connector as sqltor
        mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
        mycursor=mydb.cursor()
        rec7="create table if not exists student_entry(s_no char(20),stu_ID char(20),entry_time char(20),leaving_time char(20),student_details char(20),attendence_details char(20),fee_details char(20))"
        mycursor.execute(rec7)
        rec1="select count(*) from student_entry"
        mycursor.execute(rec1)
        for x in mycursor:
            a=x[0]
            b=str(a+1)
        rec='insert into student_entry values("'+b+'","'+ID+'","'+time.var+'",null,null,null,null)'
        mycursor.execute(rec)
        mydb.commit()
    except sqltor.Error as error:
        print("Failed to search record from table {}".format(error))
    finally:
        if (mydb.is_connected()):
            mydb.close()
    while True:
            print(" ")
            print("")
            print("     **********   Student Menu  ********** ")
            print(" ")
            print("1: Students details ")
            print("2: Attendence details ")
            print("3: Fee details")
            print("4: Exit ")
            print(" ")
            choice=int(input("Enter your Choice (1-4) : "))
            time()
            if choice==1:
                print('a')
                Log_Stu_Details(ID,b)
            elif choice==2:
                Log_Atten_Details(ID,b)
            elif choice==3:
                Log_Fee_Details(ID,b)
            elif choice==4:
                stu_leaving_time(ID,b)
                break
            else:
                print("ERROR-- Invalid Choice")
                conti=input("Press any key to return : ")
                continue
def show_teach_entry():
            try:
                import mysql.connector as sqltor
                mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
                mycursor=mydb.cursor()
                rec=('select emp_ID,entry_time,leaving_time,student_data,attendence_data,fee_details,teachers_data from teachers_entry')
                mycursor.execute(rec)
                for (emp_ID,entry_time,leaving_time,student_data,attendence_data,fee_details,teachers_data) in mycursor:
                    print("----------------------------------------------------")
                    print('Teachers ID                     : ',emp_ID)
                    print('Entry time of teacher           : ',entry_time)
                    print('Leaving time of teacher         : ',leaving_time)
                    print('Enter in student data files      : ',student_data)
                    print('Enter in attendence data files   : ',attendence_data)
                    print('Enter in fee data files           : ',fee_details)
                    print('Enter in teachers data files      : ',teachers_data)
                    print("----------------------------------------------------")
                    print('')
            except sqltor.Error as error:
                print("Failed to insert record into table {}".format(error))
                print('DATA NOT FOUND....')
            finally:
                if (mydb.is_connected()):
                    mydb.close()
def show_stu_entry():
            try:
                import mysql.connector as sqltor
                mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
                mycursor=mydb.cursor()
                rec=('select stu_ID,entry_time,leaving_time,student_details,attendence_details,fee_details from student_entry')
                mycursor.execute(rec)
                for (stu_ID,entry_time,leaving_time,student_details,attendence_details,fee_details) in mycursor :
                    print("----------------------------------------------------")
                    print('Students ID                     : ',stu_ID)
                    print('Entry time of student           : ',entry_time)
                    print('Leaving time of student         : ',leaving_time)
                    print('Enter in student data files      : ',student_details)
                    print('Enter in attendence data files   : ',attendence_details)
                    print('Enter in fee data files           : ',fee_details)
                    print("----------------------------------------------------")
                    print('')
            except sqltor.Error as error:
                print("Failed to insert record into table {}".format(error))
                print('DATA NOT FOUND....')
            finally:
                if (mydb.is_connected()):
                    mydb.close()

def search_teach_entry_ID():
            try:
                import mysql.connector as sqltor
                mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
                mycursor=mydb.cursor()
                ID=input('Enter teachers ID whose all entry to be diplay : ')
                rec='select emp_ID,entry_time,leaving_time,student_data,attendence_data,fee_details,teachers_data from teachers_entry where emp_ID="'+ID+'"'
                mycursor.execute(rec)
                for (emp_ID,entry_time,leaving_time,student_data,attendence_data,fee_details,teachers_data) in mycursor:
                    print("----------------------------------------------------")
                    print('Teachers ID                     : ',emp_ID)
                    print('Entry time of teacher           : ',entry_time)
                    print('Leaving time of teacher         : ',leaving_time)
                    print('Enter in student data files      : ',student_data)
                    print('Enter in attendence data files   : ',attendence_data)
                    print('Enter in fee data files           : ',fee_details)
                    print('Enter in teachers data files      : ',teachers_data)
                    print("----------------------------------------------------")
                    print('')
            except sqltor.Error as error:
                print("Failed to insert record into table {}".format(error))
                print('DATA NOT FOUND....')
            finally:
                if (mydb.is_connected()):
                    mydb.close()

def search_stu_entry_ID():
            try:
                import mysql.connector as sqltor
                mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
                mycursor=mydb.cursor()
                ID=input('Enter student ID whose all entry to be diplay : ')
                rec='select stu_ID,entry_time,leaving_time,student_details,attendence_details,fee_details from student_entry where stu_ID="'+ID+'"'
                mycursor.execute(rec)
                for (stu_ID,entry_time,leaving_time,student_details,attendence_details,fee_details) in mycursor :
                    print("----------------------------------------------------")
                    print('Students ID                     : ',stu_ID)
                    print('Entry time of student           : ',entry_time)
                    print('Leaving time of student         : ',leaving_time)
                    print('Enter in student data files      : ',student_details)
                    print('Enter in attendence data files   : ',attendence_details)
                    print('Enter in fee data files           : ',fee_details)
                    print("----------------------------------------------------")
                    print('')
            except sqltor.Error as error:
                print("Failed to insert record into table {}".format(error))
                print('DATA NOT FOUND....')
            finally:
                if (mydb.is_connected()):
                    mydb.close()

def search_teach_entry_data():
    while True:
            try:
                import mysql.connector as sqltor
                mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
                mycursor=mydb.cursor()
                print('      ******* Search Menu *******')
                print('')
                print('1: Student data file')
                print('2: Attendence data file')
                print('3: Fee data file')
                print('4: Teachers data file')
                print('5: Exit')
                print('')
                data=int(input('Enter file no. in which all teachers entry to be diplay : '))
                if data==1:
                    rec='select emp_ID,student_data from teachers_entry'
                    mycursor.execute(rec)
                    for (emp_ID,student_data) in mycursor:
                        print("----------------------------------------------------")
                        print('Teachers ID                     : ',emp_ID)
                        print('Enter in student data files      : ',student_data)
                        print("----------------------------------------------------")
                        print('')
                elif data==2:
                    print('')
                    rec='select emp_ID,attendence_data from teachers_entry'
                    mycursor.execute(rec)
                    for (emp_ID,attendence_data) in mycursor:
                        print("----------------------------------------------------")
                        print('Teachers ID                     : ',emp_ID)
                        print('Enter in attendence data files   : ',attendence_data)
                        print("----------------------------------------------------")
                        print('')
                elif data==3:
                    print('')
                    rec='select emp_ID,fee_details from teachers_entry'
                    mycursor.execute(rec)
                    for (emp_ID,fee_details) in mycursor:
                        print("----------------------------------------------------")
                        print('Teachers ID                     : ',emp_ID)
                        print('Enter in fee data files          : ',fee_details)
                        print("----------------------------------------------------")
                        print('')
                elif data==4:
                    print('')
                    rec='select emp_ID,teachers_data from teachers_entry'
                    mycursor.execute(rec)
                    for (emp_ID,teachers_data) in mycursor:
                        print("----------------------------------------------------")
                        print('Teachers ID                     : ',emp_ID)
                        print('Enter in student data files      : ',teachers_data)
                        print("----------------------------------------------------")
                        print('')
                elif data==5:
                    break
                else:
                    print('INVALID CHOICE......')
                    print('')
                    continue
            except sqltor.Error as error:
                print("Failed to insert record into table {}".format(error))
                print('DATA NOT FOUND....')
            finally:
                if (mydb.is_connected()):
                    mydb.close()

def search_stu_entry_data():
    while True:
            try:
                import mysql.connector as sqltor
                mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
                mycursor=mydb.cursor()
                print('      ******* Search Menu *******')
                print('')
                print('1: Student data file')
                print('2: Attendence data file')
                print('3: Fee data file')
                print('4: Exit')
                print('')
                data=int(input('Enter file no. in which all student entry to be diplay : '))
                if data==1:
                    rec='select stu_ID,student_details from student_entry'
                    mycursor.execute(rec)
                    for (emp_ID,student_data) in mycursor:
                        print("---------------------------------------------------")
                        print('Student ID                     : ',emp_ID)
                        print('Enter in student data files      : ',student_data)
                        print("----------------------------------------------------")
                        print('')
                elif data==2:
                    print('')
                    rec='select stu_ID,attendence_details from student_entry'
                    mycursor.execute(rec)
                    for (emp_ID,attendence_data) in mycursor:
                        print("----------------------------------------------------")
                        print('Student ID                     : ',emp_ID)
                        print('Enter in attendence data files   : ',attendence_data)
                        print("----------------------------------------------------")
                        print('')
                elif data==3:
                    print('')
                    rec='select stu_ID,fee_details from student_entry'
                    mycursor.execute(rec)
                    for (emp_ID,fee_details) in mycursor:
                        print("----------------------------------------------------")
                        print('Student ID                     : ',emp_ID)
                        print('Enter in fee data files          : ',fee_details)
                        print("----------------------------------------------------")
                        print('')
                elif data==4:
                    break
                else:
                    print('INVALID CHOICE......')
                    continue
            except sqltor.Error as error:
                print("Failed to insert record into table {}".format(error))
                print('DATA NOT FOUND....')
            finally:
                if (mydb.is_connected()):
                    mydb.close()
                    
def teach_entry():
    while True:
            print(" ")
            print("")
            print("     **********   Teachers Entry  ********** ")
            print(" ")
            print("1: Show Teachers Entry Details ")
            print("2: Search teachers entry using  teacher ID")
            print("3: Search teachers entry using file name")
            print("4: Exit ")
            print(" ")
            choice=int(input("Enter your Choice (1-4) : "))
            print("")
            if choice==1:
                show_teach_entry()
            elif choice==2:
                search_teach_entry_ID()
            elif choice==3:
                search_teach_entry_data()
            elif choice==4:
                print('')
                break
            else:
                print("ERROR-- Invalid Choice")
                conti=input("Press any key to return : ")
                continue
def stu_entry():
    while True:
            print(" ")
            print("")
            print("     **********   Student Entry  ********** ")
            print(" ")
            print("1: Show Student Entry Details ")
            print("2: Search Student entry using  Student ID")
            print("3: Search Student entry using file name")
            print("4: Exit ")
            print(" ")
            choice=int(input("Enter your Choice (1-4) : "))
            print("")
            if choice==1:
                show_stu_entry()
            elif choice==2:
                search_stu_entry_ID()
            elif choice==3:
                search_stu_entry_data()
            elif choice==4:
                print('')
                break
            else:
                print("ERROR-- Invalid Choice")
                conti=input("Press any key to return : ")
                continue
            
def Principal_login():
    while True:
            print(" ")
            print("")
            print("     **********   Principal Menu  ********** ")
            print(" ")
            print("1: Teachers Entry Details ")
            print("2: Student Entry Details ")
            print("3: Exit ")
            print(" ")
            choice=int(input("Enter your Choice (1-3) : "))
            print("")
            if choice==1:
                teach_entry()
            elif choice==2:
                stu_entry()
            elif choice==3:
                print('')
                break
            else:
                print("ERROR-- Invalid Choice")
                conti=input("Press any key to return : ")
                continue
            
def Teachers_check_login():
    try:
        import mysql.connector as sqltor
        mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
        mycursor=mydb.cursor()
        sql2='select emp_ID,teacher_password from teachers'
        mycursor.execute(sql2)
        c=[]
        d=[]
        for (x,y) in mycursor:
            c.append(x)
            d.append(y)
        n=len(c)
        if n!=0:
            ID=input('Enter teachers login ID : ')
            passwd=input('Enter teachers password : ')
            for i in range(n):
                if ID==c[i] and passwd==d[i]:
                    time()
                    Teachers_Login(ID,passwd)
                elif ID or passwd not in c:
                    print('INVALID... ID or PASSWORD')
                else:
                    continue
        else:
            print('NO record in Teachers table')
            print('INSERTING EXAMPLE RECORD.........')
            ex_teach_record()

    except sqltor.Error as error:
        print("Failed to insert record into table {}".format(error))
    finally:
        if (mydb.is_connected()):
            mydb.close()
            print("   ")

def Students_check_login():
        print('')
        try:
            import mysql.connector as sqltor
            mydb=sqltor.connect(user='root',password='praful',host='localhost',database='incridible')
            mycursor=mydb.cursor()
            sql2='select stu_ID,stu_password from student'
            mycursor.execute(sql2)
            c=[]
            d=[]
            for (x,y) in mycursor:
                c.append(x)
                d.append(y)
            n=len(c)
            if n!=0:
                ID=input('Enter student login ID : ')
                passwd=input('Enter student password : ')
                for i in range(n):
                    if ID==c[i] and passwd==d[i]:
                        time()
                        Students_Login(ID,passwd)
                    elif ID or passwd not in c:
                        print('INVALID... ID or PASSWORD')
                    else:
                        continue
            else:
                print('NO record in Sudents table')
                print('INSERTING EXAMPLE RECORD.........')
                ex_stu_record()

        except sqltor.Error as error:
            print("Failed to insert record into table {}".format(error))
        finally:
            if (mydb.is_connected()):
                mydb.close()
                print("   ")

def Principal_check_login():
                ID=input('Enter principal login ID : ')
                passwd=input('Enter principal password : ')
                if ID=='kv2' and passwd=='kv2':
                    Principal_login()
                else:
                    print('----INVALID... ID or PASSWORD----')

def search(list,database):
    for i in range(len(list)):
          if list[i]== database:
                return True
    return False

def main_menu():
    while True:
        print('')
        print('K.V 2- MAIN MENU')
        print('')
        print('1: Teachers login')
        print('2: Students login')
        print('3: Principal login')
        print('4: Exit')
        print('')
        choice=int(input(' Enter the Choice (1-4): '))
        if choice==1:
            Teachers_check_login()
        elif choice==2:
            Students_check_login()
        elif choice==3:
            Principal_check_login()
        elif choice==4:
            break
        else :
            print("ERROR-- Invalid Choice")
            break
        
def create_main_menu():
    import mysql.connector as sqltor
    mydb=sqltor.connect(user='root',password='praful',host='localhost')
    mycursor=mydb.cursor()
    rec1="create database incridible"
    rec2="use incridible"
    rec3="create table student (adno char(10) primary key,rollno char(10),sname char(30),address char(50),stream char(30),sclass char (5),stu_ID char(30),stu_password char(30));"
    rec4="create table teachers (emp_ID char(20) primary key,DOJ char(10),name char(30),designation char(15),class char (9),teacher_password char(30));"
    rec5="create table fee (adno char (10) primary key,sname char(30),sclass char(5),fee_deposited char(10),stu_ID char(30));"
    mycursor.execute(rec1)
    mycursor.execute(rec2)
    mycursor.execute(rec3)
    mycursor.execute(rec4)
    mycursor.execute(rec5)
    main_menu()

import mysql.connector as sqltor
mydb=sqltor.connect(user='root',password='praful',host='localhost')
mycursor=mydb.cursor()
rec1="show databases"
mycursor.execute(rec1)
a=[]
for x in mycursor:
      a.append(x[0])
database='incridible'
if search(a,database):
    main_menu()
else:
    create_main_menu()

while True:
    n=input("Do you want to use more (YES/NO)?? : ")
    if n in ('Y','y','yes','Yes','YES'):
        main_menu()
    elif n in('N','n','no','No','NO'):
        print("OK THANKS")
        print("")
        break
print("")
print("")
print("-> 1. Permanently (data will be saved in your system )")
print("-> 2. Temporary (data will erase from your system after exiting the progam )")
print("")
save=int(input("Do you want to save data permanently or temporary(1/2) : "))
if save==1:
    print("DATA SAVED")
    print("")
else:
    mycursor.execute('drop database incridible')
    print("DATA ERASED")
    print("")
print("********    YOU ARE EXIT NOW    *********")
