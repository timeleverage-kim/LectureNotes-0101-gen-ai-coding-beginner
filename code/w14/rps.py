# rps.py - 가위바위보 (보너스)
import random

choices = ["가위", "바위", "보"]
win_table = {"가위": "보", "바위": "가위", "보": "바위"}   # 왼쪽이 오른쪽을 이긴다

print("=== 가위바위보 ===")
me = input("가위, 바위, 보 중에 하나를 내세요: ")
computer = random.choice(choices)
print("컴퓨터:", computer)

if me not in choices:
    print("가위, 바위, 보 중에서만 낼 수 있어요!")
elif me == computer:
    print("비겼어요! 😮")
elif win_table[me] == computer:
    print("이겼어요! 🎉")
else:
    print("졌어요... 😢")
