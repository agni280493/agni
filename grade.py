def grades(a):

    student_grades = {}
    student_grades.update(a)
    for i in student_grades.keys():
        if 91<=student_grades[i]<= 100:
            student_grades[i] = "outstanding"
        elif 81<=student_grades[i]<=90:
            student_grades[i] = "exceeds expectations"
        elif 71 <= student_grades[i] <= 80:
            student_grades[i] = "acceptable"
        elif student_grades[i] <=70:
            student_grades[i] = "fail"

    print(student_grades)
    print(student_scores)

student_scores ={"harry":91,"ron": 78,"hermi":99,"draco":74,"Neville":62}
grades(student_scores)

