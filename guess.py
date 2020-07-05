# 产生一个随机整数1~100 （不要印出来）
# 让使用者重复输入数字去猜
# 猜对： 印出 “终于猜对了！”
# 猜错： 要告诉他比答案大、小

import random
r = random.randint(1,100)
count = 0 # 计数
while True:
	count += 1 # count = count + 1
	num = input('请输入1至100间的整数： ')
	num = int(num)
	if num == r:
		print('终于猜对了！')
		print('一共用了', count, '次猜对！')
		break
	elif num < r:
		print('您猜的太小了。')
	else:
		print('您猜的太大了。')
	print('这是第', count, '次猜测')
