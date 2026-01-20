import streamlit as st
st.title("정진경의 첫 웹앱")
st.write('안녕하세요! 반갑습니다 :)')
st.subheader("2026년 1월 20일 수요일")
st.text("오늘 하루는 어땠나요?")

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
st.markdown('<p class="title-text">✨ 미래의 꿈을 찾는 MBTI 탐험 ✨</p>', unsafe_allow_html: True)
st.write("<h4 style='text-align: center; color: white;'>나의 성격 유형을 선택하고 가장 잘 어울리는 직업을 알아보세요! 🚀</h4>", unsafe_content: True)

st.divider()

# 레이아웃 나누기
col1, col2 = st.columns([1, 1.5])

with col1:
    st.write("### 🔍 정보 입력")
    name = st.text_input("당신의 멋진 이름은?", placeholder="이름을 입력해주세요")
    mbti = st.selectbox(
        "당신의 MBTI 유형은 무엇인가요?",
        options=list(mbti_data.keys()),
        index=0
    )
    
    st.write("---")
    analyze_btn = st.button("🌟 결과 확인하기")

with col2:
    if analyze_btn:
        # 로딩 애니메이션
        with st.spinner('당신의 미래를 분석하고 있습니다...'):
            time.sleep(1.5)
            st.balloons() # 축하 풍선 효과!
        
        # 결과 표시
        data = mbti_data[mbti]
        
        st.markdown(f"""
        <div class="job-card">
            <h2>{name}님은 <b>{mbti}</b> 유형이군요! {data['emoji']}</h2>
            <hr style="border-left: 0; border-top: 1px solid #ccc;">
            <h3 style="color: #764ba2;">추천 직업: {data['job']}</h3>
            <p style="font-size: 1.2rem; line-height: 1.6;">{data['desc']}</p>
        </div>
        """, unsafe_content: True)
        
        # 추가 조언
        st.info(f"💡 {name}님, {mbti} 유형은 특히 **'{data['job'].split(',')[0]}'** 분야에서 빛을 발할 가능성이 높아요!")
    else:
        st.image("https://images.unsplash.com/photo-1481627834876-b7833e8f5570?auto=format&fit=crop&w=800&q=80", caption="당신의 미래는 밝습니다!")

# 5. 하단 푸터
st.markdown("<br><br><p style='text-align: center; color: #eee;'>© 2024 진로 교육 프로젝트 | 꿈을 향한 첫걸음 🏃‍♂️</p>", unsafe_content: True)
