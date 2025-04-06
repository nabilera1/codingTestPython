import itertools

# 파일 생성
files = ["file1.txt", "file2.txt", "file3.txt"]

# 각 파일에 내용 쓰기, 한글의 경우 encoding="utf-8" 사용
with open("file1.txt", "w", encoding="utf-8") as f:
    f.write("학교 종이 땡땡땡\n")
    f.write("어서 모이자\n")

with open("file2.txt", "w", encoding="utf-8") as f:
    f.write("선생님이 우리를\n")
    f.write("기다리신다.\n")

with open("file3.txt", "w", encoding="utf-8") as f:
    f.write("즐겁고 즐거운\n")
    f.write("나의 학교 생활\n")



# 파일 열기 및  각 파일의 줄을 연결하여 출력
file_objects = [open(file, 'r', encoding='utf-8') for file in files]  # 파일 객체 리스트 생성
try:
    lines = itertools.chain(*file_objects)    # 파일 객체의 내용을 연결
    for line in lines:
        print(line.strip())
finally:
    for file in file_objects:                 # 파일 객체 닫기
        file.close()


# 각 파일의 줄을 연결하여 출력, 아래 코드 에러 발생
# with itertools.chain(*(open(file, encoding='utf-8') for file in files)) as lines:
#     for line in lines:
#         print(line.strip())

# 에러가 발생한 이유 요약
# 각 파일 객체를 열 때 with 문이 파일 객체를 닫도록 설계해야 합니다.
# 그러나 itertools.chain은 context manager가 아니므로 파일 객체를 적절히 닫지 않습니다.
# 이 때문에 첫 번째 해결 방법(try-finally 방식)이 더 안전합니다.
# itertools.chain은 with 문에서 사용할 수 없는 객체입니다(즉, context manager가 아님).
# with 문은 파일 객체와 같이 __enter__와 __exit__ 메서드를 구현한 객체에서만 동작합니다.