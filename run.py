from flask import Flask,render_template, url_for, request
import utils

app=Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    # Activity form
    kwargs = {}
    question_list = utils.json_loader('questions.json')
    if request.method == "POST":
        # loop through questions and store respective answers
        for idx in range(len(question_list)):
            id_ = question_list[idx]['id']
            question_list[idx]['response'] = request.form[f'response_{id_}']
            kwargs[f'question_{id_}'] = question_list[idx]

    # Inputted values will be outputted to the screen when submit button is clicked [test]
    return render_template("home.html", **kwargs)


if __name__ == "__main__":
    app.run(debug=True)