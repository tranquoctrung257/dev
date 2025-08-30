# 28

def main():
    Students_A_name = "Dung"
    Students_A_math_score = 9
    Students_A_literature_score = 6
    Students_B_name = "Nguyen"
    Students_B_math_score = 5
    Students_B_literature_score = 10
    print_Student(Students_A_name,Students_A_math_score,Students_A_literature_score)
    print_Student(Students_B_name,Students_B_math_score,Students_B_literature_score)

def print_Student(name,math_score,literature_score):
    print("Student name: "+name)
    print("Math: " + str(math_score))
    print("literature: "+ str(literature_score))



main()