#학생 이름을 입력받아 정렬하여 출력하기
#입력 : 홍길동 강감찬 이순신
#출력 : 강감찬 이순신 홍길동
name=list(input().split())
for i in sorted(name):
    print(i, end=' ')

