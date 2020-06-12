from flask import Flask,request,jsonify
# from twilio.
import requests
import json 


app = Flask(__name__)

@app.route('/')
def hello():
    return "hello world"

@app.route('/login/',methods=["POST"])
def login():
    username = request.json.get('email')
    password = request.json.get('password')
    print(username)
    data = {
        'email':username,
        'password':password
    }
    url = 'http://land-title.herokuapp.com/api/v1/auth/users/signin'
    r = requests.post(url,data)
    if r.status_code == 200:
        print(r.json()['data'])
        print(r.status_code)
        return r.json()['data']
    else:
        return r.json()
@app.route('/register/',methods=["POST"])
def register():
    firstName = request.json.get('firstName')
    lastName = request.json.get('lastName')
    email = request.json.get('email')
    password = request.json.get('password')
    data = {
        
        'firstName':firstName,
        'lastName':lastName,
        'email':email,
        'password':password
    }
    url = 'http://land-title.herokuapp.com/api/v1/auth/users/signup'
    r = requests.post(url,data)
    if r.status_code == 200:
        return r.json()
    else:
        return r.json()
    # print(r.status_code)
    return "hey"
@app.route('/titles/',methods=["GET","POST"])
def titles():
    url = 'http://land-title.herokuapp.com/api/v1/titles/'
    token  = request.headers['Authorization']
    headers = {
    'Content-Type': "application/json",
    'Authorization': token
    }
    r = requests.get(url,headers=headers)
    if r.status_code == 200:
        return r.json()
    else:
        return r.json()
@app.route('/titles/post/',methods=["POST"])
def title_post():
    url = 'http://land-title.herokuapp.com/api/v1/titles/'
    token = request.headers['Authorization']
    headers = {
        # 'Content-Type': "application/json",
    'Authorization': token
    }
    title = request.json.get('title','')
    squareMeter = request.json.get('squareMeter','')
    mortgage = request.json.get('mortgage','')
    address = request.json.get('address','')
    data  = {
    "title":title,
    "squareMeter":squareMeter,
    "mortgage":mortgage,
    "address":address
    }
    r = requests.post(url,data,headers=headers)
    if r.status_code == 200:
        return r.json()
    else:
        print(r.json())
        return r.json()
@app.route('/titles/search/',methods=["GET"])
def search_title():
    term = request.args['title']
    url = f'http://land-title.herokuapp.com/api/v1/titles/search?param={term}'
    print(url)
    headers = {
        # 'Content-Type': "application/json",
    'Authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjVlZTMzMTg4ZGI4ZmNhMDAyYWE0NDZiMCIsImlhdCI6MTU5MTk0ODYwOSwiZXhwIjoxNTkyMDM1MDA5fQ.xnPeDXD4ZsMpHXiG3JdGayu9Dcew7jUZp4tdFF7kTYw"
    }
    r = requests.get(url,headers=headers)
    if r.status_code == 200:
        return r.json()
    else:
        return r.json()
# @app.route('/logout',methods=["GET","POST"])
# def logout():
#     url = 
if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)