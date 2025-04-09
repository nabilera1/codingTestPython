import os
import streamlit as st

# 현재 디렉토리의 모든 .db 파일 출력
db_files = [f for f in os.listdir() if f.endswith(".db")]

st.write("📂 현재 디렉토리의 데이터베이스 파일:")
for db in db_files:
    st.write("🔸", db)
