# • 딕셔너리를 통해 7개의 단어를 미리 등록해 놓음
# • 사용자가 조회한 단어의 뜻을 화면에 출력하는 기능을 구현
# • 사용자가 0을 입력할 때까지 무한히 조회

words = {"apple" : "사과",
         "food" : "음식",
         "dog" : "개",
         "cat" : "고양이",
         "world" : "세계",
         "student" : " 학생",
         "friend" : "친구"}

while True :
    myWord = input(str(list(words.keys()))+"중 무엇을 조회할까요?")
    if myWord == "0" :
        break
    elif myWord not in words :
        print("없는 단어입니다.")
        continue
    print(words[myWord])

print("사전 프로그램 종료")

# [문제] if와 break로 종료시키도록 코드를 작성하시오.