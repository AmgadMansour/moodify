from flask import Flask, render_template,request,redirect,jsonify
from mood import  main_func
import base64
#instance of flask class
app = Flask(__name__)

#default page (function home will get activated when going to home route "/")
# render template looks for template (html) in templates folder
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/player")
def player():
    return render_template("player.html")


@app.route('/emotion')
def emotion():
  # Get img data

  # Run script for emotion recognition
  mood = main_func()

  return jsonify(mood)

if __name__ == "__main__":
    app.run(debug=True)



#venv: virtual enviroment is to create a separate environment (python version, depndecies, packages) for this project
# we need to activate venv, then install flask


# Refrences:
# https://medium.freecodecamp.org/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492