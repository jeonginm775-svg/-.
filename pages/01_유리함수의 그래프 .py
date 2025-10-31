import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time
import random

st.set_page_config(page_title="유리함수 시각화", layout="centered")
st.title("🐱 유리함수 시각화:  y = k / (x - p) + q")

# 세션 초기화
if "params" not in st.session_state:
    st.session_state.params = {"p": 0, "q": 0, "k": 1}

# 새로운 함수 만들기 버튼
if st.button("새로운 함수 만들기 🐱"):
    st.session_state.params = {"p": 0, "q": 0, "k": 1}

    # 고양이 여러 마리가 차례대로 올라오는 애니메이션
    cat_area = st.empty()
    for i in range(5):
        cats = "🐱 " * (i + 1)
        cat_area.markdown(
            f"<p style='font-size:30px; text-align:center; margin-top:{150 - i*25}px;'>{cats}</p>",
            unsafe_allow_html=True,
        )
        time.sleep(0.15)
    time.sleep(0.4)
    cat_area.empty()

# 입력칸 (직접 정수 입력)
cols = st.columns(3)
p_str = cols[0].text_input("x축 이동 (p)", value=str(int(st.session_state.params["p"])))
q_str = cols[1].text_input("y축 이동 (q)", value=str(int(st.session_state.params["q"])))
k_str = cols[2].text_input("k 값", value=str(int(st.session_state.params["k"])))

# 정수 변환 (유효하지 않으면 0)
def safe_int(s, default=0):
    try:
        return int(float(s))
    except ValueError:
        return default

p = safe_int(p_str, 0)
q = safe_int(q_str, 0)
k = safe_int(k_str, 1)

# 세션 업데이트
st.session_state.params.update({"p": p, "q": q, "k": k})

# 현재 함수식 표시
st.subheader(f"📘 현재 함수식:  y = {k} / (x - {p}) + {q}")

# 함수 정보
vertical_asymptote = f"x = {p}"
horizontal_asymptote = f"y = {q}"
domain = f"x ∈ ℝ, 단 x ≠ {p}"
range_ = f"y ∈ ℝ, 단 y ≠ {q}"

st.markdown("### 📊 함수 정보")
st.write(f"- 수직 점근선: **{vertical_asymptote}**")
st.write(f"- 수평 점근선: **{horizontal_asymptote}**")
st.write(f"- 정의역: **{domain}**")
st.write(f"- 치역: **{range_}**")

# 그래프 설정
x = np.linspace(p - 10, p + 10, 1000)
y = np.where(x != p, k / (x - p) + q, np.nan)

fig, ax = plt.subplots(figsize=(8, 6))

# 그래프
ax.plot(x, y, label=f"y = {k}/(x-{p}) + {q}", linewidth=2)

# 점근선 표시
ax.axvline(x=p, color='red', linestyle='--', linewidth=1)
ax.axhline(y=q, color='green', linestyle='--', linewidth=1)

# 점근선 텍스트 표시
ax.text(p + 0.3, q + 4, f"x = {p}", color='red', fontsize=10)
ax.text(p - 8, q + 0.5, f"y = {q}", color='green', fontsize=10)

# 축 범위
ax.set_xlim(p - 10, p + 10)
ax.set_ylim(q - 10, q + 10)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("유리함수 그래프")
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend()

st.pyplot(fig)
