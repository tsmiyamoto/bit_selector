import random

import winsound


amount = input("金額を入力してください: ")

bits = format(int(amount), "b")

bits_reversed = "".join(list(reversed(bits)))


# mixer.init()
# mixer.music.load("drum.wav")

print(bits)
people = ["A", "B", "C", "D"]
amounts = [0, 0, 0, 0]
FLAG = True

for i, bit in enumerate(bits_reversed):
    num_bit = len(bits) - i
    rand = random.randint(0, len(people) - 1)
    print(f"{i + 1}ビット目 ({(2 ** i) * int(bit)}円) ")
    # input()
    # mixer.music.play(1)
    # playsound("drum.wav")
    winsound.PlaySound("drum.wav", winsound.SND_FILENAME)

    print(people[rand], "さんが支払い！")
    # while True:
    #     rand = random.randint(0, 3)
    #     print(people[rand])
    #     time.sleep(0.5)
    #     inp = input()
    #     if inp != "":
    #         FLAG = False
    #         break

    amounts[rand] += (2 ** i) * int(bit)

    print("\n小計")
    for i in range(len(people)):
        print(f"{people[i]}: {amounts[i]}円")
    # print(amounts)
    input()
