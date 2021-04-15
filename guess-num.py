import random

start = input('請決定隨機數字開始值：')
end = input('請決定隨機數字結束值：')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	num = input('請猜數字：')
	num = int(num)
	count += 1
	if num == r:
		print('答對了')
		print('目前猜第', count, '次')
		break
	elif num > r:
		print('太大了')
	elif num < r:
		print('太小了')
	print('目前猜第', count, '次')