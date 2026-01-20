import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="나의 자기소개 페이지",
    page_icon="👋",
    layout="centered"
)

# 2. 헤더 섹션
st.title("안녕하세요! 👋 저는 [이름]입니다")
st.subheader("꿈을 코딩하는 개발자 | 여행과 커피를 좋아하는 사람")

# 3. 사진 및 소개 섹션
col1, col2 = st.columns([1, 2])

with col1:
    # 본인의 사진 파일 경로를 적어주세요 (예: 'profile.jpg')
    # 이미지 파일이 없다면 샘플 이미지를 사용합니다.
    st.image("https://via.placeholder.com/200", caption="나의 프로필 사진", use_container_width=True)

with col2:
    st.write("""
    ### 👨‍💻 About Me
    여기에 본인에 대한 소개글을 작성하세요. 
    간단한 경력이나 관심사, 혹은 현재 공부하고 있는 분야를 적으면 좋습니다.
    
    * **📍 위치:** 대한민국 서울
    * **📧 이메일:** example@email.com
    * **🛠 기술 스택:** Python, Streamlit, SQL
    """)

st.divider()

# 4. 상세 정보 (탭 활용)
tab1, tab2, tab3 = st.tabs(["경력", "프로젝트", "취미"])

with tab1:
    st.write("""
    - **A 대학교** 컴퓨터공학 전공 (2020 - 현재)
    - **B 스타트업** 인턴 근무 (2023.01 - 2023.06)
    """)

with tab2:
    st.write("### 🚀 주요 프로젝트")
    st.info("데이터 분석 웹 대시보드 제작")
    st.info("개인 포트폴리오 사이트 구축")

with tab3:
    st.write("저는 주말에 산책하는 것과 새로운 카페 탐방하는 것을 즐깁니다. ☕️")

# 5. 하단 연락처 정보
st.sidebar.header("Contact Me")
st.sidebar.text_input("메시지를 남겨주세요:")
if st.sidebar.button("전송"):
    st.sidebar.success("메시지가 전송되었습니다! (실제 기능은 추가 구현 필요)")
