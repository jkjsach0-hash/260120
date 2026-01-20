import streamlit as st
st.title("정진경의 첫 웹앱")
st.write('안녕하세요! 반갑습니다 :)')
st.subheader("2026년 1월 20일 수요일")
st.text("오늘 하루는 어땠나요?")

import streamlit as st
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

import streamlit as st
import time

# 1. 페이지 설정 (아이콘, 레이아웃)
st.set_page_config(
    page_title="나의 꿈 찾기 탐험대 🚀",
    page_icon="✨",
    layout="wide"
)

# 2. 커스텀 CSS (화려한 배경 및 스타일링)
st.markdown("""
    <style>
    /* 전체 배경 그라데이션 */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    /* 제목 스타일 */
    .title-text {
        font-size: 50px !important;
        font-weight: 800;
        text-align: center;
        color: #ffffff;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        padding-bottom: 20px;
    }

    /* 결과 카드 스타일 */
    .job-card {
        background-color: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 25px;
        color: #333;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        margin: 10px 0;
        border-left: 10px solid #764ba2;
    }
    
    /* 구분선 스타일 */
    hr {
        border: 0;
        height: 2px;
        background: linear-gradient(to right, rgba(255,255,255,0), rgba(255,255,255,0.75), rgba(255,255,255,0));
        margin: 30px 0;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 데이터 정의 (16가지 MBTI별 직업 추천)
mbti_data = {
    "INTJ": {"job": "전략 기획가, 과학자, 소프트웨어 설계자", "emoji": "🧠", "desc": "독립적이고 분석적인 사고로 복잡한 문제를 해결해요!"},
    "INTP": {"job": "연구원, 수학자, 프로그래머", "emoji": "💡", "desc": "논리적이고 호기심이 많아 새로운 아이디어를 탐구하는 걸 즐겨요."},
    "ENTJ": {"job": "CEO, 정치인, 경영 컨설턴트", "emoji": "👑", "desc": "결단력 있고 통솔력이 뛰어나 목표를 향해 조직을 이끌어요."},
    "ENTP": {"job": "발명가, 변호사, 마케팅 디렉터", "emoji": "🎤", "desc": "창의적이고 재치 넘치는 논쟁가로 새로운 도전을 두려워하지 않아요."},
    "INFJ": {"job": "작가, 상담가, 심리학자", "emoji": "🔮", "desc": "사람들의 마음을 깊게 통찰하고 세상을 더 나은 곳으로 만들고 싶어 해요."},
    "INFP": {"job": "예술가, 소설가, 사회활동가", "emoji": "🦄", "desc": "풍부한 상상력과 따뜻한 마음으로 나만의 가치를 실현해요."},
    "ENFJ": {"job": "교사, 외교관, 시민단체 리더", "emoji": "🤝", "desc": "사람들을 격려하고 이끄는 따뜻한 카리스마의 소유자예요."},
    "ENFP": {"job": "연예인, 홍보 전문가, 이벤트 기획자", "emoji": "🌟", "desc": "에너지 넘치고 창의적이며 주변 사람들에게 기쁨을 줘요."},
    "ISTJ": {"job": "회계사, 공무원, 군인/경찰", "emoji": "📊", "desc": "책임감이 강하고 실용적이며 매사를 철저하게 관리해요."},
    "ISFJ": {"job": "간호사, 유치원 교사, 비서", "emoji": "🏠", "desc": "차분하고 다정하며 소중한 사람들을 뒤에서 묵묵히 도와줘요."},
    "ESTJ": {"job": "프로젝트 매니저, 판사, 은행원", "emoji": "🏢", "desc": "현실적이고 구체적이며 목표를 효율적으로 달성하는 능력이 탁월해요."},
    "ESFJ": {"job": "승무원, 호텔리어, 사회복지사", "emoji": "💕", "desc": "친절하고 협조적이며 타인을 돕는 일에서 보람을 느껴요."},
    "ISTP": {"job": "엔지니어, 카레이서, 조종사", "emoji": "🛠️", "desc": "관찰력이 뛰어나고 상황에 유연하게 대응하며 도구 활용 능력이 좋아요."},
    "ISFP": {"job": "디자이너, 화가, 음악가", "emoji": "🎨", "desc": "온화하고 예술적 감각이 뛰어나며 현재의 즐거움을 소중히 여겨요."},
    "ESTP": {"job": "운동선수, 소방관, 사업가", "emoji": "⚡", "desc": "활동적이고 순발력이 좋아 스릴 넘치는 현장을 즐겨요."},
    "ESFP": {"job": "배우, 투어 가이드, 마케터", "emoji": "🎈", "desc": "낙천적이며 사교성이 좋아 어디서든 주인공이 되는 분위기 메이커예요."}
}

# 4. 메인 화면 구성
st.markdown('<p class="title-text">✨ 미래의 꿈을 찾는 MBTI 탐험 ✨</p>', unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: white;'>나의 성격 유형을 선택하고 가장 잘 어울리는 직업을 알아보세요! 🚀</h4>", unsafe_allow_html=True)

st.divider()
st.divider()

# 1. 레이아웃 나누기 (이 줄의 맨 앞에는 공백이 없어야 합니다)
col1, col2 = st.columns([1, 1.5])

with col1:
    st.markdown("### 🔍 정보 입력")
    name = st.text_input("당신의 멋진 이름은?", placeholder="예: 홍길동")
    mbti = st.selectbox(
        "당신의 MBTI 유형은?",
        options=list(mbti_data.keys()),
        index=0
    )
    
    st.write("")
    analyze_btn = st.button("🌟 직업 추천받기", use_container_width=True)

with col2:
    if analyze_btn:
        with st.spinner('당신의 성향을 분석 중입니다...'):
            time.sleep(1)
            st.balloons()
        
        data = mbti_data[mbti]
        
        # 결과 카드 출력
        st.markdown(f"""
        <div class="job-card">
            <h2 style="margin-top:0;">{name if name else "탐험가"}님의 결과는? {data['emoji']}</h2>
            <h3 style="color: #764ba2;">추천 직업: {data['job']}</h3>
            <hr style="border: 0; border-top: 1px solid #eee; margin: 20px 0;">
            <p style="font-size: 1.1rem; color: #555; line-height: 1.6;">{data['desc']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # 추가 조언
        st.info(f"💡 {name if name else '탐험가'}님, {mbti} 유형은 특히 **'{data['job'].split(',')[0]}'** 분야에서 빛을 발할 가능성이 높아요!")
        
    else:
        # 버튼을 누르기 전 초기 상태
        st.info("왼쪽에서 정보를 입력하고 버튼을 눌러보세요! ✨")

# 5. 하단 푸터 (이 줄도 맨 앞 벽에 딱 붙어야 합니다)
st.markdown("<br><br><p style='text-align: center; color: #ddd; font-size: 0.8rem;'>© 2026 MBTI Career Discovery | Dream Big! 🚀</p>", unsafe_allow_html=True)
