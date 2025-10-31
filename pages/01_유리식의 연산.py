import streamlit as st

# 5문제 퀴즈 데이터 정의 (질문 텍스트와 수학 수식을 분리하여 표시 오류 해결)
quiz_data = [
    {
        "question_text": "Q1. 다음 유리식을 간단히 하시오.",
        "question_math": r"\frac{x^2 - 4}{x^2 - 5x + 6}", # 순수 수식 (달러 기호 제거)
        "options": [r"$\frac{x-2}{x+3}$", r"$\frac{x+2}{x-3}$", r"$\frac{x+2}{x+3}$", r"$\frac{x-3}{x+2}$"],
        "correct_index": 1,
        "rationale": r"분자 $x^2-4 = (x-2)(x+2)$, 분모 $x^2-5x+6 = (x-2)(x-3)$을 인수분해하여 공통 인수 $(x-2)$를 약분합니다."
    },
    {
        "question_text": "Q2. 다음 식을 계산하시오.",
        "question_math": r"\frac{1}{x} + \frac{1}{x+1}",
        "options": [r"$\frac{2}{x(x+1)}$", r"$\frac{2x+1}{x(x+1)}$", r"$\frac{x+1}{x^2+x}$", r"$\frac{x+1}{2x+1}$"],
        "correct_index": 1,
        "rationale": r"공통분모 $x(x+1)$로 통분하면 $\frac{x+1}{x(x+1)} + \frac{x}{x(x+1)} = \frac{2x+1}{x(x+1)}$ 입니다."
    },
    {
        "question_text": "Q3. 다음 식을 계산하시오.",
        "question_math": r"\frac{x}{x-1} - \frac{1}{1-x}",
        "options": [r"$\frac{x-1}{x-1}$", r"$\frac{x+1}{x-1}$", r"$\frac{x-1}{2}$", r"$1$"],
        "correct_index": 1,
        "rationale": r"$\frac{1}{1-x} = \frac{-1}{x-1}$ 이므로 $\frac{x}{x-1} - \frac{-1}{x-1} = \frac{x+1}{x-1}$ 입니다."
    },
    {
        "question_text": "Q4. 다음 식을 간단히 하시오.",
        "question_math": r"\frac{x+2}{x^2 - 1} \times \frac{x-1}{x^2 + 4x + 4}",
        "options": [r"$\frac{x-1}{(x-1)(x+2)}$", r"$\frac{1}{(x+1)(x+2)}$", r"$\frac{1}{x+1}$", r"$\frac{1}{x+2}$"],
        "correct_index": 1,
        "rationale": r"$\frac{x+2}{(x-1)(x+1)} \times \frac{x-1}{(x+2)^2}$ 로 인수분해하여 약분하면 $\frac{1}{(x+1)(x+2)}$ 입니다."
    },
    {
        "question_text": "Q5. 다음 식을 계산하시오.",
        "question_math": r"(\frac{1}{a} - \frac{1}{b}) \div \frac{b^2 - a^2}{a^2 b^2}",
        "options": [r"$\frac{a+b}{ab}$", r"$\frac{1}{a+b}$", r"$\frac{ab}{a+b}$", r"$a+b$"],
        "correct_index": 2,
        "rationale": r"$\frac{b-a}{ab} \times \frac{a^2 b^2}{(b-a)(b+a)}$ 이 되어 약분하면 $\frac{ab}{a+b}$ 입니다."
    }
]

# Streamlit 세션 상태 초기화
if 'current_q_index' not in st.session_state:
    st.session_state.current_q_index = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'correct_answers' not in st.session_state:
    st.session_state.correct_answers = [False] * len(quiz_data)
if 'quiz_finished' not in st.session_state:
    st.session_state.quiz_finished = False

