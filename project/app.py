from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import random
from flask import redirect,render_template,url_for,request,session,jsonify
from datetime import datetime
import math
import os
import os
import numpy as np

app = Flask(__name__)

file_dir = os.path.dirname(__file__) 

goal_route = os.path.join(file_dir , "app.db")

e = str(random.randint(10000,99999))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+ goal_route

db = SQLAlchemy(app)

app.secret_key = "cjdssjgghvgxfgngxmcmvvgkkgchxhzg"


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.Text, nullable=False)


with app.app_context():
    db.create_all()

@app.route('/')
def home():
    if session.get('user_name') and session.get('user_password'):
        return redirect('/use_AI_for_physics')
    else:
        return redirect('/login')

@app.route('/login')
def login():
    return render_template('form/form.html')

@app.route('/submit', methods=['POST'])
def submit():

    name = request.form['username']
    password = request.form['password']
    session["user_name"] = name 
    session["user_password"] = password
    session.permanent = True
    user = User(name = name , password = password)
    db.session.add(user)
    db.session.commit()
    return redirect('/')

@app.route('/voorood')
def voorood():
        return render_template('form/form2.html')

@app.route('/submit-voorood')
def submit_voorood():
    username = request.form['username']
    password = request.form['password']
    username_check = User.query.filter(User.name == username ).scalar() is not None
    password_check = User.query.filter(User.name == password).scalar() is not None
    if username_check and password_check:
        return redirect('/')
    else:
        return redirect('/voorood')

@app.route('/about-us')
def about():
    if session.get('user_name') and session.get('user_password'):
        return render_template('us/about_us.html')
    else:
        return redirect('/login')

@app.route('/use_AI_for_physics')
def use_AI():
    if session.get('user_name') and session.get('user_password'):
        return render_template('main-use.html')
    else:
        return redirect('/login')

@app.route("/api/sim1", methods=["POST"])
def get_data_sim1():
    data = request.get_json()
    speed = float(data.get("speed", 1))
    y0 = float(data.get("y0", 1))
    angle = float(data.get("angle", 1))
    resistance = float(data.get("resistance", 0))
    time = float(data.get("time", 5))

    ax=0
    ay=-10.
    t = np.linspace(0,time,50)
    v0x=speed*math.cos(angle)
    v0y=speed*math.sin(angle)

    vx = v0x+ ax*t
    vy = v0y + ay*t
    x = vx * t 
    y = 1.0/2*ay*t**2 + v0y * t + y0

    signals = {
        "X [m]": x.tolist(),
        "Y [m]": y.tolist(),
        "Vx [m/s]": vx.tolist(),
        "Vy [m/s]": vy.tolist(),
    }

    return jsonify({
        "x": t.tolist(),
        "signals": signals
    })

@app.route("/api/sim2", methods=["POST"])
def get_data_sim2():

    data = request.get_json()
    speed = float(data.get("speed", 1))
    y0 = float(data.get("y0", 1))
    resistance = float(data.get("resistance", 0))
    time = float(data.get("time", 5))

    a=-10.
    t = np.linspace(0,time,50)

    v = a*t + speed
    y = 1.0/2*a*t**2 + speed * t + y0

    signals = {
        "Y [m]": y.tolist(),
        "V [m/s]": v.tolist(),
        "Y1 [m]": y.tolist(),
        "V4 [m/s]": y.tolist()
    }

    return jsonify({
        "x": t.tolist(),
        "signals": signals
    })

@app.route('/use_AI_for_physics/sim1')
def sim1():
    if session.get('user_name') and session.get('user_password'):
        return redirect('/use_AI_for_physics/sim1/result')
    else:
        return redirect('/login')

@app.route('/use_AI_for_physics/sim1/result')
def sim1_result():
    return render_template('physics/sim1/result.html')

@app.route('/use_AI_for_physics/sim2')
def sim2():
    if session.get('user_name') and session.get('user_password'):
        return redirect('/use_AI_for_physics/sim2/result')
    else:
        return redirect('/login')

@app.route('/use_AI_for_physics/sim2/result')
def sim2_result():
    return render_template('physics/sim1/result2.html')

@app.route('/call-us')
def ertebat():
    if session.get('user_name') and session.get('user_password'):
        return render_template('us/call_us.html')
    else:
        return redirect('/login')
    
@app.route('/use_AI_for_physics/sim3')
def sim3():
    return render_template('physics/sim3/index.html')

@app.route('/use_AI_for_physics/sim3/result',methods=["POST"])
def sim3_result():
    f =  request.form['f']
    d = request.form['d']
    theta = request.form['theta']
    f2 = int(f)
    d2 = int(d)
    theta2 = math.cos(math.radians(int(theta)))
    theta3 = round(theta2,10)
    
    print(theta2)
    print(theta3)
    wf = f2*d2*theta3
    return render_template('physics/sim3/result.html',
                           f = f,
                           d =d,
                           theta = theta,
                           wf = wf)

@app.route('/ertebat-submit',methods=["POST"])
def ertebat_submit():
        first_name=request.form.get('user_name','no user-name')
        last_name=request.form.get('lastname','no-password')
        message=request.form.get('message','no-message')
        try:
            with open('my_file.txt', 'a') as file: 
                file.write(f'name:{first_name}  last_name:{last_name}  message:{message} \n \n'  ) 
                return redirect('/call-us')
        except Exception as e:
            return f"An error occurred: {e}"
        
@app.route('/use_AI_for_physics/sim4')
def sim4():
    return render_template('physics/sim4/index.html')

@app.route('/use_AI_for_physics/sim4/result' , methods=['POST'])
def sim4_submit():
    m = request.form['m']
    g = request.form['g']
    h = request.form['h']
    m1 = int(m)
    g1 = int(g)
    h1 = int(h)
    wg = m1*g1*h1
    
    return render_template('physics/sim4/result.html',
                           m=m,
                           g=g,
                           h=h,
                           wg=wg)
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
