from amhohwaw import AM
import json


ID = input("이름을 입력하세요: ")
PS = input("비밀번호를 입력하세요: ")

LPS = list(PS)
i = len(LPS)
amho = []
p = 0

for i in range(i):
    amho.append(AM(LPS[p]))
    p += 1

RPS = "".join(amho)

with open('login.json', 'r', encoding="utf-8") as f:
    id = json.load(f)

if id.get(ID) == RPS:
    print("로그인 성공!")
else:
    print("계정 아이디 혹은 비밀번호가 다릅니다.")
