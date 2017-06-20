from flask import Flask,request


app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>

<html>
    <title>"Signup"</title>
    <body>
        <form action = "/signup", method = "POST">
            <label for = "username">Username<label>
            <input type = "text", id = "username" />

            <label for = "password">Password<label>
            <input type = "text", id = "password" />  

            <label for = "verification">Verfiy Password<label>
            <input type = "text", id = "verifcation" />  
                
            <label for = "email">Email(optional)<label>
            <input type = "text", id = "email" />

            <input type = "submit", id = "button" />
        </form>
    </body>
</html> """

@app.route("/")
def index():
    return form

@app.route("/signup", methods = ["POST"])
def user_signup():
    signup_name = request.form['username']
    return "welcome " + signup_name