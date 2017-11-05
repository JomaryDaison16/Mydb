import MySQLdb

def database():
    db = MySQLdb.connect(host="localhost", user="root", passwd= "", db = "dbdemo")
    cursor = db.cursor()
    Db = db
    cursor.execute("CREATE DATABASE IF NOT EXISTS {} ".format(Db))
    cursor.execute("USE {}".format(Db))
    cursor.execute("""CREATE TABLE IF NOT EXISTS tables
        (
        idnum char primary key,
        course char(20),
        Fname char(20),
        Mname char(20),
        Lname char(20)
        )
            """)
    cursor.close()
    db.close()
class Student:    

    def __init__(self,idnum,course,Fname,Mname,Lname):
        self.idnum = idnum
        self.course = course        
        self.Fname = Fname
        self.Mname = Mname
        self.Lname = Lname

    def add(self):              
        db = MySQLdb.connect(host="localhost", user="root", passwd= "", db = "dbdemo")
        cursor = db.cursor()

        sql = ("""INSERT INTO tables(idnum,course,Fname,Mname,Lname)          
                VALUES('%s','%s','%s','%s','%s')""" %\
                (self.idnum,self.course,self.Fname,self.Mname,self.Lname))
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()

def delete(idnum):
    db = MySQLdb.connect(host="localhost", user="root", passwd= "", db = "dbdemo")
    cursor = db.cursor()

    cursor.execute("DELETE FROM tables WHERE idnum = %s",(idnum))

    db.commit()
    cursor.close()
    db.close()
def search(idnum):
    db = MySQLdb.connect(host="localhost", user="root", passwd= "", db = "dbdemo")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tables WHERE idnum = %s",(idnum))
    result = cursor.fetchall()
    return result

def update(choice,idnum):
    db = MySQLdb.connect(host="localhost", user="root", passwd= "", db = "dbdemo")
    cursor = db.cursor()
    if choice == "1":
        newidnum = raw_input("Enter the new idnumber: ")
        cursor.execute("""UPDATE tables SET idnum = %s WHERE idnum = %s""",(newidnum,idnum))
        db.commit()
    elif choice == "2":
        newcourse = raw_input("Enter the new course: ")
        cursor.execute("UPDATE tables SET course = %s WHERE idnum = %s""",(newcourse,idnum))
        db.commit()
        cursor.close()
        db.close()
    elif choice == "3":
        newFirstName = raw_input("Enter the new firstname: ")
        cursor.execute("UPDATE tables SET Fname = %s WHERE idnum = %s""",(newFirstName,idnum))
        db.commit()
        cursor.close()
        db.close()
    elif choice == "4":
        newMiddleName = raw_input("Enter the new middlename: ")
        cursor.execute("UPDATE tables SET Mname = %s WHERE idnum = %s""",(newMiddleName,idnum))
        db.commit()
        cursor.close()
        db.close()
    elif choice == "5":
        newLastName = raw_input("Enter the new lastname: ")
        cursor.execute("UPDATE tables SET Lname = %s WHERE idnum = %s""",(newLastName,idnum))
        db.commit()
        cursor.close()
        db.close()
    else:
        print("not in the choices\n")

def prints():
    db = MySQLdb.connect(host="localhost", user="root", passwd= "", db = "dbdemo")
    cursor = db.cursor()

    cursor.execute('SELECT * FROM tables ORDER BY idnum ASC')
    for row in cursor.fetchall():
        print row

    cursor.close()
    db.close()

def menu():   
    print('What do you want to do?\n 1.Add\n 2.Delete\n 3.Search\n 4.Update\n 5.List of Students\n')

while(True):
    menu()   
    choice1 = input("Enter your chosen number: \n")
        
    if choice1 == 1:
        idnum = raw_input("Enter idNumber: ")
        course = raw_input("Enter course: ")
        Fname = raw_input("Enter first name: ")
        Mname = raw_input("Enter middle name: ")
        Lname = raw_input("Enter last name: ")
        StudInfo = Student(idnum,course,Fname,Mname,Lname)
        StudInfo.add()

    elif choice1 == 2:
        Search = raw_input ("Enter the idnumber of the data to be deleted: \n")
        delete(Search)

    elif choice1 == 3:
        Search = raw_input ("Enter the idnumber: \n")
        print search(Search)
        
    elif choice1 == 4:
        choice = raw_input ("What do you want to update?: \n 1. Idnumber \n 2. Course \n 3. First name \n 4. Middle name \n 5. Last name \n ----> ")
        idnum = raw_input ("Idnumber of the student you want to update: \n")
        update(choice,idnum)

    elif choice1 == 5:
        prints()

    else:
        print("not in the choices\n")

    choice2 = raw_input("Want to try again? yes or no: \n")
    if (choice2 == "no"):
            break
    else :
        print("not in the choices\n")