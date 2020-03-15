#Jump 7 game
print("Let's playing the jump seven game")

for i in range(1,101):
    if i == 7:
        continue
    elif i % 10 ==7:
        continue
    elif i // 10 == 7:
        continue
    else:
        print(i, end = ' ')