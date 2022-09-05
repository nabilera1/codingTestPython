# [나의 용어 사전 만들기]
# My Glossary
#
# 지금까지 학습한 것을 다시 정리해보겠습니다.
# . 연산자는 클래스가 가지고 있는 메서드를 호출할 때 사용된다.
# tkinter의 모든 위젯 클래스에는 grid() 메서드가 있다.
# 위젯 생성 후 텍스트 위젯과 같이 위젯의 결과값을
# 다음에 다시 사용하려면, 별도의 변수를 만들어 값을 할당해 두어야합니다.

from tkinter import *

w=Tk()
w.geometry('400x200')
w.title("나의 용어 사전")
myData={#딕셔너리 (key, value), myData['BTS']
    "BTS":"is a seven-member South Korean boy band "\
          "that was formed in 2010 and debuted in 2013",
    "Messi":"is an Argentine professional footballer " \
            "who plays as a forward for Ligue 1 club " \
            "and captains the Argentina national team.",
    "Vietnam":"officially the Socialist Republic of Vietnam," \
              "is a country in Southeast Asia."
}
lbl=Label(w, text="단어 입력 후 엔터 키를 누르세요. ")
lbl.grid(row=0,column=0, sticky=W)#West

entry=Entry(w, width=20, bg="light yellow")
entry.grid(row=1,column=0, sticky=W)

def click():
    txt=entry.get()
    txtBox.delete(0.0,END) #줄번호.문자위치
    try:
        explain=myData[txt]
    except:
        explain="단어를 찾을 수 없음"
    txtBox.insert(END,explain)

Button(w, text="설명 찾기", width=10, command=click).grid(row=2,\
        column=0, sticky=W)
Label(w, text="\n정의 :").grid(row=3, column=0, sticky=W)
txtBox=Text(w,width=70, height=6, wrap=WORD, bg="light green")
txtBox.grid(row=4, column=0, columnspan=2, sticky=W)
w.mainloop()



# [문제] 도전과제
# 영어 단어와 뜻을 넣어 영어단어장 프로그램을 만들어 보시오.
