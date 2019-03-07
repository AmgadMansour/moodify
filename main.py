from flask import Flask, render_template

#instance of flask class
app = Flask(__name__)

#default page (function home will get activated when going to home route "/")
# render template looks for template (html) in templates folder
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)


#venv: virtual enviroment is to create a separate environment (python version, depndecies, packages) for this project
# we need to activate venv, then install flask


# Refrences:
# https://medium.freecodecamp.org/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492