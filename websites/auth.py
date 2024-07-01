from flask import Blueprint , request ,render_template, flash
from .model import signup , staff_signup
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
auth=Blueprint('auth',__name__)

@auth.route('/singup_validation',methods=['GET','POST'])
def signup_validation():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        age = request.form['age']
        sex = request.form['sex']
        contact_number = request.form['contact_number']
        email = request.form['email']
        password =request.form['password']
        print(f"Received form data: {fname}, {lname}, {age}, {sex}, {contact_number}, {email}, {password}")
        #database
        new_user = signup(fname=fname, lname=lname, age=age, sex=sex, contact_number=contact_number, email=email, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        flash("signup successfully")
        return render_template('login.html')
    return render_template('signup.html')

@auth.route('/login_validation', methods=['GET','POST'])
def login_validation():
    if request.method =='POST':
        email= request.form['email']
        password =request.form['password']

        user = signup.query.filter_by(email=email).first()
        if user and check_password_hash(user.password , password):
            flash('Logged in successfully')
            return render_template('userin.html')
        else:   
            flash('invalid emailid or passsword')
            return render_template('userin.html.')
    return render_template('login.html')

@auth.route('/staff_singup_validation',methods=['GET','POST'])
def staff_signup_validation():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        designation =request.form['designation']
        age = request.form['age']
        sex = request.form['sex']
        contact_number = request.form['contact_number']
        email = request.form['email']
        password =request.form['password']
        # print(f"Received form data: {fname}, {lname}, {age}, {sex}, {contact_number}, {email}, {password}")
        #database
        new_user1 = staff_signup(fname=fname, lname=lname, designation =designation, age=age, sex=sex, contact_number=contact_number, email=email, password=generate_password_hash(password))
        db.session.add(new_user1)
        db.session.commit()
        return render_template('login.html')
    return render_template('signup.html')

@auth.route('/staff_login_validation', methods=['GET','POST'])
def staff_login_validation():
    if request.method =='POST':
        email= request.form['email']
        password =request.form['password']
        user = staff_signup.query.filter_by(email=email).first()
        if user and check_password_hash(user.password , password):
            flash('Logged in successfully')
            return render_template('home.html')
        else:
            flash('invalid emailid or passsword')
            return render_template('login.html')
    return render_template('login.html')


@auth.route('/abc', methods =['GET'])
def index():
    # users = signup.query.all()
    # return render_template('userin.html', users=users)
    try:
        users =signup.query.all()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        users = []
    return render_template('userin.html', users=users)
