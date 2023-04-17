if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    for name_key in student_marks.keys():
        if query_name == name_key:
            score_list = student_marks[name_key]
            average = sum(score_list)/len(score_list)
            print("{:.2f}".format(average))
            break