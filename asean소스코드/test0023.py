# 20 30 50
# a, b, c=20,30,40
# print('a=',a,'b=',b,'c=',c)

# a, b, c=map(int,input().split())
# print('a=',a,'b=',b,'c=',c)
# print(a+b+c)

# [문제]
# 영어 수학 과학 세 과목의 평균이 80점 이상이면 ‘합격’,
# 그렇지 않으면 ‘불합격’이 되는 프로그램을 작성하시오.
# (단, 입력 점수는 0보다 크고 100보다 작다)
# 60 70 80
# 불합격
#
# 80 90 120
# 잘못된 점수
#
# 90 80 90
# 합격

english, math, science=map(int, input().split())
avg=(english+math+science)/3
if english<0 or english>100 or \
    math<0 or math>100 or \
    science<0 or science>100:
    print('잘못된 점수')
else:
    if avg>=80:
        print('합격')
    else:
        print('불합격')
