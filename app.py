from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "chandana"
@app.route("/hello", methods=['GET', 'POST'])
def index():
	flash("what's your name?")
	return render_template("index.html")

@app.route("/greet", methods=['GET', 'POST'])
def greet():
	flash("Hi " + str(request.form['name_input']) + ", it's great to see you!")
	return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)