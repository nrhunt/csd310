from pymongo import MongoClient
import certifi
url="mongodb+srv://admin:admin@cluster0.3f0yk.mongodb.net/?retryWrites=true&w=majority"
client=MongoClient(url,tlsCAFile=certifi.where())
db=client.pytech
students = db.students
student_list = students.find({})
print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in student_list:
    print("\n Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n" )

result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Hunt II"}})
nathan = students.find_one({"student_id": "1007"})
print("\n -- DISPLAYING STUDENT DOCUMENT 1007 --")
print(" Student ID: " + nathan["student_id"] + "\n First Name: " + nathan["first_name"] + "\n Last Name: " + nathan["last_name"] + "\n")
input("\n\n End of program, press any key to continue...") 