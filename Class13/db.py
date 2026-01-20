import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mano",
    database = "demo"
)
cur = con.cursor()

while True:
    print("\n 1.Insert 2.View 3.Update 4.Delete 5.Exit")
    ch = int(input("Enter Choice: "))

    # CREATE
    if ch == 1:
        name = input("Name: ")
        age = int(input("Age: "))
        dept = input("Dept: ")
        cur.execute(
            "INSERT INTO student(name, age, dept) values(%s, %s, %s)", (name, age, dept)
        )
        con.commit()
        print("Data Inserted")

    # READ
    elif ch == 2:
        cur.execute("SELECT * FROM student")
        for row in cur.fetchall():
            print(row)

    #UPDATE
    elif ch == 3:
        sid = int(input("ID: "))
        age = int(input("New Age: "))
        cur.execute(
            "Update student SET age=%s WHERE id=%s", (age, sid)
        )
        con.commit()
        print("Data Updated")

    #DELETE
    elif ch == 4:
        sid = int(input("ID: "))
        cur.execute("DELETE from student where id=%s", (sid,))
        con.commit()
        print("Data Deleted")

    #EXIT
    elif ch == 5:
        break

con.close()


"""
create database demo

create table demo.student(
	id int auto_increstudentment primary key,
    name varchar(50),
    age int,
    dept varchar(20)
)

"""