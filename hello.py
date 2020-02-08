#字典
'''dic = {'xmj': 40, 'zhang': 91, 'wang': 80}
for key, value in dic.items():
    print(key, value)
zxc = ('chen', 'wang', 'zhang', 'li')
zxc1 = (19, 20, 18, 25)
for i in range(4):
    dic1 = {'Name': zxc[i], 'Age': zxc1[i]}
    for key, value in dic1.items():
        print(key, value)'''
#习题练习(1)
'''import math
a = 1
b = 2
c = 3
d = 5
x = (math.sqrt(b * b - 4 * a * c)-b)/(2*a)
y = 4
z = (x*x+y*y)/(2*a)
v = (x+y+z)/math.sqrt(x*x*x+y*y*y+z*z*z)
n = (3+a)**2/(2*c+4*d)
m = 2*math.sin((x+y)/2)*math.cos((x-y)/2)
print(x)
print(z)
print(v)
print(n)
print(m)'''
#习题练习（2）
'''a = 7
b = -2
c = 4
x = 3*4**5/2
f = a*3%2
s = a%3+b*b-c//5
v = b**2-4*a*c
print(x, f, s, v)'''

#习题练习（3）
'''s = [9, 7, 8, 3, 2, 1, 55, 6]
print(len(s))
print(max(s))
print(min(s))
s.append(10)
s.remove(55)
print(s)'''

#迭代法
'''a = int(input("请输入被开方数:"))
x0 = a/2
x1 = (x0+a/x0)
while abs(x1-x0) > 0.00001:
    x0 = x1
    x1 = (x0+a/x0)/2
print("结果是:", x0)'''


# Word Jumble猜单词游戏
import random
# 创造单词序列
WORDS = ("python", "jumble", "easy", "difficult", "answer", "continue",
         "phone", "position", "game", "study", "encourage", "library",
         "school", "computer", "coffee", "foot", "teeth", "flew", "plane", "vocation")
# start the game
print(
"""
    欢迎参加猜单词游戏
  把字母组合成一个正确的单词
"""
)
iscontinue = "Y"
while iscontinue == "Y" or iscontinue == "y":
    # 从序列中选出一个单词
    word = random.choice(WORDS)
    # 一个用于判断玩家是否猜对的变量
    correct = word
    # 创建打乱后的单词
    jumble = ""
    while word: # word不是空串时循环
        # 根据word长度，产生word的随机位置
        position = random.randrange(len(word))
        # 将position位置字母组合到打乱后单词
        jumble += word[position]
        # 通过切片，将position位置字母从原单词中删除
        word = word[:position] + word[(position + 1):]
    print("乱序后单词:", jumble)
    guess = input("\n请你猜：")
    while guess != correct and guess != "":
        print("对不起,不正确")
        guess = input("继续猜：")
    if guess == correct:
        print("真棒,你猜对了!\n")
    iscontinue = input("\n\n是否继续(Y/N):")








