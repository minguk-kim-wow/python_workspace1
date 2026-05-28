import pickle

# [1] Student 클래스 정의
class Student:
    # __init__ 은 클래스를 생성할 때 자동으로 실행되는 '초기화(생성자)' 메서드입니다.
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        
        # 총점과 평균을 클래스 내부에서 자체적으로 계산
        self.total = self.kor + self.eng + self.math
        self.avg = self.total / 3
        self.grade = self.calculate_grade()

    # 평균 점수를 기준으로 수우미양가를 반환하는 메서드
    def calculate_grade(self):
        if self.avg >= 90:
            return "수"
        elif self.avg >= 80:
            return "우"
        elif self.avg >= 70:
            return "미"
        elif self.avg >= 60:
            return "양"
        else:
            return "가"

    # 요구사항 반영: 학생 정보를 딕셔너리 형태로 반환하는 메서드
    def get_info_dict(self):
        return {
            "학생 이름": self.name,
            "국어 성적": self.kor,
            "영어 성적": self.eng,
            "수학 성적": self.math,
            "총점": self.total,
            "평균": self.avg,
            "평균 등급": self.grade
        }
    

# 학생 객체들을 담을 리스트
student_list = []

# [2] 메인 프로그램 실행 부분
while True:
    input_name = input("이름 (종료하려면 '종료' 입력) : ")
    
    if input_name == "종료":
        print("프로그램을 종료합니다.")
        break

    score_kor = int(input("국어점수 : "))
    score_eng = int(input("영어점수 : "))
    score_math = int(input("수학점수 : "))
    
    # 에러 수정: score라는 단일 변수 대신, 입력받은 3과목 모두 정상 범위인지 체크
    if not (0 <= score_kor <= 100 and 0 <= score_eng <= 100 and 0 <= score_math <= 100):
        print("입력한 점수가 정상범위 밖입니다. 점수를 똑디 입력해라잉")
        continue # break를 쓰면 프로그램이 꺼지므로, continue를 써서 위로 다시 돌려보냅니다.

    # [3] 클래스를 이용해 인스턴스(객체) 생성
    # 이때 __init__ 함수가 실행되면서 총점, 평균, 등급이 자동으로 계산됩니다.
    new_student = Student(input_name, score_kor, score_eng, score_math)
    
    # 딕셔너리 형태로 변환하여 리스트에 저장 (요구사항 충족)
    student_list.append(new_student.get_info_dict())

    # 결과 출력: 평균만 수우미양가로 출력
    print(f"👉 [{new_student.name}] 학생의 평균은 {new_student.avg:.1f}점이며, 평균 등급은 '{new_student.grade}' 입니다.\n")