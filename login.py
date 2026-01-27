import json
from amhohwaw import AM

while 1:
    ID = input("이름을 입력하세요: ")
    PS = input("비밀번호를 입력하세요: ")
    PSA = input("비밀번호를 다시 입력하세요: ")

    if PS != PSA:
        print("비밀번호가 다릅니다. 다시 입력해주세요")
    else:
        break

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

id[ID] = RPS

with open('login.json', 'w', encoding='utf-8') as f:
    json.dump(id, f, ensure_ascii=False)

print("로그인 저장 완료")
