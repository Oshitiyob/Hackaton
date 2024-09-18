import random
questions = {
    'stop': 'מה מורה התמרור?'
}

# the correct answer is the first one on the list
answers = {
    'stop': ['עצור ותן זכות קדימה', 'תן זכות קדימה', 'תן זכות קדימה (אין צורך לעצור)', 'עצור לרגע, בדוק את מצב התנועה והמשך בנסיעתך']
}
def questions_system(sign_name):
    answers_list = answers[sign_name]
    random.shuffle(answers_list)
    question_list = [questions[sign_name], [answers_list], answers[sign_name][0]]
    print('hi')
print(questions_system('stop'))