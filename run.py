from flask import Flask,render_template, url_for, request
import utils
import main

app=Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
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
            except:
                raise ValueError

        for idx in range(len(decision_question_list)):
            id_ = decision_question_list[idx]['id']
            try:
                decision_question_list[idx]['response'] = request.form[f'response_{id_}']
            except:
                pass

        user = main.User()
        user.parse_responses(user_question_list)
        user.calculate_risk()
        decision = main.Decision()
        decision.parse_responses(decision_question_list)
        decision.evaluate_responses()
        print(user.risk, decision.response_list)

    # Inputted values will be outputted to the screen when submit button is clicked [test]
    return render_template("home.html", content=test_dict)



if __name__ == "__main__":
    app.run(debug=True)