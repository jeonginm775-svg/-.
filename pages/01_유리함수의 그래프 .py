import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="유리함수 시각화", layout="centered")
st.title("🐱 유리함수 시각화:  y = k / (x - p) + q")

# 초기 세션값(입력칸 키를 사용)
if "initialized" not in st.session_state:
    st.session_state["p_input"] = "0"
    st.session_state["q_input"] = "0"
    st.session_state["k_input"] = "0"
    st.session_state["initialized"] = True

# "새로운 함수 만들기" 버튼: 입력칸(키 값)을 직접 0으로 세팅
if st.button("새로운 함수 만들기 🐱"):
    st.session_state["p_input"] = "0"
    st.session_state["q_input"] = "0"
    st.session_state["k_input"] = "0"

    # 고양이 여러 마리 애니메이션 (차례대로 올라갔다 사라짐)
    cat_area = st.empty()
    for i in range(1, 6):
        cats = "🐱 " * i
        cat_area.markdown(
            f"<p style='font-size:34px; text-align:center; margin-top:{150 - i*22}px;'>{cats}</p>",
            unsafe_allow_html=True,
        )
        time.sleep(0.14)
    time.sleep(0.2)
    cat_area.empty()

# 입력칸 (직접 정수 입력) — 값을 세션 키에서 바로 읽고 씀
cols = st.columns(3)
p_str = cols[0].text_input("x축 이동 (p)", value=st.session_state["p_input"], key="p_input")
q_str = cols[1].text_input("y축 이동 (q)", value=st.session_state["q_input"], key="q_input")
k_str = cols[2].text_input("k 값", value=st.session_state["k_input"], key="k_input")

# 정수 변환 (유효하지 않으면 0)
def safe_int_from_str(s, default=0):
    try:
        # float->int 허용 (예: "3.0" -> 3), 하지만 소수는 잘라서 정수 취급
        return int(float(s))
    except Exception:
        return default

p = safe_int_from_str(p_str, 0)
q = safe_int_from_str(q_str, 0)
k = safe_int_from_str(k_str, 0)

# 현재 함수식 표시 (정수 표현)
st.subheader(f"📘 현재 함수식:  y = {k} / (x - {p}) + {q}")

# 점근선, 정의역, 치역 정보 (정수로 보이게)
vertical_asymptote = f"x = {p}"
horizontal_asymptote = f"y = {q}"
domain = f"x ∈ ℤ? (실수 전체이지만 x ≠ {p}) → x ∈ ℝ \\ {{ {p} }}"
range_ = f"y ∈ ℝ \\ {{ {q} }}" if k != 0 else f"y = {q} (상수 함수)"

st.markdown("### 📊 함수 정보")
st.write(f"- 수직 점근선: **{vertical_asymptote}**")
st.write(f"- 수평 점근선: **{horizontal_asymptote}**")
st.write(f"- 정의역: **{domain}**")
st.write(f"- 치역: **{range_}**")

# 그래프 데이터 생성 (x가 p 근처에서 너무 촘촘하면 NaN 처리)
span = 10  # 좌우 범위
x = np.linspace(p - span, p + span, 2000)
y = np.where(np.isclose(x, p), np.nan, k / (x - p) + q)

# 플롯
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, y, label=f"y = {k}/(x-{p}) + {q}", linewidth=2)

# 점근선 표시
ax.axvline(x=p, color='red', linestyle='--', linewidth=1)
ax.axhline(y=q, color='green', linestyle='--', linewidth=1)

# 점근선 숫자(정수)로 명확히 표시: 그래프 내에 텍스트
# 텍스트 위치는 그래프 범위에 맞춰 정수 위치에 배치
text_x_pos = p + max(0.3, span * 0.03)
text_y_pos = q + max(0.5, span * 0.1)
ax.text(text_x_pos, text_y_pos + span*0.1, f"x = {p}", color='red', fontsize=11, backgroundcolor="white")
ax.text(p - span*0.7, q + 0.3, f"y = {q}", color='green', fontsize=11, backgroundcolor="white")

# 축 범위 및 정수 눈금 설정
ax.set_xlim(p - span, p + span)
ax.set_ylim(q - span, q + span)

# xticks, yticks를 정수로 생성
# 범위가 클 경우 눈금이 너무 많아지니 적절히 간격을 두어 표시
def make_integer_ticks(center, span, max_ticks=21):
    start = int(np.floor(center - span))
    end = int(np.ceil(center + span))
    length = end - start + 1
    step = 1
    if length > max_ticks:
        # 일정 간격으로 줄이기
        step = int(np.ceil(length / max_ticks))
    return np.arange(start, end + 1, step)

ax.set_xticks(make_integer_ticks(p, span))
ax.set_yticks(make_integer_ticks(q, span))

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("유리함수 그래프 (정수 눈금)")
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend()

st.pyplot(fig)
