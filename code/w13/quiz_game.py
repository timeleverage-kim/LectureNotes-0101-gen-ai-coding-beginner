# quiz_game.py - 함수로 정리한 퀴즈 게임 (13주차)

quiz_list = [
    {"question": "대한민국의 수도는?", "answer": "서울"},
    {"question": "물은 섭씨 몇 도에서 끓을까요? (숫자만)", "answer": "100"},
    {"question": "파이썬(Python)이라는 이름은 어떤 동물에서 왔을까요?", "answer": "뱀"},
    {"question": "1 + 2 x 3 은?", "answer": "7"},
]


def is_correct(user_answer, answer):
    """사용자의 답이 정답인지 True/False로 알려 준다."""
    return user_answer.strip() == answer


def get_grade(score, total):
    """맞힌 개수에 따라 등급(글자)을 돌려준다."""
    if score == total:
        return "🏆 퀴즈 박사"
    elif score >= total / 2:
        return "👍 퀴즈 도전자"
    else:
        return "🌱 퀴즈 새싹"


def play(quizzes):
    """퀴즈를 한 문제씩 내고, 맞힌 개수를 돌려준다."""
    score = 0
    for quiz in quizzes:
        user_answer = input(quiz["question"] + " ")
        if is_correct(user_answer, quiz["answer"]):
            print("⭕ 정답!")
            score = score + 1
        else:
            print("❌ 오답! 정답은", quiz["answer"])
    return score


if __name__ == "__main__":
    print("=== 파이썬 퀴즈 ===")
    my_score = play(quiz_list)
    print("맞힌 개수:", my_score, "/", len(quiz_list))
    print("나의 등급:", get_grade(my_score, len(quiz_list)))
