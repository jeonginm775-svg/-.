# app.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction
import random

st.set_page_config(layout="wide", page_title="유리함수 시각화기")

st.title("유리함수 시각화기 — (ax + b) / (cx + d) (일차/일차)")
st.write("슬라이더로 계수와 이동을 바꿔보세요. `새로운 함수 만들기` 버튼은 랜덤 정수로 함수 생성하고 꽃 이모지 폭죽을 표시합니다.")

# -- 세션 상태 초기화 --
if "params" not in st.session_state:
    st.session_state.params = {"a":1,"b":0,"c":1,"d":0,"h":0,"k":0,"xlim":10}

def randomize_params():
    # c,d 선택 시 c==0 허용하지만 분모가 0으로 전부 상수 되지 않게 d != 0 or c != 0 보장
    while True:
        a = random.randint(-5,5)
        b = random.randint(-10,10)
        c = random.randint(-5,5)
        d = random.randint(-10,10)
        # 불허: a=b=c=d=0 (쓸모없음), 또는 (c==0 and d==0) -> 분모 0 전체 (불가)
        if not (a==b==c==d==0) and not (c==0 and d==0):
            break
    h = random.randint(-5,5)
    k = random.randint(-5,5)
    xlim = random.randint(5,15)
    st.session_state.params = {"a":a,"b":b,"c":c,"d":d,"h":h,"k":k,"xlim":xlim}
    # 꽃 이모지 플래그
    st.session_state.show_flowers = True

# 좌측: 컨트롤
with st.sidebar:
    st.header("함수 계수 (정수)")
    p = st.session_state.params
    cols = st.columns(2)
    a = cols[0].slider("a (분자 계수)", -10, 10, value=p["a"], step=1)
    b = cols[1].slider("b (분자 상수)", -20, 20, value=p["b"], step=1)
    c = cols[0].slider("c (분모 계수)", -10, 10, value=p["c"], step=1)
    d = cols[1].slider("d (분모 상수)", -20, 20, value=p["d"], step=1)

    st.markdown("---")
    st.header("이동 (정수)")
    cols2 = st.columns(2)
    h = cols2[0].slider("x-이동 (한 칸 = 1)", -10, 10, value=p["h"], step=1)  # replace x by (x - h)
    k = cols2[1].slider("y-이동 (한 칸 = 1)", -10, 10, value=p["k"], step=1)

    st.markdown("---")
    st.header("그래프 범위")
    xlim = st.slider("x 절반 범위 (플롯은 [-xlim, xlim])", 5, 30, value=p["xlim"], step=1)

    st.markdown("---")
    if st.button("새로운 함수 만들기"):
        randomize_params()

    # 저장: 세션에 반영
    st.session_state.params.update({"a":a,"b":b,"c":c,"d":d,"h":h,"k":k,"xlim":xlim})

# 꽃 이모지 폭죽 처리 (새 함수 눌렀을 때만 짧게 보여주기)
if st.session_state.get("show_flowers", False):
    # 여러 줄에 걸쳐 꽃 이모지 흩뿌리기
    for i in range(5):
        st.markdown(" ".join(["🌸"] * 20))
    # 한 번만 보이게 클리어
    st.session_state.show_flowers = False

# 메인 영역: 그래프와 정보
params = st.session_state.params
a, b, c, d, h, k, xlim = params["a"], params["b"], params["c"], params["d"], params["h"], params["k"], params["xlim"]

st.subheader(f"현재 함수: f(x) = ( {a}·(x - {h}) + {b} ) / ( {c}·(x - {h}) + {d} ) + {k}")
st.write("이는 원래 형태 (ax + b) / (cx + d)에 **x → x - h**, 전체에 **+ k** 를 적용한 것입니다.")

# 수학적 성질 계산
def frac_str(n, d):
    try:
        f = Fraction(n, d)
        if f.denominator == 1:
            return f"{f.numerator}"
        else:
            return f"{f.numerator}/{f.denominator}"
    except Exception:
        return str(n)

vertical_asymp = None
horizontal_asymp = None
notes = []

# vertical asymptote: solve c*(x - h) + d = 0 -> x = h - d/c (if c != 0)
if c != 0:
    x_va = Fraction(h) - Fraction(d, c)
    vertical_asymp = float(x_va)
    vertical_asymp_str = f"x = {frac_str(x_va.numerator, x_va.denominator)}"
else:
    vertical_asymp_str = "없음 (c = 0 → 분모가 상수, 수직 점근선 없음)"

