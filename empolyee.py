from unittest import result
import pymongo
#CRUD OPERATIONS
connection=pymongo.MongoClient("mongodb://localhost:27017")
mydb=connection["empdb"]
myemployee=mydb["employees"]

while True:
    print("****MENU****")
    print("1. Add  employee \n")
    print("2. Display database \n")
    print("3. Search an employee\n")
    print("4. Delete an employee\n")
    print("5. Update employee\n")
    print("6. Employe name start with:\n")
    print("7. Exit\n")
    op=int(input("Select an option:"))
    if op==1:
        print("*******Add employee*********")
        empCode=input("Enter the employee code:")
        empName=input("Enter the employee name:")
        empDesg=input("Enter the Desingnation:")
        data={"EmployeeCode":empCode,"Employeename":empName,"EmployeeDesignation":empDesg}
        print(data)
        myemployee.insert_one(data) #inserting data 
    elif op==2:
        print("********Display Database**********")
        res=myemployee.find().sort("Employeename",-1) #sorting in descending
        for i in res: #Displaying database
            print(i)
    elif op==3:
        print("*******Search******")
        empcode=input("Enter the Employeecode to search an employee:")
        data={"EmployeeCode":empcode}
        result=myemployee.find(data,{"_id":0})   #Here object id is hidden because we  use _id:0
        for i in result:
            print (i)
        
    elif op==4:
        print("*******Delete******")
        empcode=input("Enter the Employeecode to delete  an employee:")
        data={"EmployeeCode":empcode}
        myemployee.delete_one(data)
        print("Deletion of employee compleated")
    elif op==5:
        print("******Update******")
        empCode=input("Enter tthe employee code to be updated")
        empName=input("Enter the updated name:")
        empDesg=input("Enter the designation:")
        setdata={"EmployeeCode":empCode}
        newdata={"$set":{"Employeename":empName,"EmployeeDesignation":empDesg}}
        myemployee.update_one(setdata,newdata)
        print("Data updated successfully")
    elif op==6:
        print("******Employee name starts with ******")
        inp=input("Enter the letter you want to display:")
        condition={"Employeename":{"$gt":inp}}
        result=myemployee.find(condition)
        for i in result: 
            print(i)
    else:
        break

