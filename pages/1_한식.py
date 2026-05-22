import streamlit as st
import random

st.title("🇰🇷 한식 메뉴")

st.write("오늘의 한식 메뉴를 선택해주세요!")

# 한식 메뉴 리스트
korean_menus = [
    "🍜 국수",
    "🍲 찌개",
    "🥘 국",
    "🍖 갈비",
    "🍗 치킨",
    "🍱 도시락",
    "🥗 비빔밥",
    "🍢 주먹밥",
    "🥟 만두",
    "🍕 김밥",
    "🍝 국수",
    "🥩 불고기",
    "🥢 샤브샤브",
    "🍲 전골",
    "🌶️ 떡볶이",
    "🧆 순대",
    "🥙 김말이",
    "🍗 곱창",
]

st.markdown("---")

st.subheader("🎰 한식 메뉴 뽑기")

if st.button("🎲 무작위로 한식 메뉴 뽑기", use_container_width=True):
    selected_menu = random.choice(korean_menus)
    st.success(f"✨ 오늘의 한식 메뉴: {selected_menu}")
    st.balloons()

st.markdown("---")

st.subheader("📋 한식 메뉴 목록")
col1, col2, col3 = st.columns(3)

for i, menu in enumerate(korean_menus):
    if i % 3 == 0:
        with col1:
            st.write(f"• {menu}")
    elif i % 3 == 1:
        with col2:
            st.write(f"• {menu}")
    else:
        with col3:
            st.write(f"• {menu}")