# horizontal asymptote: limit x→∞ (a/c) + k when c != 0 (degree 같)
if c != 0:
    if c != 0:
        horiz = Fraction(a, c) + Fraction(k)
        horizontal_asymp = float(horiz)
        horizontal_asymp_str = f"y = {frac_str(horiz.numerator, horiz.denominator)}"
else:
    # c == 0 -> 함수는 실수선형 (일차 함수) -> 수평 점근선 없음 (일반적으로)
    horizontal_asymp_str = "없음 (c = 0 → 분모 상수 → 전체가 일차/상수 함수)"

# 정의역(도메인)과 치역(레인지) 일반 설명
domain_text = ""
range_text = ""
if c != 0:
    domain_text = f"정의역: 실수 전체 \u2212 {{{vertical_asymp_str}}} (즉 x ≠ {vertical_asymp_str.split('=')[1].strip()})"
    # Range: 일반적 성질은 모든 실수에서 수평아심프타트 제외 (단, 특수한 경우 존재가능)
    range_text = f"치역: 실수 전체 \u2212 {{{horizontal_asymp_str}}} (대부분의 경우). 특수케이스(예: 분자가 수평선과 같은 형태로 맞물리면 다를 수 있음)."
else:
    # c == 0 -> 분모 상수 d, 함수는 선형(혹은 상수)
    if d == 0:
        domain_text = "정의역: 분모가 0이므로 유효하지 않은 함수 (c=0, d=0). 계수를 바꿔주세요."
        range_text = "치역: 정의되지 않음"
    else:
        domain_text = "정의역: 모든 실수 (분모가 상수이므로 0이 되지 않음)"
        # 선형 함수면 치역도 모든 실수 (기울기 != 0) 혹은 상수이면 한 값
        slope = a / d
        const = (a * (-h) + b) / d + k  # value at x=0? but better to check slope zero
        if slope == 0:
            range_text = f"치역: 한 값(상수 함수). y = {(a * (-h) + b) / d + k:.6g}"
        else:
            range_text = "치역: 모든 실수"

# 출력 정보
st.markdown("### 성질 요약")
st.write(f"- 수직 점근선 (vertical asymptote): **{vertical_asymp_str}**")
st.write(f"- 수평 점근선 (horizontal asymptote): **{horizontal_asymp_str}**")
st.write(f"- {domain_text}")
st.write(f"- {range_text}")

# 그리기
st.markdown("### 그래프")
fig, ax = plt.subplots(figsize=(8,5))

# x sampling: avoid evaluating exactly at vertical asymptote
xs = np.linspace(-xlim, xlim, 2000)
ys = np.full_like(xs, np.nan, dtype=float)

# compute y safely
for i, x in enumerate(xs):
    denom = c * (x - h) + d
    if denom == 0:
        ys[i] = np.nan
    else:
        ys[i] = (a * (x - h) + b) / denom + k

# plot curve (matplotlib recommended)
ax.plot(xs, ys)

# plot vertical asymptote(s)
if c != 0:
    ax.axvline(x=vertical_asymp, linestyle="--")
# plot horizontal asymptote
if c != 0:
    ax.axhline(y=horizontal_asymp, linestyle="--")

# aesthetics
ax.set_xlim(-xlim, xlim)
# y-limits auto; but avoid extremely large spikes: clip for display
finite_ys = ys[np.isfinite(ys)]
if finite_ys.size > 0:
    y_mean = np.nanmean(finite_ys)
    y_std = np.nanstd(finite_ys)
    # set reasonable ylim around typical values but allow extremes if small
    ax.set_ylim(y_mean - max(5, 3*y_std), y_mean + max(5, 3*y_std))

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title(f"f(x) = ( {a}·(x - {h}) + {b} ) / ( {c}·(x - {h}) + {d} ) + {k}")

st.pyplot(fig)

# 추가: 함수 표본값 표
st.markdown("### 샘플 값 (x → f(x))")
sample_xs = list(range(-5,6))
vals = []
for x in sample_xs:
    denom = c * (x - h) + d
    if denom == 0:
        vals.append("정의되지 않음")
    else:
        vals.append(f"{(a*(x - h) + b)/denom + k:.6g}")
import pandas as pd
df = pd.DataFrame({"x": sample_xs, "f(x)": vals})
st.table(df)

st.markdown("---")
st.write("사용 팁: c=0이면 분모가 상수이므로 유리함수가 아니라 선형(또는 상수) 함수가 됩니다. 점근선과 정의역/치역 정보는 위의 설명을 참고하세요.")
