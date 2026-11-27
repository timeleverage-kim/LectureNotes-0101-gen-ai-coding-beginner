# quiz_game.py - 최고 점수를 파일에 저장하는 퀴즈 게임 (14주차 완성본)

SCORE_FILE = "best_score.txt"

quiz_list = [
    {"question": "대한민국의 수도는?", "answer": "서울"},
    {"question": "물은 섭씨 몇 도에서 끓을까요? (숫자만)", "answer": "100"},
    {"question": "파이썬(Python)이라는 이름은 어떤 동물에서 왔을까요?", "answer": "뱀"},
    {"question": "1 + 2 x 3 은?", "answer": "7"},
]


def is_correct(user_answer, answer):
    return user_answer.strip() == answer


def get_grade(score, total):
    if score == total:
        return "🏆 퀴즈 박사"
    elif score >= total / 2:
        return "👍 퀴즈 도전자"
    else:
        return "🌱 퀴즈 새싹"


def play(quizzes):
    score = 0
    for quiz in quizzes:
        user_answer = input(quiz["question"] + " ")
        if is_correct(user_answer, quiz["answer"]):
            print("⭕ 정답!")
            score = score + 1
        else:
            print("❌ 오답! 정답은", quiz["answer"])
    return score


def load_best_score():
    """저장된 최고 점수를 읽는다. 파일이 없으면 0점."""
    try:
        with open(SCORE_FILE, "r", encoding="utf-8") as f:
            return int(f.read())
    except (FileNotFoundError, ValueError):
        return 0


def save_best_score(score):
    """최고 점수를 파일에 적는다."""
    with open(SCORE_FILE, "w", encoding="utf-8") as f:
        f.write(str(score))


if __name__ == "__main__":
    print("=== 파이썬 퀴즈 ===")
    best = load_best_score()
    print("지금까지의 최고 점수:", best)

    my_score = play(quiz_list)
    print("맞힌 개수:", my_score, "/", len(quiz_list))
    print("나의 등급:", get_grade(my_score, len(quiz_list)))

    if my_score > best:
        save_best_score(my_score)
        print("🎉 최고 점수를 새로 썼어요!")
