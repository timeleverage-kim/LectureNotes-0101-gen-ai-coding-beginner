# check_quiz.py - "예상 결과"를 먼저 적어 두고, 실제 결과와 같은지 확인한다.
from quiz_game import get_grade, is_correct

assert is_correct(" 서울 ", "서울") == True      # 앞뒤 공백은 무시
assert is_correct("부산", "서울") == False

assert get_grade(4, 4) == "🏆 퀴즈 박사"
assert get_grade(2, 4) == "👍 퀴즈 도전자"      # 딱 절반도 도전자
assert get_grade(1, 4) == "🌱 퀴즈 새싹"

print("✅ 모든 확인을 통과했어요!")
