import sqlite3

connection=sqlite3.connect("employee.db")

# create a cursor object to insert record,create table
cursor=connection.cursor()

#create the table
table_info="""
Create table EMPLOYEE(EMP_NAME VARCHAR(25),EMP_ID VARCHAR(25),DESIGNATION VARCHAR(25),EMP_AGE INT);
"""
try:
    cursor.execute(table_info)
except:
    pass

#insert few records
cursor.execute('''Insert Into EMPLOYEE values('Satish','XY012','NLP Engineer',28)''')
cursor.execute('''Insert Into EMPLOYEE values('Aditya','XY014','Data Engineer',35)''')
cursor.execute('''Insert Into EMPLOYEE values('Akshay','XY013','Data Scientist',32)''')
cursor.execute('''Insert Into EMPLOYEE values('Amit','XY011','Cloud Engineer',38)''')
cursor.execute('''Insert Into EMPLOYEE values('Arun','XY016','Data Engineer',45)''')

#display all the records
print("The inserted records are: ")
data=cursor.execute('''Select * from EMPLOYEE''')
for row in data:
    print(row)

#Commit your changes in the database
connection.commit()
connection.close()