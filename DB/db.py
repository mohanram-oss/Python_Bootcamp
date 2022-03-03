import pymongo
#creating database
myclient = pymongo.MongoClient("localhost:27017")
#creating db
mydb = myclient["mydatabase"]
#creating collection
mycol = mydb["customers"]
#creating dictionary
mydict = { "name :": "rajesh", "mobile :": "1234567890" }
#inserting data to collection
x = mycol.insert_one(mydict)
#deleting data
#asking conformation
delete = int(input("do you want to delete the data ? (yes=1 no=0) :"))
#condition
if delete == 1 :
    mycol.delete_one(mydict)
    print("data deleted successfully :(")
    undo = int(input("do you want to undo the deletion ? (yes=1 no=0) :"))
else :
    print("data not deleted :)")

if undo == 1:
    #asking for undo
    #creating dictionary
    mydict = { "name :": "rajesh", "mobile :": "1234567890" }
    #inserting data to collection
    x = mycol.insert_one(mydict)
else :
    print("not undoed")
