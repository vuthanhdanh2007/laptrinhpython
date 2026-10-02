giay = int(input())
h = giay // 3600
m = (giay % 3600) // 60
s = giay % 60
print(h,m,s, sep=":")
