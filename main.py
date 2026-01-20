import streamlit as st
st.title("정진경의 첫 웹앱")
st.write('안녕하세요! 반갑습니다 :)')
st.subheader("2026년 1월 20일 수요일")
st.text("오늘 하루는 어땠나요?")
import pandas as pd
from datetime import date
import os

# 1. 저장할 파일 이름 정의
DB_FILE = "diary_data.csv"

def load_data():
    """기존 일기 데이터를 불러오는 함수"""
    if os.path.exists(DB_FILE):
        return pd.read_csv(DB_FILE)
    else:
        # 파일이 없으면 빈 데이터프레임 생성
        return pd.DataFrame(columns=["날짜", "제목", "내용"])

def save_data(date, title, content):
    """새로운 일기를 저장하는 함수"""
    df = load_data()
    new_data = pd.DataFrame([[date, title, content]], columns=["날짜", "제목", "내용"])
    # 데이터 합치기
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(DB_FILE, index=False, encoding='utf-8-sig')

# --- UI 레이아웃 ---
st.title("📂 나만의 데이터 통합 앱")
st.header("✍️ 오늘의 일기")

# 입력 섹션
with st.expander("새 일기 쓰기", expanded=True):
    diary_date = st.date_input("날짜 선택", date.today())
    diary_title = st.text_input("제목", placeholder="오늘의 핵심 키워드")
    diary_content = st.text_area("내용", placeholder="오늘 하루는 어땠나요?", height=200)

    if st.button("일기 저장하기"):
        if diary_title and diary_content:
            save_data(diary_date, diary_title, diary_content)
            st.success(f"{diary_date} 일기가 성공적으로 저장되었습니다!")
            st.rerun() # 화면 새로고침하여 목록 업데이트
        else:
            st.warning("제목과 내용을 모두 입력해주세요.")

# 조회 섹션
st.divider()
st.subheader("📜 이전 기록 찾아보기")
data = load_data()

if not data.empty:
    # 최신순으로 정렬하여 표시
    st.dataframe(data.sort_values(by="날짜", ascending=False), use_container_width=True)
else:
    st.info("아직 작성된 일기가 없습니다. 첫 일기를 작성해보세요!")
