# Riya Autade 22BBS0079

from flask import Flask, render_template

application = Flask(__name__, static_folder="static")

@application.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000, debug=True)

