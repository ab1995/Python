import threading
import pymysql
import time

db=pymysql.connect("localhost", "root", "root", "BankDB")
cursor=db.cursor()
exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, operation):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.operation=operation

    def run(self):
        if self.operation=='check_balance':
            self.getBalance()
        elif self.operation=='update_balance':
            self.updateBalance()

    def getBalance(self):
        threadLock.acquire()
        sql = "SELECT * FROM BANK_ACCOUNT WHERE ACCOUNT_NO=1;"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(self.name, results)
        time.sleep(7)
        threadLock.release()

    def updateBalance(self):
        threadLock.acquire()
        sql="""UPDATE BANK_ACCOUNT SET ACCOUNT_BALANCE=90000 WHERE ACCOUNT_NO=1"""
        cursor.execute(sql)
        db.commit()
        threadLock.release()


threadLock = threading.Lock()
thread1 = myThread(1, "Thread-1", "check_balance")
thread2 = myThread(2, "Thread-2", "update_balance")

thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("Exiting Main Thread")