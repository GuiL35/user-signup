from flask import Flask,request
import cgi
import os 
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    template = jinja_env.get_template('signup.html')
    return template.render()


@app.route("/signup", methods = ['POST'])
def user_signup():
    saved_user_info = ["username","email"]
    signup_name = request.form['username']
    password = request.form['password']
    verification = request.form['verification']
    template = jinja_env.get_template('welcome_greeting.html')
    saved_username_email= request.args.get('saved_user_info')
    return template.render(username = signup_name, password=password,verification=verification, saved_username_email= saved_username_email )

app.run()