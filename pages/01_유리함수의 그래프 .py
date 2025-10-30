import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(layout="wide", page_title="유리함수 시각화: y = k/(x-p)+q")
st.title("유리함수 시각화: y = k / (x - p) + q")

# 세션 초기화
if "params" not in st.session_state:
    st.session_state.params = {"p":0, "q":0, "k":0}

# 새로운 함수 만들기 버튼
if st.button("새로운 함수 만들기"):
    st.session_state.params = {"p":0, "q":0, "k":0}

    # 고양이 아래->위 애니메이션
    cat_area = st.empty()
    for i in range(10,0,-1):
        cat_area.markdown("<p style='font-size:30px; text-align:center;'>" + "🐱 "*i + "</p>", unsafe_allow_html=True)
        time.sleep(0.1)
    cat_area.empty()  # 마지막에 비우기

# 입력칸 (직접 숫자 입력)
cols = st.columns(3)
p_str = cols[0].text_input("x축 이동 p", value=str(st.session_state.params["p"]))
q_str = cols[1].text_input("y축 이동 q", value=str(st.session_state.params["q"]))
k_str = cols[2].text_input("k 값", value=str(st.session_state.params["k"]))

# 입력값 숫자 변환
try:
    p = int(p_str)
except:
    p = 0
try:
    q = int(q_str)
except:
    q = 0
try:
    k = float(k_str)
except:
    k = 0

st.session_state.params.update({"p":p,"q":q,"k":k})

st.subheader(f"현재 함수: y = {k} / (x - {p}) + {q}")

# 정의역, 치역, 점근선
vertical_asymp = p
horizontal_asymp = q

st.markdown("### 함수 정보")
st.write(f"- 수직 점근선: x = {vertical_asymp}")
st.write(f"- 수평 점근선: y = {horizontal_asymp}")
st.write(f"- 정의역: 모든 실수 x ≠ {vertical_asymp}")
st.write(f"- 치역: 모든 실수 y ≠ {horizontal_asymp}" if k != 0 else f"- 치역: y = {horizontal_asymp} (상수 함수)")

# 그래프 그리기
x = np.linspace(p - 10, p + 10, 1000)
y = np.where(x != p, k / (x - p) + q, np.nan)

fig, ax = plt.subplots(figsize=(8,5))
ax.plot(x, y, label=f"y = {k}/(x-{p}) + {q}")
ax.axvline(x=vertical_asymp, color='r', linestyle='--', label='수직 점근선')
ax.axhline(y=horizontal_asymp, color='g', linestyle='--', label='수평 점근선')
ax.set_xlim(p - 10, p + 10)
ax.set_ylim(q - 10, q + 10)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("유리함수 그래프")
ax.legend()
st.pyplot(fig)
