from flask import Flask 
app = Flask(__name__)

@app.route("/")
def index():
	return "welcome to flask app using the gunicorn server"

if __name__ == "__main__" :
	app.run(host="0.0.0.0")

