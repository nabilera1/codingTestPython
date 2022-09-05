#파이썬 자료구조 (리스트)
what_day=["Mon","Tue","Wed","Thu","Fri"]
print(what_day)
print(len(what_day))
print(what_day[0])
print(what_day[2])
print(what_day[4])
what_day[4]="My day"
print(what_day)
what_day.append("Holiday")
print(what_day)
what_day.append("Sun")
print(what_day)
print(what_day.index('Sun')+1,'번째 있습니다.')

# [문제]
# what_day 리스트에 “Good day”를 추가하고 전체 리스트를 출력해 보세요.
what_day.append("Good day")
print(what_day)
