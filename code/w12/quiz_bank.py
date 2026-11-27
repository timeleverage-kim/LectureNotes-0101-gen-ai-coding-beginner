# quiz_bank.py - 퀴즈 문제은행 (리스트와 딕셔너리)

quiz_list = [
    {"question": "대한민국의 수도는?", "answer": "서울"},
    {"question": "물은 섭씨 몇 도에서 끓을까요? (숫자만)", "answer": "100"},
    {"question": "파이썬(Python)이라는 이름은 어떤 동물에서 왔을까요?", "answer": "뱀"},
    {"question": "1 + 2 x 3 은?", "answer": "7"},
]

score = 0
print("=== 파이썬 퀴즈 ===")

for quiz in quiz_list:
    user_answer = input(quiz["question"] + " ")
    if user_answer.strip() == quiz["answer"]:
        print("⭕ 정답!")
        score = score + 1
    else:
        print("❌ 오답! 정답은", quiz["answer"])

print("맞힌 개수:", score, "/", len(quiz_list))