# 고양이 그림을 점수에 따라 단계별로 그리는 함수 (ASCII Art)
def draw_cat(score):
    if score == 0:
        cat_art = r"""
 /\_/\  (0점: 시작!)
( o.o ) 
 > ^ <
        """
    elif score == 1:
        cat_art = r"""
 /\_/\  (1점: 귀 하나)
( o.o ) 
 > ^ < 
  ( )
        """
    elif score == 2:
        cat_art = r"""
 /\_/\  (2점: 머리와 몸통)
( o.o )
 > ^ <
  (   )
 (  .  )
        """
    elif score == 3:
        cat_art = r"""
 /\_/\  (3점: 꼬리 추가)
( o.o )
 > ^ <   
  (   )
 (  .  )
/      \
        """
    elif score == 4:
        cat_art = r"""
 /\_/\  (4점: 다리와 발)
( o.o )
 > ^ <   
  (   )
 (  .  )
/      \
|  /\  |
        """
    elif score == 5:
        cat_art = r"""
 /\_/\  (5점: 완전한 고양이!) 😸
( *.* )  <- 유리식 연산 마스터!
 > ^ <
  (   )
 (  .  )
/      \
|  /\  |
| /  \ |
~~~~~~~~
        """
    else:
        cat_art = "고양이 그리기 오류"

    st.markdown(f"```\n{cat_art}\n```")
    st.progress(score / len(quiz_data))
    st.markdown(f"**현재 점수: {score} / 5**")


# 퀴즈 제출 핸들러
def submit_answer(selected_option_index):
    current_q = quiz_data[st.session_state.current_q_index]

    if st.session_state.correct_answers[st.session_state.current_q_index]:
        st.error("이미 정답을 맞힌 문제입니다. '다음 문제' 버튼을 이용해 다른 문제로 이동해 주세요.")
        return

    # 정답 확인
    if selected_option_index == current_q["correct_index"]:
        st.success("🎉 정답입니다! 다음 고양이 조각을 얻었어요!")
        
        # 정답 처리
        st.session_state.score += 1
        st.session_state.correct_answers[st.session_state.current_q_index] = True
        
        if st.session_state.score == len(quiz_data):
            st.session_state.quiz_finished = True
        
        # 상태 변경을 반영하기 위해 앱을 다시 실행 (수정된 함수)
        st.rerun() 
        
    else:
        st.error("❌ 오답입니다. 다시 한번 생각해 보세요.")
        st.markdown(f"**정답 해설:** {current_q['rationale']}")

# 메인 앱
def app():
    st.title("😸 유리식 연산 마스터 퀴즈")
    st.subheader("정답을 맞힐 때마다 고양이가 완성됩니다!")
    st.latex(r"\text{현재 진행률 (고양이 완성도)}")
    draw_cat(st.session_state.score)
    st.markdown("---")
    
    # 퀴즈가 끝나지 않았을 경우 문제 표시
    if not st.session_state.quiz_finished:
        q_index = st.session_state.current_q_index
        current_q = quiz_data[q_index]

        st.header(f"문제 {q_index + 1}.")
        # 텍스트와 수식을 분리하여 렌더링 (질문 표시 오류 수정)
        st.markdown(current_q["question_text"])
        st.latex(current_q["question_math"]) 
        
        # 라디오 버튼으로 보기 표시
        selected_option = st.radio(
            "답을 선택하세요:",
            options=current_q["options"],
            key=f"q_{q_index}_options",
            index=None, 
            format_func=lambda x: f"{x}"
        )
        
        # 제출 버튼
        if st.button("답안 제출"):
            if selected_option is not None:
                # 선택된 옵션의 인덱스를 찾음
                selected_index = current_q["options"].index(selected_option)
                submit_answer(selected_index)
            else:
                st.warning("답을 선택해 주세요.")

        st.markdown("---")
        
        # 현재 문제 인덱스 관리 (이전/다음 버튼)
        col1, col2 = st.columns(2)
        with col1:
            if st.session_state.current_q_index > 0:
                if st.button("⬅️ 이전 문제"):
                    st.session_state.current_q_index -= 1
                    st.rerun()
        with col2:
            if st.session_state.current_q_index < len(quiz_data) - 1:
                if st.button("다음 문제 ➡️"):
                    st.session_state.current_q_index += 1
                    st.rerun() 
            elif st.session_state.current_q_index == len(quiz_data) - 1:
                st.write("마지막 문제입니다.")
        
        # 정답 여부 표시
        if st.session_state.correct_answers[q_index]:
            st.info("✅ 이 문제는 이미 정답을 맞혔습니다.")
            
    else:
        # 퀴즈 완료 시
        st.balloons()
        st.header("🎉 퀴즈 완료!")
        st.success("모든 문제를 맞히고 고양이를 완성했습니다! 유리식 연산 마스터입니다!")
        
        if st.button("퀴즈 다시 시작"):
            # 세션 상태 초기화
            st.session_state.current_q_index = 0
            st.session_state.score = 0
            st.session_state.correct_answers = [False] * len(quiz_data)
            st.session_state.quiz_finished = False
            st.rerun()

if __name__ == "__main__":
    app()
