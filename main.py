

import streamlit as st
import random

# 🍱 메뉴 리스트
menu_list = [
    "🍜 라면", "🍛 카레", "🍕 피자", "🍗 치킨", "🍔 햄버거",
    "🥘 부대찌개", "🍲 김치찌개", "🍱 도시락", "🥩 스테이크",
    "🍤 돈까스", "🍝 파스타", "🥟 만두", "🥪 샌드위치", "🥗 샐러드",
    "🍚 제육덮밥", "🍣 초밥", "🌮 타코", "🍙 삼각김밥", "🍜 우동",
    "🥬 비빔밥", "🍲 순두부찌개"
]

# 🌈 페이지 설정
st.set_page_config(page_title="오늘 뭐 먹지? 🍽️", page_icon="🍴", layout="centered")

# 🎨 타이틀
st.markdown("<h1 style='text-align:center; color:#FF6347;'>🤔 오늘 뭐 먹지? 🍽️</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color:#4682B4;'>버튼을 누르면 오늘의 점심/저녁을 추천해드려요! 🧡</h3>", unsafe_allow_html=True)
st.markdown("")

# 🎲 추천 버튼
if st.button("👉 메뉴 추천 받기!"):
    choice = random.choice(menu_list)
    st.markdown("---")
    st.markdown(f"<h2 style='text-align:center; font-size:50px;'>✨ 오늘의 추천 메뉴는...<br><span style='color:#FF1493'>{choice}</span> ✨</h2>", unsafe_allow_html=True)
    st.markdown("---")
else:
    st.markdown("<p style='text-align:center;'>😋 추천받고 싶은 메뉴가 있다면 버튼을 눌러보세요!</p>", unsafe_allow_html=True)

# 🐣 푸터
st.markdown("<div style='text-align:center; font-size:20px;'>Made with ❤️ by 당신의 AI 요리비서</div>", unsafe_allow_html=True)
