'''
기본(default) 인자
키워드 인자
가변 인자
키워드 인자
'''


def add_txt(t1, t2='python'):
    print(t1 + ':' + t2)


add_txt('베스트')
add_txt(t2='대한민국', t1='1등')


def func1(*args):
    print(args)


def func2(w, h, **kwargs):
    print(kwargs)


func1()
func1(1, 2, 3, 4)
func2(10, 20)
func2(10, 20, depth=50, color='blue')
