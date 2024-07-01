from flask import Blueprint,render_template , request

views =Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/signup') 
def signup():
    return render_template('signup.html')

@views.route('/login')
def login():
    return render_template('login.html')

@views.route('/staff_signup')
def staff_signup():
    return render_template('staff_signup.html')

@views.route('/staff_login')
def staff_login():
    return render_template('staff_login.html')


