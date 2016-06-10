#-- Flask Hello World --#

# import the Flask class from the flask package
from flask import Flask

#create the appliaction object
app = Flask(__name__)

#Error handling
app.config["DEBUG"] = True

#use decorators to link the function to a url
@app.route("/")
@app.route("/hello")

#define the view using a function, which returns a string
def hello_world():
	return "Hello, is anyone out there?!?!?!"

#dynamic route
@app.route("/test/<search_query>")
def search(search_query):
	return search_query

#integer route
@app.route("/integer/<int:value>")
def int_type(value):
	print(value + 1)
	return "correct"

#floating point route
@app.route("/float/<float:value>")
def float_type(value):
	print(value + 1)
	return "correct"

#dynamic route that accepts slashes
@app.route("/path/<path:value>")
def path_type(value):
	print(value)
	return "correct"

@app.route("/name/<name>")
def index(name):
	if name.lower() == "michael":
		return "Hello, {}".format(name), 200
	else:
		return "Not Found", 404

#start the development server using the run() method
if __name__ == "__main__":
	app.run()