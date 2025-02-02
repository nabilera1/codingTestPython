import itertools

# 파일 생성
files = ["file11.txt", "file22.txt", "file33.txt"]

with open("file11.txt", "w") as f:
    f.write("apple banana\n")
    f.write("cherry orange\n")

with open("file22.txt", "w") as f:
    f.write("grape lemon\n")
    f.write("apple kiwi\n")

with open("file33.txt", "w") as f:
    f.write("banana mango\n")
    f.write("cherry apple\n")

# 'apple' 키워드가 포함된 줄만 출력
# with itertools.chain(*(open(file) for file in files)) as lines:
#     result = [line.strip() for line in lines if "apple" in line]
#     print(result)

file_objects = [open(file, 'r') for file in files]  # 파일 객체 리스트 생성
try:
    lines = itertools.chain(*file_objects)    # 파일 객체의 내용을 연결
    result = [line.strip() for line in lines if "apple" in line]
    print(result)
finally:
    for file in file_objects:                 # 파일 객체 닫기
        file.close()