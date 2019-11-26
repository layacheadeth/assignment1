score = float(input("score: "))
def prompt_score(score):
    if score <=1.0 and score > 0.0:
        if score >= 0.9:
            grade = "A"
        elif score < 0.9 and score >=0.8:
            grade = "B"
        elif score < 0.8 and score >=0.7:
            grade = "C"
        elif score < 0.7 and score >=0.6:
            grade = "D"
        else:
            grade = "F"
        print("grade: ",grade)
    else:
        print("error input")
prompt_score(score)