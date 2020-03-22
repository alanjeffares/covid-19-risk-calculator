from flask import Flask,render_template, url_for, request
import utils

app=Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    userQ = []
    decisQ =[]
    # Activity form
    test_dict = {}
    user_question_list = utils.json_loader('user_questions.json')
    decision_question_list = utils.json_loader('decision_questions.json')


    for idx in range(len(user_question_list)):
        id_ = user_question_list[idx]['id']
        # creates list of questions to populate the page with
        test_dict[f'question_{id_}'] = user_question_list[idx]

    for idx in range(len(decision_question_list)):
        id_ = decision_question_list[idx]['id']
        # creates list of questions to populate the page with
        test_dict[f'question_{id_}'] = decision_question_list[idx]

# When submit is clicked
    if request.method == "POST":
        
        
        # loop through questions and store respective answers
        for idx in range(len(user_question_list)):
            id_ = user_question_list[idx]['id']
            try:
                user_question_list[idx]['response'] = request.form[f'response_{id_}']
                userQ.append(user_question_list[idx]['response'])
            except:
                pass

        for idx in range(len(decision_question_list)):
            id_ = decision_question_list[idx]['id']
            try:
                decision_question_list[idx]['response'] = request.form[f'response_{id_}']
                decisQ.append(decision_question_list[idx]['response'])
            except:
                pass


    # Inputted values will be outputted to the screen when submit button is clicked [test]
    return render_template("home.html", content=test_dict, user=userQ, decision=decisQ)


if __name__ == "__main__":
    app.run(debug=True)