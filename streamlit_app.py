import streamlit as st
import random

st.title("🍽️ 점심 메뉴 선택")

st.write("오늘의 점심 메뉴를 선택해주세요!")

# session state 초기화
if "menu_list" not in st.session_state:
    st.session_state.menu_list = [
        "🇰🇷 한식",
        "🇨🇳 중식",
        "🇮🇹 양식",
        "🇯🇵 일식",
        "🇲🇽 멕시칸",
        "🇹🇭 태국식",
        "🇮🇳 인도식",
    ]

st.markdown("---")

st.subheader("🎰 오늘의 메뉴")

if st.button("🎲 무작위로 메뉴 뽑기", use_container_width=True):
    selected_menu = random.choice(st.session_state.menu_list)
    st.success(f"✨ 오늘의 메뉴: {selected_menu}")
    st.balloons()
