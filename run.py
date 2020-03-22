from flask import Flask,render_template, url_for, request
import utils

app=Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    # Activity form
    test_dict = {}
    ans_list = []
    tester =[]
    question_list = utils.json_loader('questions.json')

    for idx in range(len(question_list)):
        id_ = question_list[idx]['id']
        # creates list of questions to populate the page with
        test_dict[f'question_{id_}'] = question_list[idx]

# When submit is clicked
    if request.method == "POST":
        
        # loop through questions and store respective answers
        for idx in range(len(question_list)):
            id_ = question_list[idx]['id']
            try: 
                question_list[idx]['response'] = request.form[f'response_{id_}']
            except:
                pass

    # Inputted values will be outputted to the screen when submit button is clicked [test]
    return render_template("home.html", content=test_dict)


if __name__ == "__main__":
    app.run(debug=True)