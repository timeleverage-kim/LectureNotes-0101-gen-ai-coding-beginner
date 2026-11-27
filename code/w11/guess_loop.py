# guess_loop.py - 숫자 맞히기 게임 (최대 5번 도전)
import random

answer = random.randint(1, 20)
tries = 0

print("=== 숫자 맞히기 게임 (기회는 5번!) ===")

while tries < 5:
    guess = int(input("1부터 20 사이의 숫자: "))
    tries = tries + 1

    if guess == answer:
        print("🎉 정답! 도전", tries, "번 만에 맞혔어요!")
        break
    elif guess < answer:
        print("더 큰 숫자예요. ⬆️")
    else:
        print("더 작은 숫자예요. ⬇️")
else:
    print("아쉬워요! 정답은", answer, "였어요.")
