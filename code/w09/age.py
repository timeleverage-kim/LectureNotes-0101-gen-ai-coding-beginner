# age.py - 나이 계산기
this_year = 2026

print("=== 나이 계산기 ===")
name = input("이름을 입력하세요: ")
birth_year = int(input("태어난 해를 입력하세요 (예: 2007): "))

age = this_year - birth_year
dog_age = age * 7

print(name, "님은 올해", age, "살이에요.")
print("강아지 나이로 바꾸면", dog_age, "살이래요! 🐶")
