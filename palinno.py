x = int(input())
y = x
r = 0
while y != 0:
	r = (r * 10) + (y % 10)
	y = y// 10
if x == r:
	print("yes")
else:
	print("no")
