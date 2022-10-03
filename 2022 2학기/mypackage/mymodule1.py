'''
파이썬 패키지 이해하기

파이썬 모듈을 계층적인 디렉터리 형태로 구성
디렉터리를 파이썬 패키지로 인식하게 하려면 계층적으로 이루어져 있는 각 디렉터리마다
__init__.py 파일이 있어야 한다.

--init__.py 에는 version=1.0 등을 넣어두면 된다.

이제 패키지 밖의 경로에서
import mypackage
ret1=mypackage.mymodule1.add1(1,2) 를 사용할 수 있다.
'''

def add1(a,b):
    return a+b

def mul1(a, b):
    return a*b
