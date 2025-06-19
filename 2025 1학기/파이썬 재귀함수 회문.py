# 재귀 함수
#
# 문자열 인덱싱
#
# 기본적인 조건문



def is_palindrome(word):
    # 길이가 0 또는 1이면 회문이다
    if len(word) <= 1:
        return True
    # 앞뒤 문자가 다르면 회문이 아니다
    if word[0] != word[-1]:
        return False
    # 앞뒤를 제거하고 다시 검사
    return is_palindrome(word[1:-1])

# 프로그램 시작
def main():
    print("회문 검사기 (재귀 버전)")
    user_input = input("단어를 입력하세요: ").strip().lower()

    if is_palindrome(user_input):
        print("회문입니다!")
    else:
        print("회문이 아닙니다.")

main()
