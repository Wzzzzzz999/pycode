# """ 用Python设计第一个游戏 """

temp = input("不妨猜一下王峥峥现在心里想的是哪一个数字:")
guess = int(temp)
if guess == 8:
     print("你是王峥峥心里的蛔虫嘛? ! ")
     print("哼，猜中了也没奖励! ")
else:
    if guess <8:
         print("小了~")
    else:
         print("大啦~ ")

print("游戏结束，不玩啦^-^ ")
 
