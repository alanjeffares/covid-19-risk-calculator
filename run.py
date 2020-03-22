from flask import Flask,render_template, url_for, request

app=Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    # Activity form
    activity, duration = None, None
    if request.method == "POST":
        activity = request.form["activity"]
        duration = request.form["duration"]
    # Inputted values will be outputted to the screen when submit button is clicked [test]
    return render_template("home.html", activity=activity, duration=duration)


if __name__ == "__main__":
    app.run(debug=True)