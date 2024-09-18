import random
questions = {
    'stop': 'מה מורה התמרור?',
    'priority': 'מה מורה התמרור',
    'crossroad': 'מה משמעות התמרור',
    'urban area': 'מהי המהירות המותרת עד אשר יוגדר אחרת?'

}

# the correct answer is the first one on the list
answers = {
    'stop': ['עצור ותן זכות קדימה', 'תן זכות קדימה', 'תן זכות קדימה (אין צורך לעצור)', 'עצור לרגע, בדוק את מצב התנועה והמשך בנסיעתך'],
    'priority': [
        "עליך לתת זכות קדימה לרכבים הנעים בדרך החוצה, עם או בלי עצירה בהתאם לצורך.",  # תשובה נכונה
        "עליך לעצור עצירה מלאה בצומת ולהמתין עד שהדרך תהיה פנויה.",
        "עליך לפנות ימינה בלבד בצומת.",
        "עליך לתת זכות קדימה להולכי רגל במעבר חצייה."],
    'crossroad': [
        "עליך לתת זכות קדימה להולכי רגל החוצים את הכביש במעבר החצייה.",  # תשובה נכונה
        "עליך לעצור עצירה מלאה בכל מעבר חצייה, ללא קשר להולכי רגל.",
        "המעבר מיועד לכלי רכב בלבד, אין להולכי רגל להשתמש בו.",
        "עליך להאט ולאו דווקא לתת זכות קדימה להולכי רגל."],
    'urban area': [50, 30, 42, 70]




}
def questions_system(sign_name):
    answers_list = answers[sign_name].copy()
    random.shuffle(answers_list)
    question_list = [questions[sign_name], answers_list, answers[sign_name][0]]
    return question_list
print(questions_system('urban area'))
