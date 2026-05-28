persons = [
    {"name": "홍길동", "age": 23},
    {"name": "임꺽정", "age": 33},
    {"name": "장길산", "age": 27},
    {"name": "고길동", "age": 42},
]

# print(persons[0]["name"], persons[0]["age"])
# print(persons[1]["name"], persons[1]["age"])
# print(persons[2]["name"], persons[2]["age"])
# print(persons[3]["name"], persons[3]["age"])

for i in persons:
    print(i)

for i in range(0, len(persons)):
    print(persons[i]["name"], persons[i]["age"])