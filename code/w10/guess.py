# guess.py - 숫자 맞히기 게임 (한 번만 도전)
import random

answer = random.randint(1, 20)   # 1~20 중 컴퓨터가 몰래 숫자 하나를 고른다

print("=== 숫자 맞히기 게임 ===")
guess = int(input("1부터 20 사이의 숫자를 맞혀 보세요: "))

if guess == answer:
    print("🎉 정답이에요!")
elif guess < answer:
    print("더 큰 숫자예요. ⬆️")
else:
    print("더 작은 숫자예요. ⬇️")

print("컴퓨터가 고른 숫자는", answer, "였어요.")
