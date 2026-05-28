import pickle

class Person :
    def __init__(self, name="", age=0):
        self.name=name
        self.age=age

    def output(self):
        print('name : ', self.name, "\tage : ", self.age)

perList = [Person("cat", 23),Person("dog", 33),Person("dragon", 19)]

with open("person.txt","wb") as f:
    pickle.dump(perList,f) #직렬화

    
with open("person.txt","rb") as f:
    s = pickle.load(file=f) #직렬화

for a in s:
    a.output()