import random

# 生成一个1到100之间的随机数
secret_number = random.randint(1, 100)

# 初始化猜测次数
guesses = 0

print("我想了一个1到100之间的数字。")

# 给用户最多6次机会来猜测数字
while guesses < 6:
    guess = int(input("你猜是多少？ "))
    guesses += 1

    if guess == secret_number:
        print("你猜对了！")
        break
    elif guess < secret_number:
        print("太小了！")
    else:
        print("太大了！")

# 如果用户用完了所有机会还没有猜对，就告诉他们正确的答案
if guesses == 6:
    print("抱歉，你没有猜对。我想的数字是 " + str(secret_number) + "。")
