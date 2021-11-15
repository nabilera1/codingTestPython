# • 1번 기능(1번 입력): 영어 단어와 뜻을 세트로 등록
# • 2번 기능(2번 입력): 등록된 영어 단어 삭제
# • 3번 기능(3번 입력): 등록된 영어 단어 조회(원래 있던 기능)
# • 사용자가 0을 입력할 때까지 무한히 조회

words = {}
while True :
    sel=int(input("사전 프로그램 [1 : 단어 입력 / 2 : 단어 삭제 / 3 : 단어 조회 / 0 : 종료]"))
    if sel == 0 :
        break
    elif sel == 1 :
        while True :
            word1 = input("단어 : ")
            if word1 not in words :
                break
            print("이미 등록된 단어입니다.")
        words[word1] = input("단어 뜻 : ")
        print(words)
    elif sel == 2 :
        print(words)
        while True :
            word1 = input("삭제할 단어 : ")
            if word1 in words :
                break
            print("없는 단어입니다.")
        del(words[word1])
        print(words)
    elif sel == 3 :
        while True :
            myWord = input(str(list(words.keys()))+"중 무엇을 조회할까요?")
            if myWord in words :
                break
            print("없는 단어입니다.")
        print(words[myWord])
    else :
        print("1, 2, 3, 0 중 하나를 입력해주세요.")

print("사전 프로그램 종료")