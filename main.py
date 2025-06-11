import streamlit as st

# 📌 페이지 설정
st.set_page_config(
    page_title="MBTI 직업 추천 💼",
    page_icon="🧠",
    layout="centered"
)

# 🎨 CSS 스타일
st.markdown("""
    <style>
    .title {
        font-size:40px;
        font-weight:bold;
        color: #FF69B4;
        text-align: center;
    }
    .subtitle {
        font-size:22px;
        text-align: center;
        color: #6A5ACD;
    }
    .emoji-box {
        font-size: 30px;
        text-align: center;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 🎉 타이틀
st.markdown('<div class="title">🔮 MBTI로 알아보는 나의 직업 💼</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">너의 성격유형에 딱 맞는 직업을 추천해줄게! ✨</div>', unsafe_allow_html=True)
st.markdown("")

# 🌟 MBTI 리스트
mbti_types = [
    'INTJ', 'INTP', 'ENTJ', 'ENTP',
    'INFJ', 'INFP', 'ENFJ', 'ENFP',
    'ISTJ', 'ISFJ', 'ESTJ', 'ESFJ',
    'ISTP', 'ISFP', 'ESTP', 'ESFP'
]

mbti = st.selectbox("📌 MBTI를 선택해주세요:", mbti_types)

# 🔍 MBTI별 직업 추천 딕셔너리
mbti_jobs = {
    'INTJ': ["🔬 과학자", "🧠 전략 컨설턴트", "📊 데이터 사이언티스트"],
    'INTP': ["🧪 연구원", "💻 소프트웨어 개발자", "🎨 UX 디자이너"],
    'ENTJ': ["📈 CEO", "🏛️ 변호사", "💼 프로젝트 매니저"],
    'ENTP': ["🎙️ 방송인", "🚀 창업가", "🧑‍💻 스타트업 개발자"],
    'INFJ': ["🎨 예술가", "🧘 심리상담사", "📚 작가"],
    'INFP': ["📖 시인", "🎬 영화감독", "🧑‍🏫 교육자"],
    'ENFJ': ["💬 커뮤니케이터", "👩‍🏫 교사", "🌏 NGO 활동가"],
    'ENFP': ["🎤 유튜버", "🎭 배우", "🎨 크리에이터"],
    'ISTJ': ["🧮 회계사", "⚖️ 법무사", "🏛️ 공무원"],
    'ISFJ': ["🏥 간호사", "👩‍🏫 교사", "👮 경찰관"],
    'ESTJ': ["🧑‍✈️ 관리자", "🏗️ 엔지니어", "💵 은행원"],
    'ESFJ': ["👩‍⚕️ 간호사", "🏠 사회복지사", "🎓 진로상담사"],
    'ISTP': ["🔧 정비사", "🚓 경찰", "🧱 기술자"],
    'ISFP': ["🎼 작곡가", "🖌️ 디자이너", "📸 사진작가"],
    'ESTP': ["🏎️ 레이서", "🧗 스포츠선수", "🎲 사업가"],
    'ESFP': ["🎤 가수", "📷 인플루언서", "🎉 이벤트 플래너"],
}

# 🎁 결과 출력
if mbti:
    st.markdown("---")
    st.markdown(f"### 🎯 `{mbti}` 유형에게 어울리는 직업 추천 💖")
    
    for job in mbti_jobs.get(mbti, []):
        st.markdown(f"- {job}")

    st.markdown("💡 자신에게 맞는 진로를 탐색해보세요! 미래는 당신의 것! 🚀")

# ⬇️ 푸터
st.markdown("---")
st.markdown("<div class='emoji-box'>🌟 함께 꿈을 찾아 떠나는 진로 여행 🌈</div>", unsafe_allow_html=True)
