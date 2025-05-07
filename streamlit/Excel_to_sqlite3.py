import pandas as pd
import sqlite3
import streamlit as st



try:
    import openpyxl
except ImportError:
    st.error("⚠️ 'openpyxl'이 설치되어 있지 않습니다. 터미널에 'pip install openpyxl'을 입력해 설치해주세요.")


st.title("사용자 검색 앱")



# 1. 엑셀 파일에서 데이터 읽기
# df = pd.read_excel('users.xlsx')  # 또는 'uploaded_file.xlsx'

# 엑셀 파일 업로드
uploaded_file = st.file_uploader("엑셀 파일을 업로드하세요", type=["xlsx"])

if uploaded_file is not None:
    # 엑셀 파일을 DataFrame으로 읽기
    df = pd.read_excel(uploaded_file)

    # 2. SQLite 데이터베이스 연결
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # 3. 테이블 생성 (없으면 생성)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            username TEXT,
            password TEXT
        )
    ''')
    conn.commit()

    # 4. 엑셀의 각 행을 DB에 추가
    for _, row in df.iterrows():
        name = row['이름']
        username = row['ID']
        password = row['비밀번호']

        cursor.execute('INSERT INTO users (name, username, password) VALUES (?, ?, ?)',
                       (name, username, password))

    conn.commit()
    conn.close()
    st.success("엑셀 데이터를 DB에 성공적으로 입력했습니다!")

    # print("엑셀 데이터를 DB에 성공적으로 입력했습니다!")
