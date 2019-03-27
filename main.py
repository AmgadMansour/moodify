import base64

from flask import Flask, render_template,request,redirect,jsonify, json, make_response
from PIL import Image
from mood import main_func

# from mood import  main_func
# import base64
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

@app.route('/music', methods=['POST', 'GET'])
def music():
   mood = main_func()
   return redirect("/player?mood=" + mood)

@app.route("/test", methods=['POST', 'GET'])
def test():
	if request.method == 'POST':
		req = request.json
		s = req["img64"]
		print(type(s))
		#print(s)
		# Take in base64 string and return byte arrary
		imgdata = base64.b64decode(s)

		f = open("snap.jpg", "wb")
		f.write(imgdata)
		f.close()
		print(type(imgdata)) #byte array
		return True
	# if request.method == 'GET':
	# 	return render_template("test.html",variable=s)

# @app.route('/player/<emotion>') #auto rendering in html player
# def test(name):
#         return render_template("test.html", variable = name)



if __name__ == "__main__":
    app.run(debug=True)



#venv: virtual enviroment is to create a separate environment (python version, depndecies, packages) for this project
# we need to activate venv, then install flask


# Refrences:
# https://medium.freecodecamp.org/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492