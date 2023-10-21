from flask import *

app = Flask('__main__')

@app.route("/")
def index():
    return render_template("index.html", flask_token="Testando")

app.run(port=8080, debug=True)