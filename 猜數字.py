print("bc1210003張智鈞")

import random

def guess_number(answer):
    min_num = 1
    max_num = 100
    while True:
        guess = int(input(f"請猜一個介於 {min_num} 和 {max_num} 之間的數字: "))
        if guess == answer:
            print("恭喜你，猜對了！")
            break
        elif guess < answer:
            min_num = guess + 1
            print("猜錯了，猜的數字比答案小。")
        else:
            max_num = guess - 1
            print("猜錯了，猜的數字比答案大。")
        if min_num > max_num:
            print("沒有可猜的數字了！")
            break

if __name__ == "__main__":
    answer = random.randint(1, 100)
    print("歡迎來到猜數字遊戲！")
    guess_number(answer)
