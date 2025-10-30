import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random
import time

st.set_page_config(layout="wide", page_title="유리함수 시각화: y = k/(x-p) + q")

st.title("유리함수 시각화: y = k / (x - p) + q")

# 세션 상태 초기화
if "params" not in st.session_state:
    st.session_state.params = {"p":0, "q":0, "k":1}

# 입력: p, q, k
cols = st.columns(3)
p = cols[0].number_input("x축 이동 p", value=st.session_state.params["p"], step=1)
q = cols[1].number_input("y축 이동 q", value=st.session_state.params["q"], step=1)
k = cols[2].number_input("k 값", value=st.session_state.params["k"], step=1)

# 세션 상태 저장
st.session_state.params.update({"p":p,"q":q,"k":k})

# 새로운 함수 만들기 버튼
if st.button("새로운 함수 만들기"):
    # 랜덤 값 생성
    st.session_state.params["p"] = random.randint(-5,5)
    st.session_state.params["q"] = random.randint(-5,5)
    st.session_state.params["k"] = random.randint(1,10)  # k=0은 의미 없음
    p = st.session_state.params["p"]
    q = st.session_state.params["q"]
    k = st.session_state.params["k"]

    # 풍선 효과
    st.markdown("### 🎈 풍선 올라가는 효과 🎈")
    for i in range(5):
        st.markdown(" ".join(["🎈"] * 10))
        time.sleep(0.1)

st.subheader(f"현재 함수: y = {k} / (x - {p}) + {q}")

# 정의역, 치역, 점근선 계산
vertical_asymp = p
horizontal_asymp = q

st.markdown("### 함수 정보")
st.write(f"- 수직 점근선: x = {vertical_asymp}")
st.write(f"- 수평 점근선: y = {horizontal_asymp}")
st.write(f"- 정의역: 모든 실수 x ≠ {vertical_asymp}")
if k != 0:
    st.write(f"- 치역: 모든 실수 y ≠ {horizontal_asymp}")
else:
    st.write(f"- 치역: y = {horizontal_asymp} (상수 함수)")

# 그래프 그리기
x = np.linspace(p - 10, p + 10, 1000)
y = k / (x - p) + q

fig, ax = plt.subplots(figsize=(8,5))
ax.plot(x, y, label=f"y = {k}/(x-{p}) + {q}")

# 점근선
ax.axvline(x=vertical_asymp, color='r', linestyle='--', label='수직 점근선')
ax.axhline(y=horizontal_asymp, color='g', linestyle='--', label='수평 점근선')

ax.set_xlim(p - 10, p + 10)
ax.set_ylim(q - 10, q + 10)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("유리함수 그래프")
ax.legend()
st.pyplot(fig)
