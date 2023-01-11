# w - 너비
# h - 높이
# b - 비트 개수
# 계산 -> w*h*b

w, h, b = list(map(lambda n: int(n), input().split(' ')))
print(f'{w*h*b/8/1024/1024:.2f} MB')