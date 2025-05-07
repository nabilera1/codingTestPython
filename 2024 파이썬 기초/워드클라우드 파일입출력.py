# Re-run after reset
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
# import string
#
# # 파일 경로
# file_path = "./data/alice_in_wonderland.txt"
#
# # 텍스트 파일 읽기
# with open(file_path, "r", encoding="utf-8") as file:
#     text = file.read()
#
# # 소문자로 변환 및 문장부호 제거
# text = text.lower()
# translator = str.maketrans('', '', string.punctuation)
# cleaned_text = text.translate(translator)
#
# # 단어 나누기
# words = cleaned_text.split()
#
# # 단어 빈도수 계산
# word_counts = {}
# for word in words:
#     word_counts[word] = word_counts.get(word, 0) + 1
#
# # 워드클라우드 생성
# wc = WordCloud(
#     background_color="white",
#     width=800,
#     height=600
# )
#
# font_path = "C:/Windows/Fonts/malgun.ttf"  # 또는 Arial.ttf
#
# wc.generate_from_frequencies(word_counts)
#
# # 워드클라우드 출력
# plt.figure(figsize=(12, 8))
# plt.imshow(wc, interpolation='bilinear')
# plt.axis("off")
# plt.title("Word Cloud - Alice in Wonderland", fontsize=16)
# plt.show()

# 코랩에서는 동작됨.

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import string
import os
import matplotlib.font_manager as fm
# 텍스트 파일 경로
file_path = "./data/alice_in_wonderland.txt"


# 텍스트 파일 읽기
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# 텍스트 전처리: 소문자로 변환하고 문장부호 제거
text = text.lower()
translator = str.maketrans('', '', string.punctuation)
cleaned_text = text.translate(translator)
words = cleaned_text.split()

# 단어 빈도수 계산
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

# 워드클라우드 폰트 설정: Arial (영문 TrueType 폰트, 시스템 기본 포함됨)
# Arial.ttf가 기본적으로 포함된 경로를 지정
# font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
# 윈도우용 폰트 경로 설정 (Arial 또는 Malgun Gothic)
# 한글이 포함되어 있다면 "malgun.ttf", 없으면 "arial.ttf"
# font_path = "C:/Windows/Fonts/arial.ttf"  # 또는 "malgun.ttf"

# 시스템에서 사용 가능한 TrueType 폰트 자동 검색
ttf_fonts = [f.fname for f in fm.fontManager.ttflist if os.path.exists(f.fname)]
font_path = next((f for f in ttf_fonts if "arial" in f.lower() or "dejavu" in f.lower()), None)


if not os.path.exists(font_path):
    font_path = None  # 폰트 없으면 기본값 사용 (단, 한글 미지원 가능성 있음)

# 워드클라우드 생성
wc = WordCloud(
    font_path=font_path,
    background_color="white",
    width=800,
    height=600
)
wc.generate_from_frequencies(word_counts)

# 워드클라우드 출력
plt.figure(figsize=(12, 8))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud - Alice in Wonderland", fontsize=16)
plt.show()
