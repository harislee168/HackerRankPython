if __name__ == '__main__':
    
    studentDic = dict()
    
    def processStudentDic():
        scoreList = list(studentDic.values())
        scoreList.sort()
        nameList = list()
        for name in studentDic:
            if studentDic[name] == scoreList[1]:
                nameList.append(name)
        nameList.sort()
        for i in nameList:
            print(i)
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        studentDic.update({name:score})
    processStudentDic()
