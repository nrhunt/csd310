from pymongo import MongoClient
import certifi
url="mongodb+srv://admin:admin@cluster0.3f0yk.mongodb.net/?retryWrites=true&w=majority"
client=MongoClient(url,tlsCAFile=certifi.where())
db=client.pytech
print("--pytech Collection List--\n",
db.list_collection_names())
nathan = { 
    "student_id": "1007",
    "first_name": "Nathan",
    "last_name": "Hunt",
    "enrollments": [
        {
        "term": "Session 3",
        "gpa": "3.5",
        "start_date": "July 10, 2021",
        "end_date": "September  10, 2021",
        "courses": [
            {
                "course_id": "CSD310",
                "description": "Database Security",
                "instructor": "Henry Le",
                "grade": "A"

            },
            {
                "course_id": "CSD320",
                "description": "Forensic investigation",
                "instructor": "Henry Le",
                "grade": "A"
            }
         ]
        }
    ]
}

joel = {
    "student_id": "1008",
    "first_name": "Joel",
    "last_name": "Web",
    "enrollments": [ 
        {
            "term": "Session 3",
            "gpa": "3.2",
            "start_date": "July 10, 2021",
            "end_date": "September 10, 2021",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Security",
                    "instructor": "Henry Le",
                    "grade": "A-"
                },
                {
                    "course_id": "CSD320",
                    "description": "Forensic Investigation",
                    "instructor": "Henry Le",
                    "grade": "A+"

                }
            
            ]
        }
    ]
}

jason = {
    "student_id": "1009",
    "first_name": "jason",
    "last_name": "web",
    "enrollments": [
        {
            "term": "session 3",
            "gpa": "4.0",
            "start_date": "July 10, 2021",
            "end_date": "September 10, 2021",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Security",
                    "instructor": "Henry Le",
                    "grade": "A"
                },
                {
                    "course_id": "CSD320",
                    "description": "Forensic Investigation",
                    "instructor": "Henry Le",
                    "grade": "A"
                }
            ]
        }
    ]
}

students = db.students
print("\n -- INSERT STATEMENTS --")
nathan_student_id = students.insert_one(nathan).inserted_id
print(" Inserted student record Nathan Hunt into the students collection with document_id" + str(nathan_student_id))

joel_student_id = students.insert_one(joel).inserted_id
print(" Inserted student record Joel Web into the students collection with document_id" + str(joel_student_id))

jason_student_id = students.insert_one(jason).inserted_id
print(" Inserted student record Jason Web into the students collection with document_id" + str(jason_student_id))

input("\n\n End of program, press any key to exit")