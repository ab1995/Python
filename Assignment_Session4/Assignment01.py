import pymysql

db=pymysql.connect("localhost", "root", "root", "BankDB")
cursor=db.cursor()

cursor.execute("DROP TABLE IF EXISTS BANK_ACCOUNT")

sql = """CREATE TABLE BANK_ACCOUNT (
    ACCOUNT_NO INT NOT NULL,
    ACCOUNT_NAME  CHAR(20),
    ACCOUNT_BALANCE FLOAT,
    IS_SALARY_ACCOUNT CHAR(1),
    OD_LIMIT  FLOAT)"""

cursor.execute(sql)

while True:
    choice=int(input("\n 1) Saving Account\n 2) Current Account\n 3) Exit\n\n Enter your choice: "))
    if choice==3:
        break

    elif choice==1:
        sql="""INSERT INTO BANK_ACCOUNT(ACCOUNT_NO, ACCOUNT_NAME, ACCOUNT_BALANCE, IS_SALARY_ACCOUNT)
        VALUES (%s, %s, %s, %s)"""
        cursor.execute(sql, (1, 'Ajay', 10000.00, 'Y'))
        db.commit()

    elif choice==2:
        sql = """INSERT INTO BANK_ACCOUNT (ACCOUNT_NO, ACCOUNT_NAME, ACCOUNT_BALANCE, OD_LIMIT)
        VALUES (%s, %s, %s, %s)"""

        cursor.execute(sql, (2, 'Sanjay', 80000.00, 100.00))
        db.commit()

db.close()