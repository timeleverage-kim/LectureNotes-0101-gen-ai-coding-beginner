# gugudan.py - 구구단 외우기
dan = int(input("몇 단을 볼까요? "))

for i in range(1, 10):
    print(dan, "x", i, "=", dan * i)
