# 음식점 손님 받기 시스템

# • 빈자리가 생기면 예약자를 순서대로 입장시키는 시스템
# • 새로운 손님이 왔을 때 빈자리가 있으면 즉시 착석시킴(이름 출력)
# • 빈자리가 없을 경우: 순번대로 예약자 명단 관리- 손님이
# 퇴장하여 자리가 생길 때, 예약자 명단 중 제일 빨리 예약한
# 손님을 착석시킴(이름 출력)  (단, 모든 손님의 이름은 중복되지 않는다고 가정함)
# - 식사 테이블은 총 5개라고 가정함.

reserver=[]
tables=[]

while True :
    sel = int(input("< 1: 손님 입장 / 2: 손님 퇴장 / 0 : 프로그램 종료 >"))
    if sel == 0 :
        break
    elif sel == 1:
        name = input("입장 손님 성명 : ")
        if len(tables) < 5 :
            tables.append(name)
            print(name,"님 입장\n", tables)
        else :
            reserver.append(name)
            print(name,"님 예약\n", reserver)
    elif sel == 2:
        name = input("퇴장 손님 성명 : ")
        if name not in tables:
            print(name, "님 성명이 틀렸습니다\n", tables)
            continue
        tables.remove(name)
        print(name,"님 퇴장\n", tables)
        if len(reserver) > 0 :
            name = reserver[0]
            del(reserver[0])
            tables.append(name)
            print(name,"님 입장\n", tables)


# < 1: 손님 입장 / 2: 손님 퇴장 / 0 : 프로그램 종료 >1
# 입장 손님 성명 : 김동균
# 김동균 님 입장
#  ['김동균']
# < 1: 손님 입장 / 2: 손님 퇴장 / 0 : 프로그램 종료 >1
# 입장 손님 성명 : 김철수
# 김철수 님 입장
#  ['김동균', '김철수']
# < 1: 손님 입장 / 2: 손님 퇴장 / 0 : 프로그램 종료 >2
# 퇴장 손님 성명 : 김동수
# 김동수 님 성명이 틀렸습니다
#  ['김동균', '김철수']
# < 1: 손님 입장 / 2: 손님 퇴장 / 0 : 프로그램 종료 >