eren={'name','homework','quiz','test'}
mikasa={'name','homework','quiz','test'}
armin={'name','homework','quiz','test'}
eren = {
 "name": "Eren",
 "homework": [],
 "quizzes": [],
 "tests": []
}
mikasa = {
"name": "Mikasa",
"homework": [],
"quizzes": [],
"tests": []
}
armin = {
"name": "Armin",
"homework": [],
"quizzes": [],
"tests": []
}

eren = {
 "name": "Eren",
 "homework": [90.0,97.0,75.0,92.0],
 "quizzes": [88.0,40.0,94.0],
 "tests": [75.0,90.0]
}
mikasa = {
"name": "Mikasa",
"homework": [100.0, 92.0, 98.0, 100.0],
"quizzes": [82.0, 83.0, 91.0],
"tests": [89.0, 97.0]
}
armin = {
"name": "Armin",
"homework": [0.0, 87.0, 75.0, 22.0],
"quizzes": [0.0, 75.0, 78.0],
"tests": [100.0, 100.0]
}
students=[eren,mikasa,armin]
for each in students:
    print(each)
def average(numbers=[]):
    total = float(sum(numbers))
    average =total/len(numbers)
    return average
def get_average(students):

    return weighted_average