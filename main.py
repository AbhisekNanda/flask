from flask import Flask,redirect,url_for,render_template,request

import database


from datetime import time

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return "hi"

@app.route('/login',methods=['GET','POST'])
def login(email :str, password:str):
    import jwt
    import datetime
    data=database.login(email,password)
    import json
    final_data=json.loads(data)
    my_secret = 'bro bro'
    token = jwt.encode(
    payload=final_data,
    key=my_secret,
    algorithm="HS256")
    token_data=json.dumps({"accsess token":token,"Data":final_data})
    final=json.loads(token_data)
    return final

# @app.post('/signup')
# def signup(First_name,Second_name,Email,Phone,Password,DOB):
#     status = database.signup(First_name,Second_name,Email,Phone,Password,DOB)
#     return {"status":status}

# @app.post('/sendotp')
# def send_otp(email):
#     status = database.create_otp(email)
#     return {"status":status}

# @app.post('/verifyotp')
# def send_otp(email):
#     status = database.verify_otp(email)
#     return {"status":status}

# @app.get('/Course')
# def course():
#     data = database.course()
#     import json
#     final_data=json.loads(data)
#     return final_data

# @app.get('/Mentor')
# def course():
#     data = database.mentor()
#     import json
#     final_data=json.loads(data)
#     return final_data

# @app.get('/{id}/Course')
# def id_course(id):
#     data= user.user_course(id)
#     import json
#     final_data=json.loads(data)
#     return final_data

# @app.get('/{id}/Mentor')
# def id_mentor(id):
#     data= user.user_mentor(id)
#     import json
#     final_data=json.loads(data)
#     return final_data

# @app.post('/EnrollMentor')
# def EnrollMentor(userid,joinid):
#     data= user.buy_mentor(userid,joinid)
#     return {'status':data}

# @app.post('/EnrollCourse')
# def EnrollMentor(userid,joinid):
#     data= user.buy_course(userid,joinid)
#     return {'status':data}

# @app.post('/joinus/Individual_Author')
# def joinus(First_name,Last_name,Email,Raw_Password,IDCard,About,Qualification):

#     import joinus
#     data=joinus.signup_individual_author(First_name,Last_name,Email,Raw_Password,IDCard,About,Qualification)
#     return data

# @app.post('/joinus/Mentor')
# def mentor(First_Name,Last_Name,Email,Password,IDCard,Qualification,About,Session_Price):


#     import joinus
#     data=joinus.signup_mentor(First_Name,Last_Name,Email,Password,IDCard,Qualification,About,Session_Price)

#     return {'status':data}

# @app.post('/addcourse')
# def addcourse(Course_name,Join_id,Catgory,Price_enroll,Price_course,Desc,Author,Rating,Date,classs,Pendrive,cd,Type,Start_date,Duration):
#     import course
#     data=course.AddCouse(Course_name,Join_id,Catgory,Price_enroll,Price_course,Desc,Author,Rating,Date,classs,Pendrive,cd,Type,Start_date,Duration)
#     return {'status':data}

# # @app.post('/joinus/University')
# # def University(University_Name,Department_Name,About,Email,Password):

#     import joinus
#     data=joinus.signup_university(University_Name,Department_Name,About,Email,Password)

#     return {'status':data}

# @app.post('/search')
# def search(search):
#     import course
#     data = course.search(search)
#     import json
#     final_data=json.loads(data)
#     return final_data

# if __name__ == "__main__":
#     uvicorn.run("main:app", port=5000, log_level="info")

if __name__=='__main__':
    app.run(debug=True)
