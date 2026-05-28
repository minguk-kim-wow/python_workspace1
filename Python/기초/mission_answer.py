# [1] Student 클래스 정의
class Student:
    # __init__ 은 클래스를 생성할 때 자동으로 실행되는 '초기화(생성자)' 메서드입니다.
    def __init__(self, name=" ", kor=0, eng=0, math=0):
        self.name=name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.process()
        

    # 평균 점수를 기준으로 수우미양가를 반환하는 메서드
    def process(self):
        self.total = self.kor + self.eng + self.math
        self.avg = self.total/3
        if self.avg >= 90:
            self.grade= "수"
        elif self.avg >= 80:
            self.grade= "우"
        elif self.avg >= 70:
            self.grade= "미"
        elif self.avg >= 60:
            self.grade= "양"
        else:
            return "가"


    def output(self):
        print(self.name, end="\t")
        print(self.kor, end="\t")
        print(self.eng, end="\t")
        print(self.math, end="\t")
        print(self.total, end="\t")
        print(f"{self.avg:.2f}", end="\t")
        print(self.grade)
        
        
#s1 = Student("a",90,80,70)
#s1.output()

class StudentManager:
    def __init__(self):
        self.stList=[
            Student("a",90,80,70),
            Student("b",90,90,90),
            Student("c",40,80,70)
        ]
    def output(self):
        for st in self.stList:
            st.output()

    def sort(self):
        resultList = sorted(self.stList, key = lambda ob : ob.total, reverse=True)
        for r in resultList:
            r.output()

mgr = StudentManager()
mgr.output()
print("-"*20)
mgr.sort()