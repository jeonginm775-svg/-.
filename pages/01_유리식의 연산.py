# 5문제 퀴즈 데이터 정의 (Raw String으로 수정)
# r"" 를 사용하여 LaTeX 수식 내의 '\' 문자가 이스케이프되지 않도록 합니다.
quiz_data = [
    {
        "question": r"Q1. 다음 유리식 $\frac{x^2 - 4}{x^2 - 5x + 6}$ 를 간단히 하시오.",
        "options": [r"$\frac{x-2}{x+3}$", r"$\frac{x+2}{x-3}$", r"$\frac{x+2}{x+3}$", r"$\frac{x-3}{x+2}$"],
        "correct_index": 1,
        "rationale": r"분자 $x^2-4 = (x-2)(x+2)$, 분모 $x^2-5x+6 = (x-2)(x-3)$을 인수분해하여 공통 인수 $(x-2)$를 약분합니다."
    },
    {
        "question": r"Q2. $\frac{1}{x} + \frac{1}{x+1}$ 을 계산하시오.",
        "options": [r"$\frac{2}{x(x+1)}$", r"$\frac{2x+1}{x(x+1)}$", r"$\frac{x+1}{x^2+x}$", r"$\frac{x+1}{2x+1}$"],
        "correct_index": 1,
        "rationale": r"공통분모 $x(x+1)$로 통분하면 $\frac{x+1}{x(x+1)} + \frac{x}{x(x+1)} = \frac{2x+1}{x(x+1)}$ 입니다."
    },
    {
        "question": r"Q3. $\frac{x}{x-1} - \frac{1}{1-x}$ 을 계산하시오.",
        "options": [r"$\frac{x-1}{x-1}$", r"$\frac{x+1}{x-1}$", r"$\frac{x-1}{2}$", r"$1$"],
        "correct_index": 1,
        "rationale": r"$\frac{1}{1-x} = \frac{-1}{x-1}$ 이므로 $\frac{x}{x-1} - \frac{-1}{x-1} = \frac{x+1}{x-1}$ 입니다."
    },
    {
        "question": r"Q4. $\frac{x+2}{x^2 - 1} \times \frac{x-1}{x^2 + 4x + 4}$ 을 간단히 하시오.",
        "options": [r"$\frac{x-1}{(x-1)(x+2)}$", r"$\frac{1}{(x+1)(x+2)}$", r"$\frac{1}{x+1}$", r"$\frac{1}{x+2}$"],
        "correct_index": 1,
        "rationale": r"$\frac{x+2}{(x-1)(x+1)} \times \frac{x-1}{(x+2)^2}$ 로 인수분해하여 약분하면 $\frac{1}{(x+1)(x+2)}$ 입니다."
    },
    {
        "question": r"Q5. $(\frac{1}{a} - \frac{1}{b}) \div \frac{b^2 - a^2}{a^2 b^2}$ 을 계산하시오.",
        "options": [r"$\frac{a+b}{ab}$", r"$\frac{1}{a+b}$", r"$\frac{ab}{a+b}$", r"$a+b$"],
        "correct_index": 2,
        "rationale": r"$\frac{b-a}{ab} \times \frac{a^2 b^2}{(b-a)(b+a)}$ 이 되어 약분하면 $\frac{ab}{a+b}$ 입니다."
    }
