x = int(input())
to_500 = x // 500
du = x % 500
to_200 = du // 200
du = du % 200
to_100 = du // 100
print("Số từ 500: ", to_500)
print("Số từ 200: ", to_200)
print("Số từ 100: ", to_100)
