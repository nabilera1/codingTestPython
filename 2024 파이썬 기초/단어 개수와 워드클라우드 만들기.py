from wordcloud import WordCloud
import matplotlib.pyplot as plt
import string
import matplotlib.font_manager as fm

def count_words_and_generate_wordcloud():
    print("문장을 입력하세요. (빈 줄을 입력하면 종료됩니다.)")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)

    # 모든 입력된 문장을 하나로 합치고 소문자로 변환
    text = ' '.join(lines).lower()

    # 문장부호 제거
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator)

    # 단어 나누기
    words = cleaned_text.split()

    # 단어 빈도수 계산
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    # 워드클라우드 폰트 설정 (한글 깨짐 방지)
    # 윈도우: 'malgun.ttf', 맥: 'AppleGothic', 리눅스: 'NanumGothic'
    font_path = fm.findfont(fm.FontProperties(family='Malgun Gothic'))

    # 워드클라우드 객체 생성
    wc = WordCloud(
        font_path=font_path,  # 한글 폰트 경로
        background_color='white',  # 배경색
        width=800,
        height=600
    )

    # 단어 빈도수를 기반으로 워드클라우드 생성
    wc.generate_from_frequencies(word_counts)

    # 이미지 출력
    plt.figure(figsize=(10, 8))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')  # 축 제거
    plt.title("워드클라우드")
    plt.show()

count_words_and_generate_wordcloud()
