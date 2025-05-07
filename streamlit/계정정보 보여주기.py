import streamlit as st
import pandas as pd


try:
    import openpyxl
except ImportError:
    st.error("⚠️ 'openpyxl'이 설치되어 있지 않습니다. 터미널에 'pip install openpyxl'을 입력해 설치해주세요.")


st.title("사용자 검색 앱")

# 엑셀 파일 업로드
uploaded_file = st.file_uploader("엑셀 파일을 업로드하세요", type=["xlsx"])

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file)

        if '이름' in df.columns and 'ID' in df.columns and '비밀번호' in df.columns:
            # 이름 입력
            name = st.text_input("이름을 입력하세요")

            # 검색
            if name:
                result = df[df['이름'] == name]
                if not result.empty:
                    st.success("검색 결과:")
                    st.write("ID:", result.iloc[0]['ID'])
                    st.write("비밀번호:", result.iloc[0]['비밀번호'])
                else:
                    st.warning("해당 이름을 찾을 수 없습니다.")
        else:
            st.error("엑셀 파일에 '이름', 'ID', '비밀번호' 컬럼이 있어야 합니다.")
    except Exception as e:
        st.error(f"파일을 읽는 중 오류가 발생했습니다: {e}")
