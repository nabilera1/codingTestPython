import time
import mypackage
import mypackage.mymodule1
print('Hello')
time.sleep(2)
print('Good Bye')

ret1=mypackage.mymodule1.add1(1,2)
print(ret1)
'''
안정성이 검증되거나 비슷한 성향의 활용도가 높은 함수 등을 파이썬 파일로 묶어 놓은 것을 모듈이라 한다.
모듈은 import해서 사용한다.
time은 내장 모듈이다.
sleep은 time 파일에 정의된 함수 이름이다.
'''