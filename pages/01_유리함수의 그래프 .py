import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="유리함수 시각화", layout="centered")
st.title("💡 유리함수 시각화:  y = k / (x - p) + q")

# 세션 초기화
if "params" not in st.session_state:
    st.session_state.params = {"p": 0, "q": 0, "k": 1}

# "새로운 함수 만들기" 버튼
if st.button("새로운 함수 만들기 🐱"):
    st.session_state.params = {"p": 0, "q": 0, "k": 1}

    # 고양이 이모지 애니메이션 (아래→위)
    cat_area = st.empty()
    for i in range(1, 8):
        cat_area.markdown(
            f"<p style='font-size:30px; text-align:center; margin-top:{150 - i*20}px;'>🐱</p>",
            unsafe_allow_html=True,
        )
        time.sleep(0.1)
    cat_area.empty()

# 입력칸 (직접 숫자 입력)
cols = st.columns(3)
p_str = cols[0].text_input("x축 이동 (p)", value=str(st.session_state.params["p"]))
q_str = cols[1].text_input("y축 이동 (q)", value=str(st.session_state.params["q"]))
k_str = cols[2].text_input("k 값", value=str(st.session_state.params["k"]))

# 숫자 변환 (오류 방지)
def safe_float(s, default=0):
    try:
        return float(s)
    except ValueError:
        return default

p = safe_float(p_str, 0)
q = safe_float(q_str, 0)
k = safe_float(k_str, 1)

# 상태 업데이트
st.session_state.params.update({"p": p, "q": q, "k": k})

# 현재 함수식 출력
st.subheader(f"📘 현재 함수식:  y = {k} / (x - {p}) + {q}")

# 정의역, 치역, 점근선 계산
domain = f"x ∈ ℝ, 단 x ≠ {p}"
range_ = f"y ∈ ℝ, 단 y ≠ {q}"
vertical_asymptote = f"x = {p}"
horizontal_asymptote = f"y = {q}"

# 함수 정보 표시
st.markdown("### 📊 함수 정보")
st.write(f"- 수직 점근선: **{vertical_asymptote}**")
st.write(f"- 수평 점근선: **{horizontal_asymptote}**")
st.write(f"- 정의역: **{domain}**")
st.write(f"- 치역: **{range_}**")

# 그래프 그리기
x = np.linspace(p - 10, p + 10, 1000)
y = np.where(x != p, k / (x - p) + q, np.nan)

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, y, label=f"y = {k}/(x - {p}) + {q}", linewidth=2)

# 점근선 표시
ax.axvline(x=p, color='red', linestyle='--', label=f"x = {p}")
ax.axhline(y=q, color='green', linestyle='--', label=f"y = {q}")

# 축 설정
ax.set_xlim(p - 10, p + 10)
ax.set_ylim(q - 10, q + 10)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("유리함수 그래프")
ax.legend()
ax.grid(True, linestyle="--", alpha=0.6)

st.pyplot(fig)
