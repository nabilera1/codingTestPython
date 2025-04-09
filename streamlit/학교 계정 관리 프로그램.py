import streamlit as st
import sqlite3
import pandas as pd


# DB 연결 및 테이블 생성
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            username TEXT,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()


# 사용자 추가
def add_user(name, username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, username, password) VALUES (?, ?, ?)', (name, username, password))
    conn.commit()
    conn.close()


# 사용자 검색
def search_user_by_name(name):
    conn = sqlite3.connect('users.db')
    df = pd.read_sql_query(f"SELECT * FROM users WHERE name = ?", conn, params=(name,))
    conn.close()
    return df


# 앱 실행
st.title("📦 사용자 DB 관리 앱")

# DB 초기화
init_db()

menu = st.sidebar.selectbox("메뉴를 선택하세요", ["사용자 등록", "사용자 검색"])

if menu == "사용자 등록":
    st.subheader("👤 사용자 등록")
    name = st.text_input("이름")
    username = st.text_input("ID")
    password = st.text_input("비밀번호", type="password")

    if st.button("등록하기"):
        if name and username and password:
            add_user(name, username, password)
            st.success("사용자가 등록되었습니다.")
        else:
            st.warning("모든 필드를 입력해주세요.")

elif menu == "사용자 검색":
    st.subheader("🔍 사용자 검색")
    search_name = st.text_input("검색할 이름 입력")

    if st.button("검색"):
        results = search_user_by_name(search_name)
        if not results.empty:
            st.dataframe(results[['name', 'username', 'password']])
        else:
            st.warning("일치하는 사용자가 없습니다.")
